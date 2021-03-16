# documents.py

from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import (
    AuthGroup,
    AuthGroupPermissions,
    AuthPermission,
    AuthUser,
    AuthUserGroups,
    AuthUserUserPermissions,
    BaselineCounts,
    BaselineMeasurements,
    BriefSummaries,
    BrowseConditions,
    BrowseInterventions,
    CalculatedValues,
    Categories,
    CentralContacts,
    Conditions,
    Countries,
    DesignGroupInterventions,
    DesignGroups,
    DesignOutcomes,
    Designs,
    DetailedDescriptions,
    DjangoAdminLog,
    DjangoContentType,
    DjangoMigrations,
    Documents,
    DropWithdrawals,
    Eligibilities,
    Facilities,
    FacilityContacts,
    FacilityInvestigators,
    IdInformation,
    InterventionOtherNames,
    Interventions,
    IpdInformationTypes,
    Keywords,
    Links,
    MeshHeadings,
    MeshTerms,
    Milestones,
    OutcomeAnalyses,
    OutcomeAnalysisGroups,
    OutcomeCounts,
    OutcomeMeasurements,
    Outcomes,
    OverallOfficials,
    ParticipantFlows,
    PendingResults,
    ProvidedDocuments,
    ReportedEventTotals,
    ReportedEvents,
    ResponsibleParties,
    ResultAgreements,
    ResultContacts,
    ResultGroups,
    Sponsors,
    Studies,
    StudyReferences,
    StudySearches,
)


@registry.register_document
class AuthGroupDocument(Document):
    class Index:

        name = "authgroup"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = AuthGroup

        fields = ["name"]


@registry.register_document
class AuthGroupPermissionsDocument(Document):
    class Index:

        name = "auth_permission"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = AuthGroupPermissions

        fields = ["group", "permission"]


@registry.register_document
class AuthPermissionDocument(Document):
    class Index:

        name = "auth_permission"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = AuthPermission

        fields = ["name", "content_type", "codename"]


@registry.register_document
class AuthUserDocument(Document):
    class Index:

        name = "auth_user"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = AuthUser

        fields = [
            "password",
            "last_login",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_staff",
            "is_active",
            "date_joined",
        ]


@registry.register_document
class AuthUserGroupsDocument(Document):
    class Index:

        name = "auth_user_groups"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = AuthUserGroups

        fields = ["user", "group"]


@registry.register_document
class AuthUserUserPermissionsDocument(Document):
    class Index:

        name = "auth_user_user_permissions"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = AuthUserUserPermissions

        fields = ["user", "permission"]


@registry.register_document
class BaselineCountsDocument(Document):
    class Index:

        name = "baseline_counts"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = BaselineCounts

        fields = [
            "nct",
            "result_group",
            "ctgov_group_code",
            "units",
            "scope",
            "count",
        ]


@registry.register_document
class BaselineMeasurementsDocument(Document):
    class Index:

        name = "baseline_measurements"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = BaselineMeasurements

        fields = [
            "nct",
            "result_group",
            "ctgove_group_code",
            "classification",
            "category",
            "title",
            "description",
            "units",
            "param_type",
            "param_value",
            "param_value_num",
            "dispersion_type",
            "dispersion_value",
            "dispersion_value_num",
            "dispersion_lower_limit",
            "dispersion_upper_limit",
            "eplanation_of_na",
        ]


@registry.register_document
class BriefSummariesDocument(Document):
    class Index:

        name = "brief_summaries"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = BriefSummaries

        fields = ["nct", "description"]


@registry.register_document
class BrowseConditionsDocument(Document):
    class Index:

        name = "browse_conditions"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = BrowseConditions

        fields = ["nct", "mesh_term", "downcase_mesh_term"]


@registry.register_document
class BrowseInterventionsDocument(Document):
    class Index:

        name = "browse_interventions"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = BrowseInterventions

        fields = ["nct", "mesh_term", "downcase_mesh_term"]


