from django.db import models


class AnalyzedStudies(models.Model):
    id = models.BigAutoField(primary_key=True)
    nct_id = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    brief_title = models.TextField(blank=True, null=True)
    start_month = models.TextField(blank=True, null=True)
    start_year = models.IntegerField(blank=True, null=True)
    overall_status = models.TextField(blank=True, null=True)
    p_completion_month = models.TextField(blank=True, null=True)
    p_completion_year = models.IntegerField(blank=True, null=True)
    completion_month = models.TextField(blank=True, null=True)
    completion_year = models.IntegerField(blank=True, null=True)
    verification_month = models.TextField(blank=True, null=True)
    verification_year = models.IntegerField(blank=True, null=True)
    p_comp_mn = models.IntegerField(blank=True, null=True)
    p_comp_yr = models.IntegerField(blank=True, null=True)
    received_year = models.IntegerField(blank=True, null=True)
    mntopcom = models.IntegerField(blank=True, null=True)
    enrollment = models.IntegerField(blank=True, null=True)
    number_of_arms = models.IntegerField(blank=True, null=True)
    allocation = models.TextField(blank=True, null=True)
    masking = models.TextField(blank=True, null=True)
    phase = models.TextField(blank=True, null=True)
    primary_purpose = models.TextField(blank=True, null=True)
    sponsor_name = models.TextField(blank=True, null=True)
    agency_class = models.TextField(blank=True, null=True)
    collaborator_names = models.TextField(blank=True, null=True)
    funding = models.TextField(blank=True, null=True)
    responsible_party_type = models.TextField(blank=True, null=True)
    responsible_party_organization = models.TextField(blank=True, null=True)
    us_coderc = models.TextField(blank=True, null=True)
    oversight = models.TextField(blank=True, null=True)
    behavioral = models.TextField(blank=True, null=True)
    biological = models.TextField(blank=True, null=True)
    device = models.TextField(blank=True, null=True)
    dietsup = models.TextField(blank=True, null=True)
    drug = models.TextField(blank=True, null=True)
    genetic = models.TextField(blank=True, null=True)
    procedure = models.TextField(blank=True, null=True)
    radiation = models.TextField(blank=True, null=True)
    otherint = models.TextField(blank=True, null=True)
    intervg1 = models.TextField(blank=True, null=True)
    results = models.TextField(blank=True, null=True)
    resultsreceived_month = models.TextField(blank=True, null=True)
    resultsreceived_year = models.TextField(blank=True, null=True)
    firstreceived_results_dt = models.DateField(blank=True, null=True)
    t2result = models.IntegerField(blank=True, null=True)
    t2result_imp = models.IntegerField(blank=True, null=True)
    t2resmod = models.IntegerField(blank=True, null=True)
    results12 = models.TextField(blank=True, null=True)
    delayed = models.TextField(blank=True, null=True)
    dr_received_dt = models.DateField(blank=True, null=True)
    mn2delay = models.BooleanField(blank=True, null=True)
    delayed12 = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "analyzed_studies"


