from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ctgov.models import BriefSummaries, SearchStudies, Facilities
from .serializers import (
    BriefSummariesSerializer,
    SearchStudiesSerializer,
    CountriesSerializer,
    SearchStudiesDocumentSerializer,
)
from datetime import datetime
from django.db.models import Q


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
        countries = (
            Facilities.objects.all()
            .distinct()
            .order_by("country")
            .values("country")
        )
        serializer = CountriesSerializer(countries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Define post action for the API call
# Validate each parameter and construct AND, OR, Contains operators
# Return results along with metadata
class SearchStudiesApiView(APIView):
    def post(self, request, *args, **kwargs):
        study_status = request.data.get("status")
        nct_id = request.data.get("nct_id")
        first = request.data.get("first")
        last = request.data.get("last")
        condition = request.data.get("condition")
        other_terms = request.data.get("other_terms")
        country = request.data.get("country")
        intervention = request.data.get("intervention")
        target_moa = request.data.get("target")
        eligibility_criteria = request.data.get("eligibility_criteria")
        metadata_required = request.data.get("metadata_required")

        # new fields based on client demo
        modality = request.data.get("modality")
        sponsor = request.data.get("sponsor")
        phase = request.data.get("phase")
        start_date_from = request.data.get("start_date_from")
        start_date_to = request.data.get("start_date_to")
        primary_completion_date_from = request.data.get(
            "primary_completion_date_from"
        )
        primary_completion_date_to = request.data.get(
            "primary_completion_date_to"
        )
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
        last_update_posted_date_to = request.data.get(
            "last_update_posted_date_to"
        )

        # Advanced search parameters
        study_results = request.data.get("study_results")
        study_type = request.data.get("study_type")
        eligibility_age = request.data.get("eligibility_age")
        eligibility_min_age = request.data.get("eligibility_min_age")
        eligibility_max_age = request.data.get("eligibility_max_age")
        eligibility_gender = request.data.get("eligibility_gender")
        eligibility_ethnicity = request.data.get("eligibility_ethnicity")
        eligibility_condition = request.data.get("eligibility_condition")
        eligibility_healthy_volunteer = request.data.get(
            "eligibility_healthy_volunteer"
        )
        study_title_acronym = request.data.get("study_title_acronym")
        study_outcome_measure = request.data.get("study_outcome_measure")
        study_collaborator = request.data.get("study_collaborator")
        study_ids = request.data.get("study_ids")
        study_location_terms = request.data.get("study_location_terms")
        study_funder_type = request.data.get("study_funder_type")
        study_document_type = request.data.get("study_document_type")
        study_results_submitted = request.data.get("study_results_submitted")
        study_roa = request.data.get("study_roa")

        if not study_status:
            study_status = ""

        filters = {"status__icontains": study_status}
        if nct_id:
            filters["nct_id__icontains"] = nct_id
        if condition:
            filters["condition_name__icontains"] = condition
        if other_terms:
            filters["brief_title__icontains"] = other_terms
        if country:
            filters["country_name__icontains"] = country
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
        if phase:
            filters["study_phase__icontains"] = phase
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

        # Advanced Search Filters
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
        if study_roa:
            filters["study_brief_desc__icontains"] = study_roa

        # Build OR conditions for advanced search parameters
        q_title_acronym = Q()
        if study_title_acronym:
            q_title_acronym = Q(
                official_title__icontains=study_title_acronym
            ) | Q(acronym__icontains=study_title_acronym)

        q_outcome_measure = Q()
        if study_outcome_measure:
            q_outcome_measure = Q(
                primary_outcome_measures__icontains=study_outcome_measure
            ) | Q(secondary_outcome_measures__icontains=study_outcome_measure)

        q_eligibility_age = Q()
        if valid_number(eligibility_age):
            q_eligibility_age = Q(
                eligibility_min_age_numeric=convert_to_number(eligibility_age)
            ) | Q(
                eligibility_max_age_numeric=convert_to_number(eligibility_age)
            )

        q_age_between = Q()
        if valid_number(eligibility_min_age) and valid_number(
            eligibility_max_age
        ):
            q_age_between = Q(
                eligibility_min_age_numeric__gte=convert_to_number(
                    eligibility_min_age
                )
            ) & Q(
                eligibility_max_age_numeric__lte=convert_to_number(
                    eligibility_max_age
                )
            )
        elif valid_number(eligibility_min_age):
            q_age_between = Q(
                eligibility_min_age_numeric__gte=convert_to_number(
                    eligibility_min_age
                )
            )
        elif valid_number(eligibility_max_age):
            q_age_between = Q(
                eligibility_max_age_numeric__lte=convert_to_number(
                    eligibility_max_age
                )
            )

        if not first:
            first = 0
        if not last:
            last = 100

        if metadata_required:
            search_results_all = (
                SearchStudies.objects.filter(**filters)
                .filter(q_title_acronym)
                .filter(q_outcome_measure)
                .filter(q_eligibility_age)
                .filter(q_age_between)
                .all()
            )

            search_results = search_results_all.all().values(
                "status",
                "brief_title",
                "nct_id",
                "condition_name",
                "intervention_name",
                "location_name",
            )[first:last]

            results_count = search_results_all.count()

        else:
            search_results = (
                SearchStudies.objects.filter(**filters)
                .filter(q_title_acronym)
                .filter(q_outcome_measure)
                .filter(q_eligibility_age)
                .filter(q_age_between)
                .all()
                .values(
                    "status",
                    "brief_title",
                    "nct_id",
                    "condition_name",
                    "intervention_name",
                    "location_name",
                )[first:last]
            )

            results_count = "NA"

        serializer = SearchStudiesSerializer(search_results, many=True)
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
