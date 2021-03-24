# documents.py

from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from ctgov.models import Documents
from .models import Sponsors, ReportedEvents, Studies


@registry.register_document
class ReportedEventsDocuments(Document):
    class Index:
        name = "reported_events"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ReportedEvents

        fields = [
            "ctgov_group_code",
            "time_frame",
            "event_type",
            "default_vocab",
            "default_assessment",
            "subjects_affected",
            "subjects_at_risk",
            "description",
            "event_count",
            "organ_system",
            "adverse_event_term",
            "frequency_threshold",
            "vocab",
            "assessment",
        ]


@registry.register_document
class SearchDocuments(Document):
    class Index:
        name = "study_comments"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Documents

        fields = [
            "document_id",
            "document_type",
            "url",
            "comment",
        ]


@registry.register_document
class SponsorsDocuments(Document):
    class Index:
        name = "sponsors"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Sponsors

        fields = [
            "agency_class",
            "lead_or_collaborator",
            "name",
        ]


@registry.register_document
class StudiesDocuments(Document):
    class Index:
        name = "studies"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Studies

        fields = [
            "id",
            "nct_id",
            "nlm_download_date_description",
            "study_first_submitted_date",
            "results_first_submitted_date",
            "disposition_first_submitted_date",
            "last_update_submitted_date",
            "study_first_submitted_qc_date",
            "study_first_posted_date",
            "study_first_posted_date_type",
            "results_first_submitted_qc_date",
            "results_first_posted_date",
            "results_first_posted_date_type",
            "disposition_first_submitted_qc_date",
            "disposition_first_posted_date",
            "disposition_first_posted_date_type",
            "last_update_submitted_qc_date",
            "last_update_posted_date",
            "last_update_posted_date_type",
            "start_month_year",
            "start_date_type",
            "start_date",
            "verification_month_year",
            "verification_date",
            "completion_month_year",
            "completion_date_type",
            "completion_date",
            "primary_completion_month_year",
            "primary_completion_date_type",
            "primary_completion_date",
            "target_duration",
            "study_type",
            "acronym",
            "baseline_population",
            "brief_title",
            "official_title",
            "overall_status",
            "last_known_status",
            "phase",
            "enrollment",
            "enrollment_type",
            "source",
            "limitations_and_caveats",
            "number_of_arms",
            "number_of_groups",
            "why_stopped",
            "has_expanded_access",
            "expanded_access_type_individual",
            "expanded_access_type_intermediate",
            "expanded_access_type_treatment",
            "has_dmc",
            "is_fda_regulated_drug",
            "is_fda_regulated_device",
            "is_unapproved_device",
            "is_ppsd",
            "is_us_export",
            "biospec_retention",
            "biospec_description",
            "ipd_time_frame",
            "ipd_access_criteria",
            "ipd_url",
            "plan_to_share_ipd",
            "plan_to_share_ipd_description",
            "created_at",
            "updated_at",
        ]