@registry.register_document
class CalculatedValuesDocument(Document):
    class Index:

        name = "calculated_values"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = CalculatedValues

        fields = [
            "nct",
            "number_of_facilities",
            "number_of_nsae_subjects",
            "number_of_sae_subjects",
            "registered_in_calendar_year",
            "nlm_download_date",
            "actual_duration",
            "were_results_reported",
            "months_to_report_results",
            "has_us_facility",
            "has_single_facility",
            "minimum_age_num",
            "maximum_age_num",
            "minimum_age_unit",
            "maximum_age_unit",
            "number_of_primary_outcomes_to_measure",
            "number_of_secondary_outcomes_to_measure",
            "number_of_other_outcomes_to_measure",
        ]


@registry.register_document
class CategoriesDocument(Document):
    class Index:

        name = "categories"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Categories

        fields = [
            "nct",
            "name",
            "created_at",
            "updated_at",
            "grouping",
            "study_search_id",
        ]


@registry.register_document
class CentralContactsDocument(Document):
    class Index:

        name = "central_contacts"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = CentralContacts

        fields = ["nct", "contact_type", "name", "phone", "email"]


@registry.register_document
class ConditionsDocument(Document):
    class Index:

        name = "conditions"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Conditions

        fields = ["nct", "name", "downcase_name"]


@registry.register_document
class CountriesDocument(Document):
    class Index:

        name = "countries"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Countries

        fields = ["nct", "name", "downcase_name"]


@registry.register_document
class DesignGroupInterventionsDocument(Document):
    class Index:

        name = "design_group_interventions"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = DesignGroupInterventions

        fields = ["nct", "design_group", "intervention"]


@registry.register_document
class DesignGroupsDocument(Document):
    class Index:

        name = "design_groups"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = DesignGroups

        fields = ["nct", "group_type", "title", "description"]


@registry.register_document
class DesignOutcomesDocument(Document):
    class Index:

        name = "design_outcomes"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = DesignOutcomes

        fields = [
            "nct",
            "outcome_type",
            "measure",
            "time_frame",
            "population",
            "description",
        ]


@registry.register_document
class DesignsDocument(Document):
    class Index:

        name = "designs"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Designs

        fields = [
            "nct",
            "allocation",
            "intervention_model",
            "observational_model",
            "primary_purpose",
            "time_perspective",
            "masking",
            "masking_description",
            "intervention_model_description",
            "subject_masked",
            "caregiver_masked",
            "investigator_masked",
            "investigator_masked",
        ]


@registry.register_document
class DetailedDescriptionsDocument(Document):
    class Index:

        name = "detailed_descriptions"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = DetailedDescriptions

        fields = [
            "nct",
            "description",
        ]


@registry.register_document
class DjangoAdminLogDocument(Document):
    class Index:

        name = "django_admin_log"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = DjangoAdminLog

        fields = [
            "action_time",
            "object_id",
            "object_repr",
            "action_flag",
            "change_message",
            "content_type",
            "user",
        ]


@registry.register_document
class DjangoContentTypeDocument(Document):
    class Index:

        name = "django_content_type"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = DjangoContentType

        fields = [
            "app_label",
            "model",
        ]


@registry.register_document
class DjangoMigrationsDocument(Document):
    class Index:

        name = "django_migrations"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = DjangoMigrations

        fields = ["app", "name", "applied"]


@registry.register_document
class DocumentsDocument(Document):
    class Index:

        name = "documents"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Documents

        fields = ["nct", "document_id", "document_type", "url", "comment"]


@registry.register_document
class DropWithdrawalsDocument(Document):
    class Index:

        name = "drop_withdrawals"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = DropWithdrawals

        fields = [
            "nct",
            "result_group",
            "ctgov_group_code",
            "period",
            "reason",
            "count",
        ]


