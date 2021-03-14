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
