from rest_framework import serializers
from ctgov.models import (
    BriefSummaries,
    SearchStudies,
    Facilities,
    BrowseConditions,
    Countries_New,
)
from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from ctgov.documents import ClinicalTrialsSearchStudies


# Serializer to return Brief Summaries dataset
class BriefSummariesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BriefSummaries
        fields = ["nct", "description"]


# Serializezr to return Search Studies Results dataset
class SearchStudiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchStudies
        fields = [
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
        ]


# Serializer to return Study Countries list
class CountriesNewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries_New
        fields = ["name"]


# Serializer to return Study Countries list
class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ["country"]


# Serializer to return Study States list
class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ["state"]


# Serializer to return Study Cities list
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = ["city"]


# Serializer to return conditions list
class ConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrowseConditions
        fields = ["mesh_term"]


# Serializer to return Trial Timelines dataset
class TrialTimelinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchStudies
        fields = [
            "nct_id",
            "study_start_date",
            "primary_completion_date",
            "study_phase",
        ]


# Serializer to return single Study dataset
class StudyDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchStudies
        fields = [
            "nct_id",
            "brief_title",
            "official_title",
            "study_brief_desc",
            "study_detailed_desc",
            "status",
            "study_phase",
            "study_start_date",
            "primary_completion_date",
            "study_first_posted_date",
            "results_first_posted_date",
            "last_update_posted_date",
            "results_submitted_qc_not_done",
            "results_submitted_qc_done",
            "study_type",
            "condition_name",
            "intervention_name",
            "eligibility_criteria",
            "eligibility_gender",
            "eligibility_min_age",
            "eligibility_max_age",
            "sponsor_name",
            "funder_type",
            "primary_outcome_measures",
            "secondary_outcome_measures",
            "study_ids",
            "document_types",
            "is_unapproved_device",
            "acronym",
            "healthy_volunteers",
            "location_name",
            "country_name",
            "city_name",
            "state_name",
        ]


# Serialzer for Elastic Search document
class SearchStudiesDocumentSerializer(DocumentSerializer):
    class Meta:
        document = ClinicalTrialsSearchStudies

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