@registry.register_document
class EligibilitiesDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = "eligibilities"
        # See Elasticsearch Indices API reference for available settings
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Eligibilities  # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            "sampling_method",
            "gender",
            "minimum_age",
            "healthy_volunteers",
            "population",
            "criteria",
            "gender_description",
            "gender_based",
        ]

        # Ignore auto updating of Elasticsearch when a model is saved
        # or deleted:
        # ignore_signals = True

        # Don't perform an index refresh after every update (overrides global setting):
        # auto_refresh = False

        # Paginate the django queryset used to populate the index with the specified size
        # (by default it uses the database driver's default setting)
        # queryset_pagination = 5000


@registry.register_document
class FacilitiesDocument(Document):
    class Index:

        name = "facilities"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Facilities

        fields = ["status", "name", "city", "state", "zip", "country"]


@registry.register_document
class FacilityContactsDocument(Document):
    class Index:

        name = "facility_contacts"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = FacilityContacts

        fields = [
            "nct",
            "facility",
            "contact_type",
            "name",
            "email",
            "phone",
        ]


@registry.register_document
class FacilityInvestigatorsDocument(Document):
    class Index:

        name = "facility_investigators"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = FacilityInvestigators

        fields = [
            "nct",
            "facility",
            "role",
            "name",
        ]


@registry.register_document
class IdInformationDocument(Document):
    class Index:

        name = "id_information"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = IdInformation

        fields = [
            "nct",
            "id_type",
            "id_value",
        ]


@registry.register_document
class InterventionOtherNamesDocument(Document):
    class Index:

        name = "intervention_other_names"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = InterventionOtherNames

        fields = [
            "nct",
            "intervention",
            "name",
        ]


@registry.register_document
class IpdInformationTypesDocument(Document):
    class Index:

        name = "ipd_information_types"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = IpdInformationTypes

        fields = [
            "nct",
            "name",
        ]


@registry.register_document
class KeywordsDocument(Document):
    class Index:

        name = "keywords"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Keywords

        fields = ["nct", "name", "downcase_name"]


@registry.register_document
class LinksDocument(Document):
    class Index:

        name = "links"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Links

        fields = ["nct", "url", "description"]


@registry.register_document
class MeshHeadingsDocument(Document):
    class Index:

        name = "mesh_headings"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = MeshHeadings

        fields = ["qualifier", "heading", "subcategory"]


@registry.register_document
class MeshTermsDocument(Document):
    class Index:

        name = "mesh_terms"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = MeshTerms

        fields = [
            "qualifier",
            "tree_number",
            "description",
            "mesh_term",
            "downcase_mesh_term",
        ]


@registry.register_document
class MilestonesDocument(Document):
    class Index:

        name = "milestones"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Milestones

        fields = [
            "nct",
            "result_group",
            "ctgov_group_code",
            "title",
            "period",
            "description",
            "count",
        ]


@registry.register_document
class OutcomeAnalysesDocument(Document):
    class Index:

        name = "outcome_analyses"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = OutcomeAnalyses

        fields = [
            "nct",
            "outcome",
            "non_inferiority_type",
            "non_inferiority_description",
            "param_type",
            "param_value",
            "dispersion_type",
            "dispersion_value",
            "p_value_modifier",
            "p_value",
            "ci_n_sides",
            "ci_percent",
            "ci_lower_limit",
            "ci_upper_limit",
            "ci_upper_limit_na_comment",
            "p_value_description",
            "method",
            "method_description",
            "estimate_description",
            "groups_description",
            "other_analysis_description",
        ]


@registry.register_document
class OutcomeAnalysisGroupsDocument(Document):
    class Index:

        name = "outcome_analysis_groups"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = OutcomeAnalysisGroups

        fields = [
            "nct",
            "outcome_analysis",
            "result_group",
            "ctgov_group_code",
        ]


@registry.register_document
class OutcomeCountsDocument(Document):
    class Index:

        name = "outcome_counts"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = OutcomeCounts

        fields = [
            "nct",
            "outcome",
            "result_group",
            "ctgov_group_code",
            "scope",
            "units",
            "count",
        ]


