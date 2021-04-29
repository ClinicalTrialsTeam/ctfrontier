import logging
from collections import OrderedDict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create a logger for this file
logger = logging.getLogger(__name__)

from ctgov.models import (
    BriefSummaries,
    SearchStudies,
    Facilities,
    BrowseConditions,
    Interventions,
    Sponsors,
)
from .serializers import (
    BriefSummariesSerializer,
    SearchStudiesSerializer,
    serialize_countries,
    SearchStudiesDocumentSerializer,
    ConditionsSerializer,
    StatesSerializer,
    CitySerializer,
    StudyDetailSerializer,
    TrialTimelinesSerializer,
)
from datetime import datetime
from django.db.models import Q, Count

from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)

from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination
from ctgov.documents import ClinicalTrialsSearchStudies


# API end point for elastic search
class SearchStudiesDocumentView(BaseDocumentViewSet):
    document = ClinicalTrialsSearchStudies
    serializer_class = SearchStudiesDocumentSerializer
    pagination_class = PageNumberPagination

    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]

    search_fields = (
        "status",
        "brief_title",
        "nct_id",
        "condition_name",
        "study_detailed_desc",
        "country_name",
        "intervention_name",
        "eligibility_criteria",
        "study_brief_desc",
        "location_name",
    )

    ordering_fields = {
        "status": "status.raw",
        "country_name": "country_name.raw",
    }


