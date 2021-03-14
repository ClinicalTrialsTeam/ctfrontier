from rest_framework import serializers
from ctgov.models import BriefSummaries, BasicSearch, Studies, Facilities


class BriefSummariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BriefSummaries
        fields = ["nct", "description"]


class BasicSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicSearch
        fields = [
            "status",
            "brief_title",
            "nct_id",
            "condition_name",
            "intervention_name",
            "location_name",
        ]

        # model = Studies
        # fields = ["overall_status", "brief_title", "nct_id"]


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ["country"]
