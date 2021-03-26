import json
from rest_framework import serializers
from ctgov.models import BriefSummaries, BasicSearchM, Studies, Facilities
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from ctgov.documents import ClinicalTrialsBasicSearch


class BriefSummariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BriefSummaries
        fields = ["nct", "description"]


class BasicSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicSearchM
        fields = [
            "status",
            "brief_title",
            "nct_id",
            "condition_name",
            "intervention_name",
            "location_name",
        ]


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ["country"]


class BasicSearchDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ClinicalTrialsBasicSearch

        fields = [
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
        ]