@registry.register_document
class OutcomeMeasurementsDocument(Document):
    class Index:

        name = "outcome_measurements"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = OutcomeMeasurements

        fields = [
            "nct",
            "outcome",
            "result_group",
            "ctgov_group_code",
            "classification",
            "category",
            "title",
            "description",
            "outcome",
            "units",
            "param_type",
            "param_value",
            "param_value_num",
            "dispersion_type",
            "dispersion_value",
            "dispersion_value_num",
            "dispersion_lower_limit",
            "dispersion_upper_limit",
            "explanation_of_na",
        ]


@registry.register_document
class OutcomesDocument(Document):
    class Index:

        name = "outcomes"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Outcomes

        fields = [
            "nct",
            "outcome_type",
            "title",
            "description",
            "time_frame",
            "population",
            "anticipated_posting_date",
            "anticipated_posting_month_year",
            "units",
            "units_analyzed",
            "dispersion_type",
            "param_type",
        ]


@registry.register_document
class OverallOfficialsDocument(Document):
    class Index:

        name = "overall_officials"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = OverallOfficials

        fields = [
            "nct",
            "role",
            "name",
            "affiliation",
        ]


@registry.register_document
class ParticipantFlowsDocument(Document):
    class Index:

        name = "participant_flows"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ParticipantFlows

        fields = [
            "nct",
            "recruitment_details",
            "pre_assignment_details",
        ]


@registry.register_document
class PendingResultsDocument(Document):
    class Index:

        name = "pending_results"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = PendingResults

        fields = ["nct", "event", "event_date_description", "event_date"]


@registry.register_document
class ProvidedDocumentsDocument(Document):
    class Index:

        name = "provided_documents"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ProvidedDocuments

        fields = [
            "nct",
            "document_type",
            "has_protocol",
            "has_icf",
            "has_sap",
            "document_date",
            "url",
        ]


@registry.register_document
class ReportedEventTotalsDocument(Document):
    class Index:

        name = "reported_event_totals"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ReportedEventTotals

        fields = [
            "nct",
            "ctgov_group_code",
            "event_type",
            "classification",
            "subjects_affected",
            "subjects_at_risk",
            "created_at",
            "updated_at",
        ]


@registry.register_document
class ReportedEventsDocument(Document):
    class Index:

        name = "reported_events"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ReportedEvents

        fields = [
            "nct",
            "result_group",
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
class ResponsiblePartiesDocument(Document):
    class Index:

        name = "responsible_parties"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ResponsibleParties

        fields = [
            "nct",
            "responsible_party_type",
            "name",
            "title",
            "organization",
            "affiliation",
        ]


@registry.register_document
class ResultAgreementsDocument(Document):
    class Index:

        name = "result_agreements"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ResultAgreements

        fields = [
            "pi_employee",
            "agreement",
            "restriction_type",
            "other_details",
            "restrictive_agreement",
        ]


@registry.register_document
class ResultContactsDocument(Document):
    class Index:

        name = "result_contacts"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ResultContacts

        fields = [
            "nct",
            "organization",
            "name",
            "phone",
            "email",
        ]


@registry.register_document
class ResultGroupsDocument(Document):
    class Index:

        name = "result_groups"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ResultGroups

        fields = [
            "nct",
            "ctgov_group_code",
            "result_type",
            "title",
            "description",
        ]


@registry.register_document
class SponsorsDocument(Document):
    class Index:

        name = "sponsors"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Sponsors

        fields = [
            "nct",
            "agency_class",
            "lead_or_collaborator",
            "name",
        ]


@registry.register_document
class StudiesDocument(Document):
    class Index:

        name = "studies"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Studies

        fields = [
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


@registry.register_document
class StudyReferencesDocument(Document):
    class Index:

        name = "study_references"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = StudyReferences

        fields = [
            "nct",
            "pmid",
            "reference_type",
            "citation",
        ]


@registry.register_document
class StudySearchesDocument(Document):
    class Index:

        name = "study_searches"

        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = StudySearches

        fields = [
            "save_tsv",
            "query",
            "grouping",
            "name",
            "beta_api",
            "created_at",
            "updated_at",
        ]
