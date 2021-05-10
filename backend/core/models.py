# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = "auth_group"


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey("AuthPermission", models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_group_permissions"
        unique_together = (("group", "permission"),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey("DjangoContentType", models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "auth_permission"
        unique_together = (("content_type", "codename"),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "auth_user"


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_groups"
        unique_together = (("user", "group"),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "auth_user_user_permissions"
        unique_together = (("user", "permission"),)


class BaselineCounts(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    result_group = models.ForeignKey(
        "ResultGroups", models.DO_NOTHING, blank=True, null=True
    )
    ctgov_group_code = models.CharField(max_length=-1, blank=True, null=True)
    units = models.CharField(max_length=-1, blank=True, null=True)
    scope = models.CharField(max_length=-1, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "baseline_counts"


class BaselineMeasurements(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    result_group = models.ForeignKey(
        "ResultGroups", models.DO_NOTHING, blank=True, null=True
    )
    ctgov_group_code = models.CharField(max_length=-1, blank=True, null=True)
    classification = models.CharField(max_length=-1, blank=True, null=True)
    category = models.CharField(max_length=-1, blank=True, null=True)
    title = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    units = models.CharField(max_length=-1, blank=True, null=True)
    param_type = models.CharField(max_length=-1, blank=True, null=True)
    param_value = models.CharField(max_length=-1, blank=True, null=True)
    param_value_num = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    dispersion_type = models.CharField(max_length=-1, blank=True, null=True)
    dispersion_value = models.CharField(max_length=-1, blank=True, null=True)
    dispersion_value_num = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    dispersion_lower_limit = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    dispersion_upper_limit = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    explanation_of_na = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "baseline_measurements"


class BriefSummaries(models.Model):
    nct = models.OneToOneField(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "brief_summaries"


class BrowseConditions(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    mesh_term = models.CharField(max_length=-1, blank=True, null=True)
    downcase_mesh_term = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "browse_conditions"


class BrowseInterventions(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    mesh_term = models.CharField(max_length=-1, blank=True, null=True)
    downcase_mesh_term = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "browse_interventions"


class CalculatedValues(models.Model):
    nct = models.OneToOneField(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    number_of_facilities = models.IntegerField(blank=True, null=True)
    number_of_nsae_subjects = models.IntegerField(blank=True, null=True)
    number_of_sae_subjects = models.IntegerField(blank=True, null=True)
    registered_in_calendar_year = models.IntegerField(blank=True, null=True)
    nlm_download_date = models.DateField(blank=True, null=True)
    actual_duration = models.IntegerField(blank=True, null=True)
    were_results_reported = models.BooleanField(blank=True, null=True)
    months_to_report_results = models.IntegerField(blank=True, null=True)
    has_us_facility = models.BooleanField(blank=True, null=True)
    has_single_facility = models.BooleanField(blank=True, null=True)
    minimum_age_num = models.IntegerField(blank=True, null=True)
    maximum_age_num = models.IntegerField(blank=True, null=True)
    minimum_age_unit = models.CharField(max_length=-1, blank=True, null=True)
    maximum_age_unit = models.CharField(max_length=-1, blank=True, null=True)
    number_of_primary_outcomes_to_measure = models.IntegerField(
        blank=True, null=True
    )
    number_of_secondary_outcomes_to_measure = models.IntegerField(
        blank=True, null=True
    )
    number_of_other_outcomes_to_measure = models.IntegerField(
        blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "calculated_values"


class Categories(models.Model):
    nct = models.ForeignKey("Studies", models.DO_NOTHING)
    name = models.CharField(max_length=-1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    grouping = models.CharField(max_length=-1)
    study_search_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "categories"


class CentralContacts(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    contact_type = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "central_contacts"


class Conditions(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    name = models.CharField(max_length=-1, blank=True, null=True)
    downcase_name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "conditions"


class Countries(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    name = models.CharField(max_length=-1, blank=True, null=True)
    removed = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "countries"


class DesignGroupInterventions(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    design_group = models.ForeignKey(
        "DesignGroups", models.DO_NOTHING, blank=True, null=True
    )
    intervention = models.ForeignKey(
        "Interventions", models.DO_NOTHING, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "design_group_interventions"


class DesignGroups(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    group_type = models.CharField(max_length=-1, blank=True, null=True)
    title = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "design_groups"


class DesignOutcomes(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    outcome_type = models.CharField(max_length=-1, blank=True, null=True)
    measure = models.TextField(blank=True, null=True)
    time_frame = models.TextField(blank=True, null=True)
    population = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "design_outcomes"


class Designs(models.Model):
    nct = models.OneToOneField(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    allocation = models.CharField(max_length=-1, blank=True, null=True)
    intervention_model = models.CharField(max_length=-1, blank=True, null=True)
    observational_model = models.CharField(
        max_length=-1, blank=True, null=True
    )
    primary_purpose = models.CharField(max_length=-1, blank=True, null=True)
    time_perspective = models.CharField(max_length=-1, blank=True, null=True)
    masking = models.CharField(max_length=-1, blank=True, null=True)
    masking_description = models.TextField(blank=True, null=True)
    intervention_model_description = models.TextField(blank=True, null=True)
    subject_masked = models.BooleanField(blank=True, null=True)
    caregiver_masked = models.BooleanField(blank=True, null=True)
    investigator_masked = models.BooleanField(blank=True, null=True)
    outcomes_assessor_masked = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "designs"


class DetailedDescriptions(models.Model):
    nct = models.OneToOneField(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "detailed_descriptions"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(
        "DjangoContentType", models.DO_NOTHING, blank=True, null=True
    )
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "django_admin_log"


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = "django_content_type"
        unique_together = (("app_label", "model"),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_migrations"


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "django_session"


class Documents(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    document_id = models.CharField(max_length=-1, blank=True, null=True)
    document_type = models.CharField(max_length=-1, blank=True, null=True)
    url = models.CharField(max_length=-1, blank=True, null=True)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "documents"


class DropWithdrawals(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    result_group = models.ForeignKey(
        "ResultGroups", models.DO_NOTHING, blank=True, null=True
    )
    ctgov_group_code = models.CharField(max_length=-1, blank=True, null=True)
    period = models.CharField(max_length=-1, blank=True, null=True)
    reason = models.CharField(max_length=-1, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "drop_withdrawals"


class Eligibilities(models.Model):
    nct = models.OneToOneField(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    sampling_method = models.CharField(max_length=-1, blank=True, null=True)
    gender = models.CharField(max_length=-1, blank=True, null=True)
    minimum_age = models.CharField(max_length=-1, blank=True, null=True)
    maximum_age = models.CharField(max_length=-1, blank=True, null=True)
    healthy_volunteers = models.CharField(max_length=-1, blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    criteria = models.TextField(blank=True, null=True)
    gender_description = models.TextField(blank=True, null=True)
    gender_based = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "eligibilities"


class Facilities(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    status = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    city = models.CharField(max_length=-1, blank=True, null=True)
    state = models.CharField(max_length=-1, blank=True, null=True)
    zip = models.CharField(max_length=-1, blank=True, null=True)
    country = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "facilities"


class FacilityContacts(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    facility = models.ForeignKey(
        Facilities, models.DO_NOTHING, blank=True, null=True
    )
    contact_type = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "facility_contacts"


class FacilityInvestigators(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    facility = models.ForeignKey(
        Facilities, models.DO_NOTHING, blank=True, null=True
    )
    role = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "facility_investigators"


class IdInformation(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    id_type = models.CharField(max_length=-1, blank=True, null=True)
    id_value = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "id_information"


class InterventionOtherNames(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    intervention = models.ForeignKey(
        "Interventions", models.DO_NOTHING, blank=True, null=True
    )
    name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "intervention_other_names"


class Interventions(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    intervention_type = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "interventions"


class IpdInformationTypes(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ipd_information_types"


class Keywords(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    name = models.CharField(max_length=-1, blank=True, null=True)
    downcase_name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "keywords"


class Links(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    url = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "links"


class MeshHeadings(models.Model):
    qualifier = models.CharField(max_length=-1, blank=True, null=True)
    heading = models.CharField(max_length=-1, blank=True, null=True)
    subcategory = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mesh_headings"


class MeshTerms(models.Model):
    qualifier = models.CharField(max_length=-1, blank=True, null=True)
    tree_number = models.CharField(max_length=-1, blank=True, null=True)
    description = models.CharField(max_length=-1, blank=True, null=True)
    mesh_term = models.CharField(max_length=-1, blank=True, null=True)
    downcase_mesh_term = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mesh_terms"


class Milestones(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    result_group = models.ForeignKey(
        "ResultGroups", models.DO_NOTHING, blank=True, null=True
    )
    ctgov_group_code = models.CharField(max_length=-1, blank=True, null=True)
    title = models.CharField(max_length=-1, blank=True, null=True)
    period = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "milestones"


class OutcomeAnalyses(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    outcome = models.ForeignKey(
        "Outcomes", models.DO_NOTHING, blank=True, null=True
    )
    non_inferiority_type = models.CharField(
        max_length=-1, blank=True, null=True
    )
    non_inferiority_description = models.TextField(blank=True, null=True)
    param_type = models.CharField(max_length=-1, blank=True, null=True)
    param_value = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    dispersion_type = models.CharField(max_length=-1, blank=True, null=True)
    dispersion_value = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    p_value_modifier = models.CharField(max_length=-1, blank=True, null=True)
    p_value = models.FloatField(blank=True, null=True)
    ci_n_sides = models.CharField(max_length=-1, blank=True, null=True)
    ci_percent = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    ci_lower_limit = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    ci_upper_limit = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    ci_upper_limit_na_comment = models.CharField(
        max_length=-1, blank=True, null=True
    )
    p_value_description = models.CharField(
        max_length=-1, blank=True, null=True
    )
    method = models.CharField(max_length=-1, blank=True, null=True)
    method_description = models.TextField(blank=True, null=True)
    estimate_description = models.TextField(blank=True, null=True)
    groups_description = models.TextField(blank=True, null=True)
    other_analysis_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "outcome_analyses"


class OutcomeAnalysisGroups(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    outcome_analysis = models.ForeignKey(
        OutcomeAnalyses, models.DO_NOTHING, blank=True, null=True
    )
    result_group = models.ForeignKey(
        "ResultGroups", models.DO_NOTHING, blank=True, null=True
    )
    ctgov_group_code = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "outcome_analysis_groups"


class OutcomeCounts(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    outcome = models.ForeignKey(
        "Outcomes", models.DO_NOTHING, blank=True, null=True
    )
    result_group = models.ForeignKey(
        "ResultGroups", models.DO_NOTHING, blank=True, null=True
    )
    ctgov_group_code = models.CharField(max_length=-1, blank=True, null=True)
    scope = models.CharField(max_length=-1, blank=True, null=True)
    units = models.CharField(max_length=-1, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "outcome_counts"


class OutcomeMeasurements(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    outcome = models.ForeignKey(
        "Outcomes", models.DO_NOTHING, blank=True, null=True
    )
    result_group = models.ForeignKey(
        "ResultGroups", models.DO_NOTHING, blank=True, null=True
    )
    ctgov_group_code = models.CharField(max_length=-1, blank=True, null=True)
    classification = models.CharField(max_length=-1, blank=True, null=True)
    category = models.CharField(max_length=-1, blank=True, null=True)
    title = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    units = models.CharField(max_length=-1, blank=True, null=True)
    param_type = models.CharField(max_length=-1, blank=True, null=True)
    param_value = models.CharField(max_length=-1, blank=True, null=True)
    param_value_num = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    dispersion_type = models.CharField(max_length=-1, blank=True, null=True)
    dispersion_value = models.CharField(max_length=-1, blank=True, null=True)
    dispersion_value_num = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    dispersion_lower_limit = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    dispersion_upper_limit = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    explanation_of_na = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "outcome_measurements"


class Outcomes(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    outcome_type = models.CharField(max_length=-1, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    time_frame = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    anticipated_posting_date = models.DateField(blank=True, null=True)
    anticipated_posting_month_year = models.CharField(
        max_length=-1, blank=True, null=True
    )
    units = models.CharField(max_length=-1, blank=True, null=True)
    units_analyzed = models.CharField(max_length=-1, blank=True, null=True)
    dispersion_type = models.CharField(max_length=-1, blank=True, null=True)
    param_type = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "outcomes"


class OverallOfficials(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    role = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    affiliation = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "overall_officials"


class ParticipantFlows(models.Model):
    nct = models.OneToOneField(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    recruitment_details = models.TextField(blank=True, null=True)
    pre_assignment_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "participant_flows"


class PendingResults(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    event = models.CharField(max_length=-1, blank=True, null=True)
    event_date_description = models.CharField(
        max_length=-1, blank=True, null=True
    )
    event_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "pending_results"


class ProvidedDocuments(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    document_type = models.CharField(max_length=-1, blank=True, null=True)
    has_protocol = models.BooleanField(blank=True, null=True)
    has_icf = models.BooleanField(blank=True, null=True)
    has_sap = models.BooleanField(blank=True, null=True)
    document_date = models.DateField(blank=True, null=True)
    url = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "provided_documents"


class ReportedEventTotals(models.Model):
    nct = models.ForeignKey("Studies", models.DO_NOTHING)
    ctgov_group_code = models.CharField(max_length=-1)
    event_type = models.CharField(max_length=-1, blank=True, null=True)
    classification = models.CharField(max_length=-1)
    subjects_affected = models.IntegerField(blank=True, null=True)
    subjects_at_risk = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "reported_event_totals"


class ReportedEvents(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    result_group = models.ForeignKey(
        "ResultGroups", models.DO_NOTHING, blank=True, null=True
    )
    ctgov_group_code = models.CharField(max_length=-1, blank=True, null=True)
    time_frame = models.TextField(blank=True, null=True)
    event_type = models.CharField(max_length=-1, blank=True, null=True)
    default_vocab = models.CharField(max_length=-1, blank=True, null=True)
    default_assessment = models.CharField(max_length=-1, blank=True, null=True)
    subjects_affected = models.IntegerField(blank=True, null=True)
    subjects_at_risk = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    event_count = models.IntegerField(blank=True, null=True)
    organ_system = models.CharField(max_length=-1, blank=True, null=True)
    adverse_event_term = models.CharField(max_length=-1, blank=True, null=True)
    frequency_threshold = models.IntegerField(blank=True, null=True)
    vocab = models.CharField(max_length=-1, blank=True, null=True)
    assessment = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "reported_events"


class ResponsibleParties(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    responsible_party_type = models.CharField(
        max_length=-1, blank=True, null=True
    )
    name = models.CharField(max_length=-1, blank=True, null=True)
    title = models.CharField(max_length=-1, blank=True, null=True)
    organization = models.CharField(max_length=-1, blank=True, null=True)
    affiliation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "responsible_parties"


class ResultAgreements(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    pi_employee = models.CharField(max_length=-1, blank=True, null=True)
    agreement = models.TextField(blank=True, null=True)
    restriction_type = models.CharField(max_length=-1, blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)
    restrictive_agreement = models.CharField(
        max_length=-1, blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "result_agreements"


class ResultContacts(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    organization = models.CharField(max_length=-1, blank=True, null=True)
    name = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "result_contacts"


class ResultGroups(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    ctgov_group_code = models.CharField(max_length=-1, blank=True, null=True)
    result_type = models.CharField(max_length=-1, blank=True, null=True)
    title = models.CharField(max_length=-1, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "result_groups"


class Sponsors(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    agency_class = models.CharField(max_length=-1, blank=True, null=True)
    lead_or_collaborator = models.CharField(
        max_length=-1, blank=True, null=True
    )
    name = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sponsors"


class Studies(models.Model):
    nct_id = models.CharField(
        unique=True, max_length=-1, blank=True, null=True
    )
    nlm_download_date_description = models.CharField(
        max_length=-1, blank=True, null=True
    )
    study_first_submitted_date = models.DateField(blank=True, null=True)
    results_first_submitted_date = models.DateField(blank=True, null=True)
    disposition_first_submitted_date = models.DateField(blank=True, null=True)
    last_update_submitted_date = models.DateField(blank=True, null=True)
    study_first_submitted_qc_date = models.DateField(blank=True, null=True)
    study_first_posted_date = models.DateField(blank=True, null=True)
    study_first_posted_date_type = models.CharField(
        max_length=-1, blank=True, null=True
    )
    results_first_submitted_qc_date = models.DateField(blank=True, null=True)
    results_first_posted_date = models.DateField(blank=True, null=True)
    results_first_posted_date_type = models.CharField(
        max_length=-1, blank=True, null=True
    )
    disposition_first_submitted_qc_date = models.DateField(
        blank=True, null=True
    )
    disposition_first_posted_date = models.DateField(blank=True, null=True)
    disposition_first_posted_date_type = models.CharField(
        max_length=-1, blank=True, null=True
    )
    last_update_submitted_qc_date = models.DateField(blank=True, null=True)
    last_update_posted_date = models.DateField(blank=True, null=True)
    last_update_posted_date_type = models.CharField(
        max_length=-1, blank=True, null=True
    )
    start_month_year = models.CharField(max_length=-1, blank=True, null=True)
    start_date_type = models.CharField(max_length=-1, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    verification_month_year = models.CharField(
        max_length=-1, blank=True, null=True
    )
    verification_date = models.DateField(blank=True, null=True)
    completion_month_year = models.CharField(
        max_length=-1, blank=True, null=True
    )
    completion_date_type = models.CharField(
        max_length=-1, blank=True, null=True
    )
    completion_date = models.DateField(blank=True, null=True)
    primary_completion_month_year = models.CharField(
        max_length=-1, blank=True, null=True
    )
    primary_completion_date_type = models.CharField(
        max_length=-1, blank=True, null=True
    )
    primary_completion_date = models.DateField(blank=True, null=True)
    target_duration = models.CharField(max_length=-1, blank=True, null=True)
    study_type = models.CharField(max_length=-1, blank=True, null=True)
    acronym = models.CharField(max_length=-1, blank=True, null=True)
    baseline_population = models.TextField(blank=True, null=True)
    brief_title = models.TextField(blank=True, null=True)
    official_title = models.TextField(blank=True, null=True)
    overall_status = models.CharField(max_length=-1, blank=True, null=True)
    last_known_status = models.CharField(max_length=-1, blank=True, null=True)
    phase = models.CharField(max_length=-1, blank=True, null=True)
    enrollment = models.IntegerField(blank=True, null=True)
    enrollment_type = models.CharField(max_length=-1, blank=True, null=True)
    source = models.CharField(max_length=-1, blank=True, null=True)
    limitations_and_caveats = models.CharField(
        max_length=-1, blank=True, null=True
    )
    number_of_arms = models.IntegerField(blank=True, null=True)
    number_of_groups = models.IntegerField(blank=True, null=True)
    why_stopped = models.CharField(max_length=-1, blank=True, null=True)
    has_expanded_access = models.BooleanField(blank=True, null=True)
    expanded_access_type_individual = models.BooleanField(
        blank=True, null=True
    )
    expanded_access_type_intermediate = models.BooleanField(
        blank=True, null=True
    )
    expanded_access_type_treatment = models.BooleanField(blank=True, null=True)
    has_dmc = models.BooleanField(blank=True, null=True)
    is_fda_regulated_drug = models.BooleanField(blank=True, null=True)
    is_fda_regulated_device = models.BooleanField(blank=True, null=True)
    is_unapproved_device = models.BooleanField(blank=True, null=True)
    is_ppsd = models.BooleanField(blank=True, null=True)
    is_us_export = models.BooleanField(blank=True, null=True)
    biospec_retention = models.CharField(max_length=-1, blank=True, null=True)
    biospec_description = models.TextField(blank=True, null=True)
    ipd_time_frame = models.CharField(max_length=-1, blank=True, null=True)
    ipd_access_criteria = models.CharField(
        max_length=-1, blank=True, null=True
    )
    ipd_url = models.CharField(max_length=-1, blank=True, null=True)
    plan_to_share_ipd = models.CharField(max_length=-1, blank=True, null=True)
    plan_to_share_ipd_description = models.CharField(
        max_length=-1, blank=True, null=True
    )
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "studies"


class StudyReferences(models.Model):
    nct = models.ForeignKey(Studies, models.DO_NOTHING, blank=True, null=True)
    pmid = models.CharField(max_length=-1, blank=True, null=True)
    reference_type = models.CharField(max_length=-1, blank=True, null=True)
    citation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "study_references"


class StudySearches(models.Model):
    save_tsv = models.BooleanField()
    query = models.CharField(max_length=-1)
    grouping = models.CharField(max_length=-1)
    name = models.CharField(max_length=-1)
    beta_api = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "study_searches"


class StatsExport(models.Model):
    sponsor = models.CharField()
    study_title = models.TextField()
    study_type = models.CharField()
    entry_year = models.IntegerField()
    study_ID = models.CharField()
    url = models.CharField()
    indication = models.CharField()
    treatment_name = models.CharField()
    treatment_duration = models.TextField()
    treatment_duration_unit = models.TextField()
    study_phase = models.CharField()
    arm_number = models.CharField()
    arm_treatment = models.TextField()
    arm_dose = models.TextField()
    arm_dose_unit = models.TextField()
    arm_regimen = models.TextField()
    total_study_number_participants = models.IntegerField()
    arm_number_of_participants = models.IntegerField()
    p_value = models.DecimalField()
    p_value_description = models.CharField()
    method_description = models.TextField()
    time_frame = models.TextField()
    title = models.TextField()
    description = models.TextField()
    arm_population_age_group = models.CharField()
    arm_population_male_percent = models.CharField()
    arm_modality = models.TextField()

    class Meta:
        managed = False
        db_table = "stats_export"
