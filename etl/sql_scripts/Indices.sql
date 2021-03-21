

CREATE INDEX contact_type_idx
	ON ctfrontier.contact_type USING btree
	(contact_type_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.contact_type USING contact_type_idx;

CREATE INDEX group_type_idx
	ON ctfrontier.group_type USING btree
	(group_type_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.group_type USING group_type_idx;

CREATE INDEX outcome_type_idx
	ON ctfrontier.outcome_type USING btree
	(outcome_type_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.outcome_type USING outcome_type_idx;

CREATE INDEX primary_purpose_idx
	ON ctfrontier.primary_purpose USING btree
	(primary_purpose_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.primary_purpose USING primary_purpose_idx;

CREATE INDEX intervention_model_idx
	ON ctfrontier.intervention_model USING btree
	(intervention_model_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.intervention_model USING intervention_model_idx;

CREATE INDEX observational_model_idx
	ON ctfrontier.observational_model USING btree
	(observational_model_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.observational_model USING observational_model_idx;

CREATE INDEX allocation_model_idx
	ON ctfrontier.allocation_model USING btree
	(allocation_model_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.allocation_model USING allocation_model_idx;

CREATE INDEX time_perspective_idx
	ON ctfrontier.time_perspective USING btree
	(time_perspective_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.time_perspective USING time_perspective_idx;

CREATE INDEX masking_idx
	ON ctfrontier.masking USING btree
	(masking_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.masking USING masking_idx;

CREATE INDEX facility_idx
	ON ctfrontier.facility USING btree
	(facility_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.facility USING facility_idx;

CREATE INDEX intervention_type_idx
	ON ctfrontier.intervention_type USING btree
	(intervention_type_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.intervention_type USING intervention_type_idx;

CREATE INDEX facility_role_idx
	ON ctfrontier.facility_role USING btree
	(facility_role_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.facility_role USING facility_role_idx;

CREATE INDEX official_role_idx
	ON ctfrontier.official_role USING btree
	(official_role_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.official_role USING official_role_idx;

CREATE INDEX responsible_party_type_idx
	ON ctfrontier.responsible_party_type USING btree
	(responsible_party_type_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.responsible_party_type USING responsible_party_type_idx;

CREATE INDEX affiliate_idx
	ON ctfrontier.affiliate USING btree
	(affiliate_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.affiliate USING affiliate_idx;

CREATE INDEX organization_idx
	ON ctfrontier.organization USING btree
	(organization_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.organization USING organization_idx;

CREATE INDEX group_code_idx
	ON ctfrontier.group_code USING btree
	(group_code_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.group_code USING group_code_idx;

CREATE INDEX result_type_idx
	ON ctfrontier.result_type USING btree
	(result_type_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.result_type USING result_type_idx;

CREATE INDEX category_idx
	ON ctfrontier.category USING btree
	(category_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.category USING category_idx;

CREATE INDEX classification_idx
	ON ctfrontier.classification USING btree
	(classification_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.classification USING classification_idx;

CREATE INDEX study_type_idx
	ON ctfrontier.study_type USING btree
	(study_type_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.study_type USING study_type_idx;

CREATE INDEX date_type_idx
	ON ctfrontier.date_type USING btree
	(date_type_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.date_type USING date_type_idx;

CREATE INDEX study_idx
	ON ctfrontier.study USING btree
	(study_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.study USING study_idx;

CREATE INDEX brief_summary_idx
	ON ctfrontier.brief_summary USING btree
	(brief_summary_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.brief_summary USING brief_summary_idx;

CREATE INDEX browse_condition_idx
	ON ctfrontier.browse_condition USING btree
	(browse_condition_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.browse_condition USING browse_condition_idx;

CREATE INDEX browse_intervention_idx
	ON ctfrontier.browse_intervention USING btree
	(browse_intervention_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.browse_intervention USING browse_intervention_idx;

CREATE INDEX condition_idx
	ON ctfrontier.condition USING btree
	(condition_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.condition USING condition_idx;

CREATE INDEX detailed_description_idx
	ON ctfrontier.detailed_description USING btree
	(detailed_description_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.detailed_description USING detailed_description_idx;

CREATE INDEX document_idx
	ON ctfrontier.document USING btree
	(document_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.document USING document_idx;

CREATE INDEX provided_document_idx
	ON ctfrontier.provided_document USING btree
	(provided_document_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.provided_document USING provided_document_idx;

CREATE INDEX eligibility_idx
	ON ctfrontier.eligibility USING btree
	(eligibility_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.eligibility USING eligibility_idx;

CREATE INDEX id_information_idx
	ON ctfrontier.id_information USING btree
	(id_information_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.id_information USING id_information_idx;

CREATE INDEX keyword_idx
	ON ctfrontier.keyword USING btree
	(keyword_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.keyword USING keyword_idx;

CREATE INDEX external_link_idx
	ON ctfrontier.external_link USING btree
	(external_link_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.external_link USING external_link_idx;

CREATE INDEX sponsor_idx
	ON ctfrontier.sponsor USING btree
	(sponsor_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.sponsor USING sponsor_idx;

CREATE INDEX study_reference_idx
	ON ctfrontier.study_reference USING btree
	(study_reference_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.study_reference USING study_reference_idx;

CREATE INDEX result_agreement_idx
	ON ctfrontier.result_agreement USING btree
	(result_agreement_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.result_agreement USING result_agreement_idx;

CREATE INDEX pending_result_idx
	ON ctfrontier.pending_result USING btree
	(pending_result_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.pending_result USING pending_result_idx;

CREATE INDEX outcome_idx
	ON ctfrontier.outcome USING btree
	(outcome_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.outcome USING outcome_idx;

CREATE INDEX participant_flow_idx
	ON ctfrontier.participant_flow USING btree
	(participant_flow_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.participant_flow USING participant_flow_idx;

CREATE INDEX central_contact_idx
	ON ctfrontier.central_contact USING btree
	(central_contact_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.central_contact USING central_contact_idx;

CREATE INDEX study_country_idx
	ON ctfrontier.study_country USING btree
	(study_country_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.study_country USING study_country_idx;

CREATE INDEX design_group_idx
	ON ctfrontier.design_group USING btree
	(design_group_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.design_group USING design_group_idx;

CREATE INDEX design_outcome_idx
	ON ctfrontier.design_outcome USING btree
	(design_outcome_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.design_outcome USING design_outcome_idx;

CREATE INDEX study_facility_idx
	ON ctfrontier.study_facility USING btree
	(study_facility_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.study_facility USING study_facility_idx;

CREATE INDEX facility_contact_idx
	ON ctfrontier.facility_contact USING btree
	(facility_contact_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.facility_contact USING facility_contact_idx;

CREATE INDEX intervention_idx
	ON ctfrontier.intervention USING btree
	(intervention_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.intervention USING intervention_idx;

CREATE INDEX intervention_other_name_idx
	ON ctfrontier.intervention_other_name USING btree
	(intervention_other_name_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.intervention_other_name USING intervention_other_name_idx;

CREATE INDEX overall_official_idx
	ON ctfrontier.overall_official USING btree
	(overall_official_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.overall_official USING overall_official_idx;

CREATE INDEX result_contact_idx
	ON ctfrontier.result_contact USING btree
	(result_contact_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.result_contact USING result_contact_idx;

CREATE INDEX outcome_analysis_idx
	ON ctfrontier.outcome_analysis USING btree
	(outcome_analysis_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.outcome_analysis USING outcome_analysis_idx;

CREATE INDEX facility_investigator_idx
	ON ctfrontier.facility_investigator USING btree
	(facility_investigator_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.facility_investigator USING facility_investigator_idx;

CREATE INDEX result_group_idx
	ON ctfrontier.result_group USING btree
	(result_group_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.result_group USING result_group_idx;

CREATE INDEX baseline_count_idx
	ON ctfrontier.baseline_count USING btree
	(baseline_count_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.baseline_count USING baseline_count_idx;

CREATE INDEX reported_event_idx
	ON ctfrontier.reported_event USING btree
	(reported_event_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.reported_event USING reported_event_idx;

CREATE INDEX milestone_idx
	ON ctfrontier.milestone USING btree
	(milestone_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.milestone USING milestone_idx;

CREATE INDEX drop_withdrawal_idx
	ON ctfrontier.drop_withdrawal USING btree
	(drop_withdrawal_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.drop_withdrawal USING drop_withdrawal_idx;

CREATE INDEX responsible_party_idx
	ON ctfrontier.responsible_party USING btree
	(responsible_party_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.responsible_party USING responsible_party_idx;

CREATE INDEX outcome_analysis_group_idx
	ON ctfrontier.outcome_analysis_group USING btree
	(outcome_analysis_group_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.outcome_analysis_group USING outcome_analysis_group_idx;

CREATE INDEX outcome_count_idx
	ON ctfrontier.outcome_count USING btree
	(outcome_count_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.outcome_count USING outcome_count_idx;

CREATE INDEX baseline_measurement_idx
	ON ctfrontier.baseline_measurement USING btree
	(baseline_measurement_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.baseline_measurement USING baseline_measurement_idx;

CREATE INDEX outcome_measurement_idx
	ON ctfrontier.outcome_measurement USING btree
	(outcome_measurement_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.outcome_measurement USING outcome_measurement_idx;

CREATE INDEX design_idx
	ON ctfrontier.design USING btree
	(design_id ASC NULLS LAST)
	TABLESPACE pg_default;

CLUSTER ctfrontier.design USING design_idx;

