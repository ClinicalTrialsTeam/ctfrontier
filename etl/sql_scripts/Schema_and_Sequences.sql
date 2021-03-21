CREATE SCHEMA ctfrontier
	AUTHORIZATION "postgres";

-- SEQUENCE: ctfrontier.study_id_seq
CREATE SEQUENCE ctfrontier.study_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.study_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.brief_summary_id_seq
CREATE SEQUENCE ctfrontier.brief_summary_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.brief_summary_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.browse_condition_id_seq
CREATE SEQUENCE ctfrontier.browse_condition_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.browse_condition_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.browse_intervention_id_seq
CREATE SEQUENCE ctfrontier.browse_intervention_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.browse_intervention_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.central_contact_id_seq
CREATE SEQUENCE ctfrontier.central_contact_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.central_contact_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.condition_id_seq
CREATE SEQUENCE ctfrontier.condition_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.condition_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.country_id_seq
CREATE SEQUENCE ctfrontier.country_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.country_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.study_country_id_seq
CREATE SEQUENCE ctfrontier.study_country_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.study_country_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.contact_type_id_seq
CREATE SEQUENCE ctfrontier.contact_type_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.contact_type_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.design_group_id_seq
CREATE SEQUENCE ctfrontier.design_group_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.design_group_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.group_type_id_seq
CREATE SEQUENCE ctfrontier.group_type_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.group_type_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.design_outcome_id_seq
CREATE SEQUENCE ctfrontier.design_outcome_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.design_outcome_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.outcome_type_id_seq
CREATE SEQUENCE ctfrontier.outcome_type_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.outcome_type_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.design_id_seq
CREATE SEQUENCE ctfrontier.design_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.design_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.primary_purpose_id_seq
CREATE SEQUENCE ctfrontier.primary_purpose_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.primary_purpose_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.intervention_model_id_seq
CREATE SEQUENCE ctfrontier.intervention_model_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.intervention_model_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.observational_model_id_seq
CREATE SEQUENCE ctfrontier.observational_model_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.observational_model_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.allocation_model_id_seq
CREATE SEQUENCE ctfrontier.allocation_model_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.allocation_model_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.time_perspective_id_seq
CREATE SEQUENCE ctfrontier.time_perspective_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.time_perspective_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.masking_id_seq
CREATE SEQUENCE ctfrontier.masking_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.masking_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.detailed_description_id_seq
CREATE SEQUENCE ctfrontier.detailed_description_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.detailed_description_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.document_id_seq
CREATE SEQUENCE ctfrontier.document_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.document_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.provided_document_id_seq
CREATE SEQUENCE ctfrontier.provided_document_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.provided_document_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.eligibility_id_seq
CREATE SEQUENCE ctfrontier.eligibility_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.eligibility_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.facility_id_seq
CREATE SEQUENCE ctfrontier.facility_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.facility_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.study_facility_id_seq
CREATE SEQUENCE ctfrontier.study_facility_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.study_facility_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.facility_contact_id_seq
CREATE SEQUENCE ctfrontier.facility_contact_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.facility_contact_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.id_information_id_seq
CREATE SEQUENCE ctfrontier.id_information_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.id_information_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.intervention_other_name_id_seq
CREATE SEQUENCE ctfrontier.intervention_other_name_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.intervention_other_name_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.intervention_id_seq
CREATE SEQUENCE ctfrontier.intervention_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.intervention_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.intervention_type_id_seq
CREATE SEQUENCE ctfrontier.intervention_type_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.intervention_type_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.facility_investigator_id_seq
CREATE SEQUENCE ctfrontier.facility_investigator_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.facility_investigator_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.facility_role_id_seq
CREATE SEQUENCE ctfrontier.facility_role_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.facility_role_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.keyword_id_seq
CREATE SEQUENCE ctfrontier.keyword_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.keyword_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.external_link_id_seq
CREATE SEQUENCE ctfrontier.external_link_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.external_link_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.overall_official_id_seq
CREATE SEQUENCE ctfrontier.overall_official_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.overall_official_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.official_role_id_seq
CREATE SEQUENCE ctfrontier.official_role_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.official_role_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.responsible_party_id_seq
CREATE SEQUENCE ctfrontier.responsible_party_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.responsible_party_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.responsible_party_type_id_seq
CREATE SEQUENCE ctfrontier.responsible_party_type_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.responsible_party_type_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.affiliate_id_seq
CREATE SEQUENCE ctfrontier.affiliate_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.affiliate_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.sponsor_id_seq
CREATE SEQUENCE ctfrontier.sponsor_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.sponsor_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.study_reference_id_seq
CREATE SEQUENCE ctfrontier.study_reference_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.study_reference_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.result_agreement_id_seq
CREATE SEQUENCE ctfrontier.result_agreement_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.result_agreement_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.result_contact_id_seq
CREATE SEQUENCE ctfrontier.result_contact_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.result_contact_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.organization_id_seq
CREATE SEQUENCE ctfrontier.organization_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.organization_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.result_group_id_seq
CREATE SEQUENCE ctfrontier.result_group_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.result_group_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.group_code_id_seq
CREATE SEQUENCE ctfrontier.group_code_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.group_code_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.result_type_id_seq
CREATE SEQUENCE ctfrontier.result_type_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.result_type_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.pending_result_id_seq
CREATE SEQUENCE ctfrontier.pending_result_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.pending_result_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.baseline_measurement_id_seq
CREATE SEQUENCE ctfrontier.baseline_measurement_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.baseline_measurement_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.category_id_seq
CREATE SEQUENCE ctfrontier.category_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.category_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.classification_id_seq
CREATE SEQUENCE ctfrontier.classification_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.classification_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.baseline_count_id_seq
CREATE SEQUENCE ctfrontier.baseline_count_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.baseline_count_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.reported_event_id_seq
CREATE SEQUENCE ctfrontier.reported_event_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.reported_event_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.outcome_id_seq
CREATE SEQUENCE ctfrontier.outcome_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.outcome_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.outcome_analysis_group_id_seq
CREATE SEQUENCE ctfrontier.outcome_analysis_group_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.outcome_analysis_group_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.outcome_analysis_id_seq
CREATE SEQUENCE ctfrontier.outcome_analysis_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.outcome_analysis_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.outcome_measurement_id_seq
CREATE SEQUENCE ctfrontier.outcome_measurement_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.outcome_measurement_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.outcome_count_id_seq
CREATE SEQUENCE ctfrontier.outcome_count_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.outcome_count_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.participant_flow_id_seq
CREATE SEQUENCE ctfrontier.participant_flow_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.participant_flow_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.milestone_id_seq
CREATE SEQUENCE ctfrontier.milestone_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.milestone_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.drop_withdrawal_id_seq
CREATE SEQUENCE ctfrontier.drop_withdrawal_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.drop_withdrawal_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.study_type_id_seq
CREATE SEQUENCE ctfrontier.study_type_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.study_type_id_seq
	OWNER TO "postgres";

-- SEQUENCE: ctfrontier.date_type_id_seq
CREATE SEQUENCE ctfrontier.date_type_id_seq
	INCREMENT 1
	START 1
	MINVALUE 1
	MAXVALUE 9223372036854775807
	CACHE 1;
ALTER SEQUENCE ctfrontier.date_type_id_seq
	OWNER TO "postgres";
