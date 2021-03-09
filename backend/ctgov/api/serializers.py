from rest_framework import serializers
from ctgov.models import BriefSummaries


class BriefSummariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BriefSummaries
        fields = ["nct", "description"]
