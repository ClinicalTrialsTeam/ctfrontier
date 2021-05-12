class SqlScripts:
    last_run_date = """
    SELECT last_run_date
    FROM ctgov.etl
    """

    update_count_from_ctti = """
    SELECT COUNT(*)
    FROM ctgov.studies
    WHERE last_update_submitted_date >= %s
    AND study_first_submitted_date < %s |

    UPDATE ctgov.etl
    SET update_max_rows = %s
    """

    insert_count_from_ctti = """
    SELECT COUNT(*)
    FROM ctgov.studies
    WHERE study_first_submitted_date >= %s |

    UPDATE ctgov.etl
    SET insert_max_rows = %s
    """

    get_etl_metadata = """
    SELECT last_run_date,
           insert_current_offset,
           insert_max_rows,
           update_current_offset,
           update_max_rows
    FROM ctgov.etl
    """

    insert_studies = """
    SELECT nct_id, nlm_download_date_description,
           study_first_submitted_date, results_first_submitted_date,
           disposition_first_submitted_date, last_update_submitted_date,
           study_first_submitted_qc_date, study_first_posted_date,
           study_first_posted_date_type, results_first_submitted_qc_date,
           results_first_posted_date, results_first_posted_date_type,
           disposition_first_submitted_qc_date, disposition_first_posted_date,
           disposition_first_posted_date_type, last_update_submitted_qc_date,
           last_update_posted_date, last_update_posted_date_type,
           start_month_year, start_date_type, start_date,
           verification_month_year, verification_date,
           completion_month_year, completion_date_type, completion_date,
           primary_completion_month_year, primary_completion_date_type,
           primary_completion_date, target_duration, study_type, acronym,
           baseline_population, brief_title, official_title, overall_status,
           last_known_status, phase, enrollment, enrollment_type, source,
           limitations_and_caveats, number_of_arms, number_of_groups,
           why_stopped, has_expanded_access, expanded_access_type_individual,
           expanded_access_type_intermediate, expanded_access_type_treatment,
           has_dmc, is_fda_regulated_drug, is_fda_regulated_device,
           is_unapproved_device, is_ppsd, is_us_export, biospec_retention,
           biospec_description, ipd_time_frame, ipd_access_criteria, ipd_url,
           plan_to_share_ipd, plan_to_share_ipd_description, created_at,
           updated_at
    FROM ctgov.studies
    WHERE study_first_submitted_date >= %s
    ORDER BY created_at LIMIT %s OFFSET %s |

    INSERT INTO ctgov.studies(nct_id, nlm_download_date_description,
                              study_first_submitted_date,
                              results_first_submitted_date,
                              disposition_first_submitted_date,
                              last_update_submitted_date,
                              study_first_submitted_qc_date,
                              study_first_posted_date,
                              study_first_posted_date_type,
                              results_first_submitted_qc_date,
                              results_first_posted_date,
                              results_first_posted_date_type,
                              disposition_first_submitted_qc_date,
                              disposition_first_posted_date,
                              disposition_first_posted_date_type,
                              last_update_submitted_qc_date,
                              last_update_posted_date,
                              last_update_posted_date_type, start_month_year,
                              start_date_type, start_date,
                              verification_month_year, verification_date,
                              completion_month_year, completion_date_type,
                              completion_date, primary_completion_month_year,
                              primary_completion_date_type,
                              primary_completion_date, target_duration,
                              study_type, acronym, baseline_population,
                              brief_title, official_title, overall_status,
                              last_known_status, phase, enrollment,
                              enrollment_type, source, limitations_and_caveats,
                              number_of_arms, number_of_groups, why_stopped,
                              has_expanded_access,
                              expanded_access_type_individual,
                              expanded_access_type_intermediate,
                              expanded_access_type_treatment, has_dmc,
                              is_fda_regulated_drug, is_fda_regulated_device,
                              is_unapproved_device, is_ppsd, is_us_export,
                              biospec_retention, biospec_description,
                              ipd_time_frame, ipd_access_criteria, ipd_url,
                              plan_to_share_ipd, plan_to_share_ipd_description,
                              created_at, updated_at)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    update_studies = """
    SELECT nlm_download_date_description, study_first_submitted_date,
           results_first_submitted_date, disposition_first_submitted_date,
           last_update_submitted_date, study_first_submitted_qc_date,
           study_first_posted_date, study_first_posted_date_type,
           results_first_submitted_qc_date, results_first_posted_date,
           results_first_posted_date_type, disposition_first_submitted_qc_date,
           disposition_first_posted_date, disposition_first_posted_date_type,
           last_update_submitted_qc_date, last_update_posted_date,
           last_update_posted_date_type, start_month_year, start_date_type,
           start_date, verification_month_year, verification_date,
           completion_month_year, completion_date_type, completion_date,
           primary_completion_month_year, primary_completion_date_type,
           primary_completion_date, target_duration, study_type, acronym,
           baseline_population, brief_title, official_title, overall_status,
           last_known_status, phase, enrollment, enrollment_type, source,
           limitations_and_caveats, number_of_arms, number_of_groups,
           why_stopped, has_expanded_access, expanded_access_type_individual,
           expanded_access_type_intermediate, expanded_access_type_treatment,
           has_dmc, is_fda_regulated_drug, is_fda_regulated_device,
           is_unapproved_device, is_ppsd, is_us_export, biospec_retention,
           biospec_description, ipd_time_frame, ipd_access_criteria, ipd_url,
           plan_to_share_ipd, plan_to_share_ipd_description, created_at,
           updated_at, nct_id
    FROM ctgov.studies
    WHERE last_update_submitted_date >= %s
    AND study_first_submitted_date < %s
    ORDER BY created_at LIMIT %s OFFSET %s |

    UPDATE ctgov.studies
    SET nlm_download_date_description=%s,
        study_first_submitted_date=%s,
        results_first_submitted_date=%s,
        disposition_first_submitted_date=%s,
        last_update_submitted_date=%s,
        study_first_submitted_qc_date=%s,
        study_first_posted_date=%s,
        study_first_posted_date_type=%s,
        results_first_submitted_qc_date=%s,
        results_first_posted_date=%s,
        results_first_posted_date_type=%s,
        disposition_first_submitted_qc_date=%s,
        disposition_first_posted_date=%s,
        disposition_first_posted_date_type=%s,
        last_update_submitted_qc_date=%s,
        last_update_posted_date=%s,
        last_update_posted_date_type=%s,
        start_month_year=%s,
        start_date_type=%s,
        start_date=%s,
        verification_month_year=%s,
        verification_date=%s,
        completion_month_year=%s,
        completion_date_type=%s,
        completion_date=%s,
        primary_completion_month_year=%s,
        primary_completion_date_type=%s,
        primary_completion_date=%s,
        target_duration=%s,
        study_type=%s,
        acronym=%s,
        baseline_population=%s,
        brief_title=%s,
        official_title=%s,
        overall_status=%s,
        last_known_status=%s,
        phase=%s,
        enrollment=%s,
        enrollment_type=%s,
        source=%s,
        limitations_and_caveats=%s,
        number_of_arms=%s,
        number_of_groups=%s,
        why_stopped=%s,
        has_expanded_access=%s,
        expanded_access_type_individual=%s,
        expanded_access_type_intermediate=%s,
        expanded_access_type_treatment=%s,
        has_dmc=%s,
        is_fda_regulated_drug=%s,
        is_fda_regulated_device=%s,
        is_unapproved_device=%s,
        is_ppsd=%s,
        is_us_export=%s,
        biospec_retention=%s,
        biospec_description=%s,
        ipd_time_frame=%s,
        ipd_access_criteria=%s,
        ipd_url=%s,
        plan_to_share_ipd=%s,
        plan_to_share_ipd_description=%s,
        created_at=%s,
        updated_at=%s
    WHERE nct_id = %s;
    """

    insert_conditions = """
    SELECT id, nct_id, name, downcase_name
    FROM ctgov.conditions
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.conditions(id, nct_id, name, downcase_name)
    VALUES (%s, %s, %s, %s);
    """

    update_conditions = """
    SELECT name, downcase_name, id
    FROM ctgov.conditions
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |

    UPDATE ctgov.conditions
    SET name=%s,
        downcase_name=%s
    WHERE id = %s
    """

    insert_detailed_descriptions = """
    SELECT id, nct_id, description
    FROM ctgov.detailed_descriptions
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.detailed_descriptions(id, nct_id, description)
    VALUES (%s, %s, %s)
    """

    update_detailed_descriptions = """
    SELECT description, id
    FROM ctgov.detailed_descriptions
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    UPDATE ctgov.detailed_descriptions
    SET description= %s
    WHERE id = %s
    """

    insert_countries = """
    SELECT id, nct_id, name, removed
    FROM ctgov.countries
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.countries(id, nct_id, name, removed)
    VALUES (%s, %s, %s, %s);
    """

    update_countries = """
    SELECT name, removed, id
    FROM ctgov.countries
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    UPDATE ctgov.countries
    SET name= %s, removed= %s
    WHERE id = %s;
    """

    insert_interventions = """
    SELECT id, nct_id, intervention_type, name, description
    FROM ctgov.interventions
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.interventions
    (id, nct_id, intervention_type, name, description)
    VALUES (%s, %s, %s, %s, %s);
    """

    update_interventions = """
    SELECT intervention_type, name, description, id
    FROM ctgov.interventions
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    UPDATE ctgov.interventions
    SET intervention_type=%s, name=%s, description=%s
    WHERE id = %s;
    """

    insert_keywords = """
    SELECT id, nct_id, name, downcase_name
    FROM ctgov.keywords
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.keywords(id, nct_id, name, downcase_name)
    VALUES (%s, %s, %s, %s);
    """

    update_keywords = """
    SELECT name, downcase_name, id
    FROM ctgov.keywords
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    UPDATE ctgov.keywords
    SET name=%s, downcase_name=%s
    WHERE id = %s;
    """

    insert_eligibilities = """
    SELECT id, nct_id, sampling_method, gender, minimum_age, maximum_age,
           healthy_volunteers, population, criteria, gender_description,
           gender_based
    FROM ctgov.eligibilities
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.eligibilities(id, nct_id, sampling_method, gender,
                                    minimum_age, maximum_age,
                                    healthy_volunteers, population, criteria,
                                    gender_description, gender_based)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    update_eligibilities = """
    SELECT sampling_method, gender, minimum_age, maximum_age,
           healthy_volunteers, population, criteria, gender_description,
           gender_based, id
    FROM ctgov.eligibilities
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    UPDATE ctgov.eligibilities
    SET sampling_method=%s, gender=%s, minimum_age=%s, maximum_age=%s,
        healthy_volunteers=%s, population=%s, criteria=%s,
        gender_description=%s, gender_based=%s
    WHERE id = %s;
    """

    insert_facilities = """
    SELECT id, nct_id, status, name, city, state, zip, country
    FROM ctgov.facilities
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.facilities(
    id, nct_id, status, name, city, state, zip, country)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
    """

    update_facilities = """
    SELECT status, name, city, state, zip, country, id
    FROM ctgov.facilities
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    UPDATE ctgov.facilities
    SET status=%s, name=%s, city=%s, state=%s, zip=%s, country=%s
    WHERE id = %s;
    """

    insert_brief_summaries = """
    SELECT id, nct_id, description
    FROM ctgov.brief_summaries
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.brief_summaries(id, nct_id, description)
    VALUES (%s, %s, %s);
    """

    update_brief_summaries = """
    SELECT description, id
    FROM ctgov.brief_summaries
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    UPDATE ctgov.brief_summaries
    SET description=%s
    WHERE id = %s;
    """

    insert_sponsors = """
    SELECT id, nct_id, agency_class, lead_or_collaborator, name
    FROM ctgov.sponsors
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.sponsors(
    id, nct_id, agency_class, lead_or_collaborator, name)
    VALUES (%s, %s, %s, %s, %s);
    """

    update_sponsors = """
    SELECT agency_class, lead_or_collaborator, name, id
    FROM ctgov.sponsors
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    UPDATE ctgov.sponsors
    SET agency_class=%s, lead_or_collaborator=%s, name=%s
    WHERE id = %s;
    """

    # Handle Deletes
    insert_outcomes = """
    SELECT id, nct_id, outcome_type, title, description, time_frame,
    population, anticipated_posting_date, anticipated_posting_month_year,
    units, units_analyzed, dispersion_type, param_type
    FROM ctgov.outcomes
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.outcomes(
    id, nct_id, outcome_type, title, description, time_frame, population,
    anticipated_posting_date, anticipated_posting_month_year, units,
    units_analyzed, dispersion_type, param_type)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    update_outcomes = """
    SELECT outcome_type, title, description, time_frame, population,
    anticipated_posting_date, anticipated_posting_month_year, units,
    units_analyzed, dispersion_type, param_type, id
    FROM ctgov.outcomes
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    UPDATE ctgov.outcomes
    SET outcome_type=%s, title=%s, description=%s, time_frame=%s,
        population=%s, anticipated_posting_date=%s,
        anticipated_posting_month_year=%s, units=%s, units_analyzed=%s,
        dispersion_type=%s, param_type=%s
    WHERE id = %s;
    """

    insert_results_groups = """
    SELECT id, nct_id, ctgov_group_code, result_type, title, description
    FROM ctgov.result_groups
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.result_groups(
    id, nct_id, ctgov_group_code, result_type, title, description)
    VALUES (%s, %s, %s, %s, %s, %s);
    """

    update_results_groups = """
    SELECT ctgov_group_code, result_type, title, description, id
    FROM ctgov.result_groups
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    UPDATE ctgov.result_groups
    SET ctgov_group_code=%s, result_type=%s, title=%s, description=%s
    WHERE id = %s;
    """

    insert_outcome_measures = """
    SELECT id, nct_id, outcome_id, result_group_id, ctgov_group_code,
           classification, category, title, description, units, param_type,
           param_value, param_value_num, dispersion_type, dispersion_value,
           dispersion_value_num, dispersion_lower_limit,
           dispersion_upper_limit, explanation_of_na
    FROM ctgov.outcome_measurements
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.outcome_measurements(
    id, nct_id, outcome_id, result_group_id, ctgov_group_code, classification,
    category, title, description, units, param_type, param_value,
    param_value_num, dispersion_type, dispersion_value, dispersion_value_num,
    dispersion_lower_limit, dispersion_upper_limit, explanation_of_na)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s);
    """

    update_outcome_measures = """
    SELECT outcome_id, result_group_id, ctgov_group_code,
           classification, category, title, description, units, param_type,
           param_value, param_value_num, dispersion_type, dispersion_value,
           dispersion_value_num, dispersion_lower_limit,
           dispersion_upper_limit, explanation_of_na, id
    FROM ctgov.outcome_measurements
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    UPDATE ctgov.outcome_measurements
    SET outcome_id=%s, result_group_id=%s, ctgov_group_code=%s,
        classification=%s, category=%s, title=%s, description=%s, units=%s,
        param_type=%s, param_value=%s, param_value_num=%s, dispersion_type=%s,
        dispersion_value=%s, dispersion_value_num=%s,
        dispersion_lower_limit=%s, dispersion_upper_limit=%s,
        explanation_of_na=%s
    WHERE id = %s;
    """

    insert_id_information = """
    SELECT id, nct_id, id_type, id_value
    FROM ctgov.id_information
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.id_information(id, nct_id, id_type, id_value)
    VALUES (%s, %s, %s, %s);
    """

    update_id_information = """
    SELECT id_type, id_value, id
    FROM ctgov.id_information
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    UPDATE ctgov.id_information
    SET id_type=%s, id_value=%s
    WHERE id = %s;
    """

    insert_documents = """
    SELECT id, nct_id, document_id, document_type, url, comment
    FROM ctgov.documents
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE study_first_submitted_date >= %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    INSERT INTO ctgov.documents(
    id, nct_id, document_id, document_type, url, comment)
    VALUES (%s, %s, %s, %s, %s, %s);
    """

    update_documents = """
    SELECT document_id, document_type, url, comment, id
    FROM ctgov.documents
    WHERE nct_id IN (SELECT nct_id
                     FROM ctgov.studies
                     WHERE last_update_submitted_date >= %s
                     AND study_first_submitted_date < %s
                     ORDER BY created_at LIMIT %s OFFSET %s) |
    UPDATE ctgov.documents
    SET document_id=%s, document_type=%s, url=%s, comment=%s
    WHERE id = %s;
    """

    update_last_run_date = """
    UPDATE ctgov.etl
    SET last_run_date = %s
    """

    rebuild_search_studies = """
    REFRESH MATERIALIZED VIEW ctgov.search_studies
    """

    rebuild_all_sponsors_type = """
    REFRESH MATERIALIZED VIEW ctgov.all_sponsors_type
    """

    rebuild_all_documents = """
    REFRESH MATERIALIZED VIEW ctgov.all_documents
    """