class BaselineCounts(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    result_group = models.ForeignKey(
        "ResultGroups", models.DO_NOTHING, blank=True, null=True
    )
    ctgov_group_code = models.TextField(blank=True, null=True)
    units = models.TextField(blank=True, null=True)
    scope = models.TextField(blank=True, null=True)
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
    ctgov_group_code = models.TextField(blank=True, null=True)
    classification = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    units = models.TextField(blank=True, null=True)
    param_type = models.TextField(blank=True, null=True)
    param_value = models.TextField(blank=True, null=True)
    param_value_num = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    dispersion_type = models.TextField(blank=True, null=True)
    dispersion_value = models.TextField(blank=True, null=True)
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
        db_table = "baseline_measurements"


class BriefSummaries(models.Model):
    nct = models.OneToOneField(
        "Studies", on_delete=models.DO_NOTHING, blank=True, null=True
    )
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "brief_summaries"


class BrowseConditions(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    mesh_term = models.TextField(blank=True, null=True)
    downcase_mesh_term = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "browse_conditions"


class BrowseInterventions(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    mesh_term = models.TextField(blank=True, null=True)
    downcase_mesh_term = models.TextField(blank=True, null=True)

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
    minimum_age_unit = models.TextField(blank=True, null=True)
    maximum_age_unit = models.TextField(blank=True, null=True)
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


class CardiovascularStudies(models.Model):
    id = models.BigAutoField(primary_key=True)
    nct_id = models.TextField(blank=True, null=True)
    brief_title = models.TextField(blank=True, null=True)
    lead_sponsor = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cardiovascular_studies"


class Categories(models.Model):
    nct = models.ForeignKey("Studies", models.DO_NOTHING)
    name = models.TextField(max_length=-1)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    grouping = models.TextField(max_length=-1)
    study_search_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "categories"


class CdekOrganizations(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    downcase_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cdek_organizations"


class CdekSynonyms(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    preferred_name = models.TextField(blank=True, null=True)
    downcase_name = models.TextField(blank=True, null=True)
    downcase_preferred_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cdek_synonyms"


class CentralContacts(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    contact_type = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "central_contacts"


class Conditions(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    name = models.TextField(blank=True, null=True)
    downcase_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "conditions"


class Countries(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    name = models.TextField(blank=True, null=True)
    removed = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "countries"


# Unable to inspect table 'covid_study_ids'
# The error was: permission denied for table covid_study_ids


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
    group_type = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "design_groups"


class DesignOutcomes(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    outcome_type = models.TextField(blank=True, null=True)
    measure = models.TextField(blank=True, null=True)
    time_frame = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "design_outcomes"


class Designs(models.Model):
    nct = models.OneToOneField(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    allocation = models.TextField(blank=True, null=True)
    intervention_model = models.TextField(blank=True, null=True)
    observational_model = models.TextField(blank=True, null=True)
    primary_purpose = models.TextField(blank=True, null=True)
    time_perspective = models.TextField(blank=True, null=True)
    masking = models.TextField(blank=True, null=True)
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


class Documents(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    document_id = models.TextField(blank=True, null=True)
    document_type = models.TextField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)
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
    ctgov_group_code = models.TextField(blank=True, null=True)
    period = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "drop_withdrawals"


class Eligibilities(models.Model):
    nct = models.OneToOneField(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    sampling_method = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    minimum_age = models.TextField(blank=True, null=True)
    maximum_age = models.TextField(blank=True, null=True)
    healthy_volunteers = models.TextField(blank=True, null=True)
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
    status = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    city = models.TextField(blank=True, null=True)
    state = models.TextField(blank=True, null=True)
    zip = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)

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
    contact_type = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)

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
    role = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "facility_investigators"


class IdInformation(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    id_type = models.TextField(blank=True, null=True)
    id_value = models.TextField(blank=True, null=True)

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
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "intervention_other_names"


class Interventions(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    intervention_type = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "interventions"


class IpdInformationTypes(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "ipd_information_types"


class Keywords(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    name = models.TextField(blank=True, null=True)
    downcase_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "keywords"


class Links(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "links"


class MentalHealthStudies(models.Model):
    id = models.BigAutoField(primary_key=True)
    nct_id = models.TextField(blank=True, null=True)
    brief_title = models.TextField(blank=True, null=True)
    lead_sponsor = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mental_health_studies"


class MeshHeadings(models.Model):
    qualifier = models.TextField(blank=True, null=True)
    heading = models.TextField(blank=True, null=True)
    subcategory = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "mesh_headings"


class MeshTerms(models.Model):
    qualifier = models.TextField(blank=True, null=True)
    tree_number = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mesh_term = models.TextField(blank=True, null=True)
    downcase_mesh_term = models.TextField(blank=True, null=True)

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
    ctgov_group_code = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    period = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "milestones"


class OncologyStudies(models.Model):
    id = models.BigAutoField(primary_key=True)
    nct_id = models.TextField(blank=True, null=True)
    brief_title = models.TextField(blank=True, null=True)
    lead_sponsor = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "oncology_studies"


class OutcomeAnalyses(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    outcome = models.ForeignKey(
        "Outcomes", models.DO_NOTHING, blank=True, null=True
    )
    non_inferiority_type = models.TextField(blank=True, null=True)
    non_inferiority_description = models.TextField(blank=True, null=True)
    param_type = models.TextField(blank=True, null=True)
    param_value = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    dispersion_type = models.TextField(blank=True, null=True)
    dispersion_value = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    p_value_modifier = models.TextField(blank=True, null=True)
    p_value = models.FloatField(blank=True, null=True)
    ci_n_sides = models.TextField(blank=True, null=True)
    ci_percent = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    ci_lower_limit = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    ci_upper_limit = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    ci_upper_limit_na_comment = models.TextField(blank=True, null=True)
    p_value_description = models.TextField(blank=True, null=True)
    method = models.TextField(blank=True, null=True)
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
    ctgov_group_code = models.TextField(blank=True, null=True)

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
    ctgov_group_code = models.TextField(blank=True, null=True)
    scope = models.TextField(blank=True, null=True)
    units = models.TextField(blank=True, null=True)
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
    ctgov_group_code = models.TextField(blank=True, null=True)
    classification = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    units = models.TextField(blank=True, null=True)
    param_type = models.TextField(blank=True, null=True)
    param_value = models.TextField(blank=True, null=True)
    param_value_num = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    dispersion_type = models.TextField(blank=True, null=True)
    dispersion_value = models.TextField(blank=True, null=True)
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
    outcome_type = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    time_frame = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    anticipated_posting_date = models.DateField(blank=True, null=True)
    anticipated_posting_month_year = models.TextField(blank=True, null=True)
    units = models.TextField(blank=True, null=True)
    units_analyzed = models.TextField(blank=True, null=True)
    dispersion_type = models.TextField(blank=True, null=True)
    param_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "outcomes"


class OverallOfficials(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    role = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    affiliation = models.TextField(blank=True, null=True)

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
    event = models.TextField(blank=True, null=True)
    event_date_description = models.TextField(blank=True, null=True)
    event_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "pending_results"


class ProvidedDocuments(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    document_type = models.TextField(blank=True, null=True)
    has_protocol = models.BooleanField(blank=True, null=True)
    has_icf = models.BooleanField(blank=True, null=True)
    has_sap = models.BooleanField(blank=True, null=True)
    document_date = models.DateField(blank=True, null=True)
    url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "provided_documents"


class ReportedEventTotals(models.Model):
    nct = models.ForeignKey("Studies", models.DO_NOTHING)
    ctgov_group_code = models.TextField(max_length=-1)
    event_type = models.TextField(blank=True, null=True)
    classification = models.TextField(max_length=-1)
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
    ctgov_group_code = models.TextField(blank=True, null=True)
    time_frame = models.TextField(blank=True, null=True)
    event_type = models.TextField(blank=True, null=True)
    default_vocab = models.TextField(blank=True, null=True)
    default_assessment = models.TextField(blank=True, null=True)
    subjects_affected = models.IntegerField(blank=True, null=True)
    subjects_at_risk = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    event_count = models.IntegerField(blank=True, null=True)
    organ_system = models.TextField(blank=True, null=True)
    adverse_event_term = models.TextField(blank=True, null=True)
    frequency_threshold = models.IntegerField(blank=True, null=True)
    vocab = models.TextField(blank=True, null=True)
    assessment = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "reported_events"


class ResponsibleParties(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    responsible_party_type = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    organization = models.TextField(blank=True, null=True)
    affiliation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "responsible_parties"


class ResultAgreements(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    pi_employee = models.TextField(blank=True, null=True)
    agreement = models.TextField(blank=True, null=True)
    restriction_type = models.TextField(blank=True, null=True)
    other_details = models.TextField(blank=True, null=True)
    restrictive_agreement = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "result_agreements"


class ResultContacts(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    organization = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    phone = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "result_contacts"


class ResultGroups(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    ctgov_group_code = models.TextField(blank=True, null=True)
    result_type = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "result_groups"


class Sponsors(models.Model):
    nct = models.ForeignKey(
        "Studies", models.DO_NOTHING, blank=True, null=True
    )
    agency_class = models.TextField(blank=True, null=True)
    lead_or_collaborator = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "sponsors"


class Studies(models.Model):
    nct_id = models.TextField(unique=True, blank=True, null=True)
    nlm_download_date_description = models.TextField(blank=True, null=True)
    study_first_submitted_date = models.DateField(blank=True, null=True)
    results_first_submitted_date = models.DateField(blank=True, null=True)
    disposition_first_submitted_date = models.DateField(blank=True, null=True)
    last_update_submitted_date = models.DateField(blank=True, null=True)
    study_first_submitted_qc_date = models.DateField(blank=True, null=True)
    study_first_posted_date = models.DateField(blank=True, null=True)
    study_first_posted_date_type = models.TextField(blank=True, null=True)
    results_first_submitted_qc_date = models.DateField(blank=True, null=True)
    results_first_posted_date = models.DateField(blank=True, null=True)
    results_first_posted_date_type = models.TextField(blank=True, null=True)
    disposition_first_submitted_qc_date = models.DateField(
        blank=True, null=True
    )
    disposition_first_posted_date = models.DateField(blank=True, null=True)
    disposition_first_posted_date_type = models.TextField(
        blank=True, null=True
    )
    last_update_submitted_qc_date = models.DateField(blank=True, null=True)
    last_update_posted_date = models.DateField(blank=True, null=True)
    last_update_posted_date_type = models.TextField(blank=True, null=True)
    start_month_year = models.TextField(blank=True, null=True)
    start_date_type = models.TextField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    verification_month_year = models.TextField(blank=True, null=True)
    verification_date = models.DateField(blank=True, null=True)
    completion_month_year = models.TextField(blank=True, null=True)
    completion_date_type = models.TextField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    primary_completion_month_year = models.TextField(blank=True, null=True)
    primary_completion_date_type = models.TextField(blank=True, null=True)
    primary_completion_date = models.DateField(blank=True, null=True)
    target_duration = models.TextField(blank=True, null=True)
    study_type = models.TextField(blank=True, null=True)
    acronym = models.TextField(blank=True, null=True)
    baseline_population = models.TextField(blank=True, null=True)
    brief_title = models.TextField(blank=True, null=True)
    official_title = models.TextField(blank=True, null=True)
    overall_status = models.TextField(blank=True, null=True)
    last_known_status = models.TextField(blank=True, null=True)
    phase = models.TextField(blank=True, null=True)
    enrollment = models.IntegerField(blank=True, null=True)
    enrollment_type = models.TextField(blank=True, null=True)
    source = models.TextField(blank=True, null=True)
    limitations_and_caveats = models.TextField(blank=True, null=True)
    number_of_arms = models.IntegerField(blank=True, null=True)
    number_of_groups = models.IntegerField(blank=True, null=True)
    why_stopped = models.TextField(blank=True, null=True)
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
    biospec_retention = models.TextField(blank=True, null=True)
    biospec_description = models.TextField(blank=True, null=True)
    ipd_time_frame = models.TextField(blank=True, null=True)
    ipd_access_criteria = models.TextField(blank=True, null=True)
    ipd_url = models.TextField(blank=True, null=True)
    plan_to_share_ipd = models.TextField(blank=True, null=True)
    plan_to_share_ipd_description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "studies"


class StudyReferences(models.Model):
    nct = models.ForeignKey(Studies, models.DO_NOTHING, blank=True, null=True)
    pmid = models.TextField(blank=True, null=True)
    reference_type = models.TextField(blank=True, null=True)
    citation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "study_references"


class StudySearches(models.Model):
    save_tsv = models.BooleanField()
    query = models.TextField(max_length=-1)
    grouping = models.TextField(max_length=-1)
    name = models.TextField(max_length=-1)
    beta_api = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = "study_searches"


class TaggedTerms(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.TextField(blank=True, null=True)
    term = models.TextField(blank=True, null=True)
    term_type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "tagged_terms"


# Unable to inspect table 'univ_als_studies'
# The error was: permission denied for table univ_als_studies
# Unable to inspect table 'univ_studies'
# The error was: permission denied for table univ_studies
# Unable to inspect table 'universities'
# The error was: permission denied for table universities


class Y2010MeshTerms(models.Model):
    id = models.BigAutoField(primary_key=True)
    qualifier = models.TextField(blank=True, null=True)
    tree_number = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mesh_term = models.TextField(blank=True, null=True)
    downcase_mesh_term = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "y2010_mesh_terms"


class Y2016MeshHeadings(models.Model):
    id = models.BigAutoField(primary_key=True)
    qualifier = models.TextField(blank=True, null=True)
    heading = models.TextField(blank=True, null=True)
    subcategory = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "y2016_mesh_headings"


class Y2016MeshTerms(models.Model):
    id = models.BigAutoField(primary_key=True)
    qualifier = models.TextField(blank=True, null=True)
    tree_number = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mesh_term = models.TextField(blank=True, null=True)
    downcase_mesh_term = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "y2016_mesh_terms"


class Y2018MeshTerms(models.Model):
    id = models.BigAutoField(primary_key=True)
    qualifier = models.TextField(blank=True, null=True)
    tree_number = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    mesh_term = models.TextField(blank=True, null=True)
    downcase_mesh_term = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "y2018_mesh_terms"


class AllBrowseConditions(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_browse_conditions"


class AllBrowseInterventions(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_browse_interventions"


class AllCities(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_cities"


class AllConditions(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_conditions"


class AllCountries(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_countries"


class AllDesignOutcomes(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_design_outcomes"


class AllFacilities(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_facilities"


class AllGroupTypes(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_group_types"


class AllIdInformation(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_id_information"


class AllInterventionTypes(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_intervention_types"


class AllInterventions(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_interventions"


class AllKeywords(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_keywords"


class AllOverallOfficialAffiliations(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_overall_official_affiliations"


class AllOverallOfficials(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_overall_officials"


class AllPrimaryOutcomeMeasures(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_primary_outcome_measures"


class AllSecondaryOutcomeMeasures(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_secondary_outcome_measures"


class AllSponsors(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_sponsors"


class AllStates(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    names = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "all_states"


class Covid19Studies(models.Model):
    nct_id = models.TextField(blank=True, null=True)
    overall_status = models.TextField(blank=True, null=True)
    study_type = models.TextField(blank=True, null=True)
    official_title = models.TextField(blank=True, null=True)
    acronym = models.TextField(blank=True, null=True)
    phase = models.TextField(blank=True, null=True)
    why_stopped = models.TextField(blank=True, null=True)
    has_dmc = models.BooleanField(blank=True, null=True)
    enrollment = models.IntegerField(blank=True, null=True)
    is_fda_regulated_device = models.BooleanField(blank=True, null=True)
    is_fda_regulated_drug = models.BooleanField(blank=True, null=True)
    is_unapproved_device = models.BooleanField(blank=True, null=True)
    has_expanded_access = models.BooleanField(blank=True, null=True)
    study_first_submitted_date = models.DateField(blank=True, null=True)
    last_update_posted_date = models.DateField(blank=True, null=True)
    results_first_posted_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    primary_completion_date = models.DateField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    study_first_posted_date = models.DateField(blank=True, null=True)
    number_of_facilities = models.IntegerField(blank=True, null=True)
    has_single_facility = models.BooleanField(blank=True, null=True)
    nlm_download_date = models.DateField(blank=True, null=True)
    number_of_arms = models.IntegerField(blank=True, null=True)
    number_of_groups = models.IntegerField(blank=True, null=True)
    lead_sponsor = models.TextField(blank=True, null=True)
    other_ids = models.TextField(blank=True, null=True)
    gender = models.TextField(blank=True, null=True)
    gender_based = models.BooleanField(blank=True, null=True)
    gender_description = models.TextField(blank=True, null=True)
    population = models.TextField(blank=True, null=True)
    minimum_age = models.TextField(blank=True, null=True)
    maximum_age = models.TextField(blank=True, null=True)
    criteria = models.TextField(blank=True, null=True)
    healthy_volunteers = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    interventions = models.TextField(blank=True, null=True)
    conditions = models.TextField(blank=True, null=True)
    primary_purpose = models.TextField(blank=True, null=True)
    allocation = models.TextField(blank=True, null=True)
    observational_model = models.TextField(blank=True, null=True)
    intervention_model = models.TextField(blank=True, null=True)
    masking = models.TextField(blank=True, null=True)
    subject_masked = models.BooleanField(blank=True, null=True)
    caregiver_masked = models.BooleanField(blank=True, null=True)
    investigator_masked = models.BooleanField(blank=True, null=True)
    outcomes_assessor_masked = models.BooleanField(blank=True, null=True)
    design_outcomes = models.TextField(blank=True, null=True)
    brief_summary = models.TextField(blank=True, null=True)
    detailed_description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "covid_19_studies"


class SearchStudies(models.Model):
    status = models.TextField(blank=True, null=True)
    brief_title = models.TextField(blank=True, null=True)
    official_title = models.TextField(blank=True, null=True)
    nct_id = models.TextField(primary_key=True, null=False)
    condition_name = models.TextField(blank=True, null=True)
    study_detailed_desc = models.TextField(blank=True, null=True)
    country_name = models.TextField(blank=True, null=True)
    intervention_name = models.TextField(blank=True, null=True)
    keywords = models.TextField(blank=True, null=True)
    eligibility_criteria = models.TextField(blank=True, null=True)
    eligibility_gender = models.TextField(blank=True, null=True)
    eligibility_min_age = models.TextField(blank=True, null=True)
    eligibility_min_age_numeric = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    eligibility_max_age = models.TextField(blank=True, null=True)
    eligibility_max_age_numeric = models.DecimalField(
        max_digits=65535, decimal_places=65535, blank=True, null=True
    )
    healthy_volunteers = models.TextField(blank=True, null=True)
    location_name = models.TextField(blank=True, null=True)
    study_brief_desc = models.TextField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = "search_studies"
