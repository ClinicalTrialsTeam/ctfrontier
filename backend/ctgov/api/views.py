from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from ctgov.models import BriefSummaries, BasicSearch, Studies, Facilities
from .serializers import (
    BriefSummariesSerializer,
    BasicSearchSerializer,
    CountriesSerializer,
)
from django.db.models import Q


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

        filters = {"status__contains": study_status}
        if nct_id:
            filters["nct_id__contains"] = nct_id
        if condition:
            filters["condition_name__contains"] = condition
        if other_terms:
            # filters["keywords__contains"] = other_terms
            # filters["official_title__contains"] = other_terms
            filters["brief_title__contains"] = other_terms
            # filters["study_brief_desc__contains"] = other_terms
        if country:
            filters["country_name__contains"] = country
        if intervention:
            filters["intervention_name__contains"] = intervention
        if target_moa:
            filters["keywords__contains"] = target_moa
            filters["study_brief_desc__contains"] = target_moa
        if eligibility_criteria:
            filters["eligibility_criteria__contains"] = eligibility_criteria

        if not first:
            first = 0
        if not last:
            last = 100

        search_results = (
            BasicSearch.objects.filter(**filters)
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

        # search_results = BasicSearch.objects.filter(
        #                     Q(status__contains=study_status),
        #                     Q(condition_name__contains=condition),
        #                     Q(study_brief_desc__contains=other_terms) | Q(official_title__contains=other_terms) |
        #                     Q(keywords__contains=other_terms) | Q(condition_name__contains=other_terms),
        #                     Q(country_name__contains=country),
        #                     Q(intervention_name__contains=intervention),
        #                     Q(keywords__contains=target_moa) | Q(study_brief_desc__contains=target_moa),
        #                     Q(nct_id__contains=nct_id),
        #                     Q(eligibility_criteria__contains=eligibility_criteria)
        #                     ).all().values("status","brief_title","nct_id","condition_name","intervention_name","location_name")[first:last]

        serializer = BasicSearchSerializer(search_results, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
