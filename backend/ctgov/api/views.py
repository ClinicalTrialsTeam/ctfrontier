from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ctgov.models import BriefSummaries, BasicSearchM, Facilities
from .serializers import (
    BriefSummariesSerializer,
    BasicSearchSerializer,
    CountriesSerializer,
)
from datetime import datetime


class BriefSummariesListApiView(APIView):
    def get(self, request, *args, **kwargs):
        summaries = BriefSummaries.objects.all()[:10]
        serializer = BriefSummariesSerializer(summaries, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


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


class BasicSearchApiView(APIView):
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

        if not study_status:
            study_status = "Completed"

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

        if not first:
            first = 0
        if not last:
            last = 100

        search_results = (
            BasicSearchM.objects.filter(**filters)
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

        serializer = BasicSearchSerializer(search_results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


def convert_to_date(datestr):
    date = datetime.strptime(datestr, "%Y-%m-%d")
    return date


def valid_date(datestr):
    status = True
    try:
        datetime.strptime(datestr, "%Y-%m-%d")
    except ValueError:
        status = False

    return status