# Test API call to get brief summaries of clinical studies
class BriefSummariesListApiView(APIView):
    def get(self, request, *args, **kwargs):
        summaries = BriefSummaries.objects.all()[:10]
        serializer = BriefSummariesSerializer(summaries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# API to get list of contries where trials are conducted
# This is for the front-end user interface control to display country drop-down
class CountriesListApiView(APIView):
    def get(self, request, *args, **kwargs):
        logger.info("CountriesListApiView: get()")
        countries = (
            Facilities.objects.all()
            .distinct()
            .values("country")
            .exclude(country="")
            .exclude(country="United States")
            .order_by("country")
        )

        logger.info("CountriesListApiView: Before serialize.")
        serialized = serialize_countries(countries)
        logger.info("CountriesListApiView: After serialize")

        # Insert US first
        # (serializer.data is immutable so we must create a new object)
        us = OrderedDict()
        us["country"] = "United States"
        data = [us]
        data.extend(serialized)

        r = Response(data, status=status.HTTP_200_OK)
        logger.info("CountriesListApiView: Complete")
        return r


# API to get list of conditions
# This is to auto-suggest condition names to users when they type in condition text field
class ConditionsListApiView(APIView):
    def get(self, request, *args, **kwargs):
        conditions = (
            BrowseConditions.objects.all()
            .distinct()
            .order_by("mesh_term")
            .values("mesh_term")
        )
        serializer = ConditionsSerializer(conditions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# API to get list of states in United States
class StatesListApiView(APIView):
    def get(self, request, *args, **kwargs):
        states = (
            Facilities.objects.filter(country="United States")
            .values("state")
            .distinct()
            .order_by("state")
        )
        serializer = StatesSerializer(states, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# API to get list of cities
class CitiesListApiView(APIView):
    def get(self, request, *args, **kwargs):
        cities = (
            Facilities.objects.all()
            .distinct()
            .order_by("city")
            .values("city")
            .exclude(city="")
        )
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# API to get single trial details
class StudyDetailApiView(APIView):
    def post(self, request, *args, **kwargs):
        nct_id = request.data.get("nct_id")

        study = SearchStudies.objects.all().filter(nct_id=nct_id)
        serializer = StudyDetailSerializer(study, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# API to get trial timelines based on comma separated NCT_IDs
class TrialTimelinesApiView(APIView):
    def post(self, request, *args, **kwargs):
        logger.info("TrialTimelinesApiView: get()")
        nct_ids = request.data.get("nct_ids")
        ncts = str(nct_ids).split(",")
        nct_list = [str(item).strip(" ") for item in ncts]

        trial_timelines = (
            SearchStudies.objects.all()
            .filter(nct_id__in=nct_list)
            .values(
                "nct_id",
                "study_start_date",
                "primary_completion_date",
                "study_phase",
            )
        )
        logger.info("TrialTimelinesApiView: Before serialize")
        serializer = TrialTimelinesSerializer(trial_timelines, many=True)
        logger.info("TrialTimelinesApiView: After serialize")
        r = Response(serializer.data, status=status.HTTP_200_OK)
        logger.info("TrialTimelinesApiView: Complete")
        return r


# API to export search results
class SearchResultsExportApiView(APIView):
    def post(self, request, *args, **kwargs):
        logger.info("SearchResultsExportApiView: post()")
        filters = construct_filters(request)
        q_title_acronym = filter_title_acronym(request)
        q_outcome_measure = filter_outcome_measure(request)
        q_eligibility_age = filter_eligibility_age(request)
        q_age_between = filter_age_between(request)
        q_study_roa = filter_study_roa(request)
        q_study_status = filter_study_status(request)
        q_phase = filter_phase(request)

        filter_results = (
            SearchStudies.objects.filter(**filters)
            .filter(q_title_acronym)
            .filter(q_outcome_measure)
            .filter(q_eligibility_age)
            .filter(q_age_between)
            .filter(q_study_roa)
            .filter(q_study_status)
            .filter(q_phase)
            .all()
        )

        serializer = SearchStudiesSerializer(filter_results, many=True)
        logger.info("SearchResultsExportApiView: return response")
        return Response(serializer.data, status=status.HTTP_200_OK)


# API to get Trials Dashboard Metadata
class TrialsDashboardApiView(APIView):
    def post(self, request, *args, **kwargs):
        filters = construct_filters(request)
        q_title_acronym = filter_title_acronym(request)
        q_outcome_measure = filter_outcome_measure(request)
        q_eligibility_age = filter_eligibility_age(request)
        q_age_between = filter_age_between(request)
        q_study_roa = filter_study_roa(request)
        q_study_status = filter_study_status(request)
        q_phase = filter_phase(request)

        filter_results = (
            SearchStudies.objects.filter(**filters)
            .filter(q_title_acronym)
            .filter(q_outcome_measure)
            .filter(q_eligibility_age)
            .filter(q_age_between)
            .filter(q_study_roa)
            .filter(q_study_status)
            .filter(q_phase)
            .all()
        )

        trials_dashboard_phase = (
            filter_results.all()
            .values("study_phase")
            .annotate(trials_count=Count("nct_id"))
        )
        trials_dashboard_status = (
            filter_results.all()
            .values("status")
            .annotate(trials_count=Count("nct_id"))
        )
        trials_dashboard_interventions = (
            Interventions.objects.all()
            .values("intervention_type")
            .annotate(trials_count=Count("nct", distinct=True))
            .filter(nct__in=filter_results.all().values("nct_id"))
        )
        trials_dashboard_sponsors = (
            Sponsors.objects.all()
            .values("name")
            .annotate(trials_count=Count("nct", distinct=True))
            .filter(nct__in=filter_results.all().values("nct_id"))
            .order_by("-trials_count")[:10]
        )

        return Response(
            {
                "sponsors": trials_dashboard_sponsors,
                "phases": trials_dashboard_phase,
                "interventions": trials_dashboard_interventions,
                "status": trials_dashboard_status,
            },
            status=status.HTTP_200_OK,
        )


# Define post action for the API call
# Validate each parameter and construct AND, OR, Contains operators
# Return results along with metadata
class SearchStudiesApiView(APIView):
    def post(self, request, *args, **kwargs):
        logger.info("SearchStudiesApiView: post()")
        logger.warning(f"{type(request)} - {request}")
        first = request.data.get("first")
        last = request.data.get("last")
        metadata_required = request.data.get("metadata_required")

        if not first:
            first = 0
        if not last:
            last = 100

        filters = construct_filters(request)
        q_title_acronym = filter_title_acronym(request)
        q_outcome_measure = filter_outcome_measure(request)
        q_eligibility_age = filter_eligibility_age(request)
        q_age_between = filter_age_between(request)
        q_study_roa = filter_study_roa(request)
        q_study_status = filter_study_status(request)
        q_phase = filter_phase(request)

        if metadata_required:
            search_results_all = (
                SearchStudies.objects.filter(**filters)
                .filter(q_title_acronym)
                .filter(q_outcome_measure)
                .filter(q_eligibility_age)
                .filter(q_age_between)
                .filter(q_study_roa)
                .filter(q_study_status)
                .filter(q_phase)
                .all()
            )

            search_results = search_results_all.all().values(
                "status",
                "brief_title",
                "nct_id",
                "condition_name",
                "intervention_name",
                "location_name",
                "study_phase",
                "sponsor_name",
                "location_name",
                "study_brief_desc",
                "primary_outcome_measures",
                "secondary_outcome_measures",
                "study_start_date",
                "primary_completion_date",
            )[first:last]

            results_count = search_results_all.count()

        else:
            search_results = (
                SearchStudies.objects.filter(**filters)
                .filter(q_title_acronym)
                .filter(q_outcome_measure)
                .filter(q_eligibility_age)
                .filter(q_age_between)
                .filter(q_study_roa)
                .filter(q_study_status)
                .filter(q_phase)
                .all()
                .values(
                    "status",
                    "brief_title",
                    "nct_id",
                    "condition_name",
                    "intervention_name",
                    "location_name",
                    "study_phase",
                    "sponsor_name",
                    "location_name",
                    "study_brief_desc",
                    "primary_outcome_measures",
                    "secondary_outcome_measures",
                    "study_start_date",
                    "primary_completion_date",
                )[first:last]
            )

            results_count = "NA"

        serializer = SearchStudiesSerializer(search_results, many=True)
        logger.info("SearchStudiesApiView: return results")
        logger.warning(
            f"SearchStudiesApiView: {results_count} results - {serializer.data}"
        )
        return Response(
            {
                "metadata": [{"results_count": str(results_count)}],
                "search_results": serializer.data,
            },
            status=status.HTTP_200_OK,
        )


# Convert passed date parameter to match with db format
def convert_to_date(datestr):
    date = datetime.strptime(datestr, "%Y-%m-%d")
    return date


# Check whether passed date parameter is valid
def valid_date(datestr):
    status = True
    try:
        if datestr:
            datetime.strptime(str(datestr), "%Y-%m-%d")
        else:
            status = False
    except (ValueError):
        status = False

    return status


# Check whether passed date age parameter is either integer or float
def valid_number(agestr):
    status = True
    try:
        if agestr:
            status = isinstance(float(agestr), float)
        else:
            status = False
    except (ValueError):
        status = False

    return status


# Convert passed age parameter to number
def convert_to_number(agestr):
    return float(agestr)


# Function to construct filters based on search parameters posted to REST API
def construct_filters(request):
    nct_id = request.data.get("nct_id")
    condition = request.data.get("condition")
    condition_terms = request.data.get("condition_terms")
    other_terms = request.data.get("other_terms")
    country = request.data.get("country")
    city = request.data.get("city")
    state = request.data.get("state")
    intervention = request.data.get("intervention")
    target_moa = request.data.get("target")
    eligibility_criteria = request.data.get("eligibility_criteria")

    # new fields based on client demo
    modality = request.data.get("modality")
    sponsor = request.data.get("sponsor")
    start_date_from = request.data.get("start_date_from")
    start_date_to = request.data.get("start_date_to")
    primary_completion_date_from = request.data.get(
        "primary_completion_date_from"
    )
    primary_completion_date_to = request.data.get("primary_completion_date_to")
    first_posted_date_from = request.data.get("first_posted_date_from")
    first_posted_date_to = request.data.get("first_posted_date_to")
    results_first_posted_date_from = request.data.get(
        "results_first_posted_date_from"
    )
    results_first_posted_date_to = request.data.get(
        "results_first_posted_date_to"
    )
    last_update_posted_date_from = request.data.get(
        "last_update_posted_date_from"
    )
    last_update_posted_date_to = request.data.get("last_update_posted_date_to")

    # Advanced search parameters
    study_results = request.data.get("study_results")
    study_type = request.data.get("study_type")
    eligibility_gender = request.data.get("eligibility_gender")
    eligibility_ethnicity = request.data.get("eligibility_ethnicity")
    eligibility_condition = request.data.get("eligibility_condition")
    eligibility_healthy_volunteer = request.data.get(
        "eligibility_healthy_volunteer"
    )
    study_collaborator = request.data.get("study_collaborator")
    study_ids = request.data.get("study_ids")
    study_location_terms = request.data.get("study_location_terms")
    study_funder_type = request.data.get("study_funder_type")
    study_document_type = request.data.get("study_document_type")
    study_results_submitted = request.data.get("study_results_submitted")

    # Construct filter map object
    if not nct_id:
        nct_id = ""

    filters = {"nct_id__icontains": nct_id}
    if condition:
        filters["condition_name__icontains"] = condition
    if condition_terms:
        filters["condition_name__icontains"] = condition_terms
    if other_terms:
        filters["brief_title__icontains"] = other_terms
    if country:
        filters["country_name__icontains"] = country
    if city:
        filters["city_name__icontains"] = city
    if state:
        filters["state_name__icontains"] = state
    if intervention:
        filters["intervention_name__icontains"] = intervention
    if target_moa:
        filters["study_brief_desc__icontains"] = target_moa
    if eligibility_criteria:
        filters["eligibility_criteria__icontains"] = eligibility_criteria
    if modality:
        filters["study_detailed_desc__icontains"] = modality
    if sponsor:
        filters["sponsor_name__icontains"] = sponsor
    if valid_date(start_date_from):
        filters["study_start_date__gte"] = convert_to_date(start_date_from)
    if valid_date(start_date_to):
        filters["study_start_date__lte"] = convert_to_date(start_date_to)
    if valid_date(primary_completion_date_from):
        filters["primary_completion_date__gte"] = convert_to_date(
            primary_completion_date_from
        )
    if valid_date(primary_completion_date_to):
        filters["primary_completion_date__lte"] = convert_to_date(
            primary_completion_date_to
        )
    if valid_date(first_posted_date_from):
        filters["study_first_posted_date__gte"] = convert_to_date(
            first_posted_date_from
        )
    if valid_date(first_posted_date_to):
        filters["study_first_posted_date__lte"] = convert_to_date(
            first_posted_date_to
        )
    if valid_date(results_first_posted_date_from):
        filters["results_first_posted_date__gte"] = convert_to_date(
            results_first_posted_date_from
        )
    if valid_date(results_first_posted_date_to):
        filters["results_first_posted_date__lte"] = convert_to_date(
            results_first_posted_date_to
        )
    if valid_date(last_update_posted_date_from):
        filters["last_update_posted_date__gte"] = convert_to_date(
            last_update_posted_date_from
        )
    if valid_date(last_update_posted_date_to):
        filters["last_update_posted_date__lte"] = convert_to_date(
            last_update_posted_date_to
        )
    if study_results:
        if str(study_results).lower() == "studies with results":
            filters["results_first_posted_date__isnull"] = False
        if str(study_results).lower() == "studies without results":
            filters["results_first_posted_date__isnull"] = True
    if study_type:
        filters["study_type__icontains"] = study_type
    if eligibility_gender:
        filters["eligibility_gender__iexact"] = eligibility_gender
    if eligibility_ethnicity:
        filters["eligibility_criteria__icontains"] = eligibility_ethnicity
    if eligibility_condition:
        filters["eligibility_criteria__icontains"] = eligibility_condition
    if eligibility_healthy_volunteer:
        filters[
            "healthy_volunteers__icontains"
        ] = eligibility_healthy_volunteer
    if study_collaborator:
        filters["sponsor_name__icontains"] = study_collaborator
    if study_ids:
        filters["study_ids__icontains"] = study_ids
    if study_location_terms:
        filters["location_name__icontains"] = study_location_terms
    if study_funder_type:
        filters["funder_type__icontains"] = study_funder_type
    if study_document_type:
        filters["document_types__icontains"] = study_document_type
    if study_results_submitted:
        if str(study_results_submitted).lower() == "not submitted":
            filters["results_submitted_qc_not_done__isnull"] = True
        if str(study_results_submitted).lower() == "submitted":
            filters["results_submitted_qc_not_done__isnull"] = False
        if str(study_results_submitted).lower() == "qc done":
            filters["results_submitted_qc_done__isnull"] = False

    return filters


# Function to construct queryset filter for title acronym
def filter_title_acronym(request):
    study_title_acronym = request.data.get("study_title_acronym")

    q_title_acronym = Q()
    if study_title_acronym:
        q_title_acronym = Q(official_title__icontains=study_title_acronym) | Q(
            acronym__icontains=study_title_acronym
        )

    return q_title_acronym


# Function to construct queryset filter for outcome measure
def filter_outcome_measure(request):
    study_outcome_measure = request.data.get("study_outcome_measure")

    q_outcome_measure = Q()
    if study_outcome_measure:
        q_outcome_measure = Q(
            primary_outcome_measures__icontains=study_outcome_measure
        ) | Q(secondary_outcome_measures__icontains=study_outcome_measure)

    return q_outcome_measure


# Function to construct queryset filter for eligibility age
def filter_eligibility_age(request):
    eligibility_age = request.data.get("eligibility_age")

    q_eligibility_age = Q()
    if valid_number(eligibility_age):
        q_eligibility_age = Q(
            eligibility_min_age_numeric=convert_to_number(eligibility_age)
        ) | Q(eligibility_max_age_numeric=convert_to_number(eligibility_age))

    return q_eligibility_age


# Function to construct queryset filter for age groups
def filter_age_between(request):
    eligibility_age_group = request.data.get("eligibility_age_group")

    q_age_between = Q()
    if eligibility_age_group:
        age_group_list = str(eligibility_age_group).split(",")
        age_group_queries = []
        for age_group in age_group_list:
            if age_group.lower().strip(" ") == "child":
                age_group_queries.append(
                    Q(eligibility_min_age_numeric__gte=0)
                    & Q(eligibility_min_age_numeric__lte=17)
                    & (
                        Q(eligibility_max_age_numeric=0)
                        | Q(eligibility_max_age_numeric__lte=17)
                    )
                )
            if age_group.lower().strip(" ") == "adult":
                age_group_queries.append(
                    Q(eligibility_min_age_numeric__gte=0)
                    & (
                        Q(eligibility_max_age_numeric__gte=18)
                        | Q(eligibility_max_age_numeric=0)
                    )
                )
            if age_group.lower().strip(" ") == "older adult":
                age_group_queries.append(
                    Q(eligibility_min_age_numeric__gte=0)
                    & (
                        Q(eligibility_max_age_numeric__gte=65)
                        | Q(eligibility_max_age_numeric=0)
                    )
                )
        q_age_between = age_group_queries.pop()
        for item in age_group_queries:
            q_age_between |= item

    return q_age_between


# Function to construct queryset filter for comma delimited values of routes of administration
def filter_study_roa(request):
    study_roa = request.data.get("study_roa")

    q_study_roa = Q()
    if study_roa:
        roa_list = str(study_roa).split(",")
        roa_queries = [
            Q(study_brief_desc__iregex="r(?:\\s|^)" + roa.strip(" ") + "*")
            for roa in roa_list
        ]
        q_study_roa = roa_queries.pop()
        for item in roa_queries:
            q_study_roa |= item

    return q_study_roa


# Function to construct queryset filter for pipe delimited values of study status
def filter_study_status(request):
    study_status = request.data.get("status")

    q_study_status = Q()
    if study_status:
        status_list = str(study_status).split("|")
        status_queries = [
            Q(status__iexact=status.strip(" ")) for status in status_list
        ]
        q_study_status = status_queries.pop()
        for item in status_queries:
            q_study_status |= item

    return q_study_status


# Function to construct queryset filter for comma separated values of study phases
def filter_phase(request):
    phase = request.data.get("phase")

    q_phase = Q()
    if phase:
        phase_list = str(phase).split(",")
        phase_queries = [
            Q(study_phase__icontains=phase.strip(" ")) for phase in phase_list
        ]
        q_phase = phase_queries.pop()
        for item in phase_queries:
            q_phase |= item

    return q_phase
