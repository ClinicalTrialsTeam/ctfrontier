-- TABLE: ctfrontier.country
CREATE TABLE ctfrontier.country
(
	country_id integer NOT NULL DEFAULT nextval('ctfrontier.country_id_seq'::regclass),
	name text COLLATE pg_catalog."default",
	removed boolean,
	CONSTRAINT country_pkey PRIMARY KEY(country_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.country
	OWNER to "postgres";

-- TABLE: ctfrontier.contact_type
CREATE TABLE ctfrontier.contact_type
(
	contact_type_id integer NOT NULL DEFAULT nextval('ctfrontier.contact_type_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT contact_type_pkey PRIMARY KEY(contact_type_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.contact_type
	OWNER to "postgres";

-- TABLE: ctfrontier.group_type
CREATE TABLE ctfrontier.group_type
(
	group_type_id integer NOT NULL DEFAULT nextval('ctfrontier.group_type_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT group_type_pkey PRIMARY KEY(group_type_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.group_type
	OWNER to "postgres";

-- TABLE: ctfrontier.outcome_type
CREATE TABLE ctfrontier.outcome_type
(
	outcome_type_id integer NOT NULL DEFAULT nextval('ctfrontier.outcome_type_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT outcome_type_pkey PRIMARY KEY(outcome_type_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.outcome_type
	OWNER to "postgres";

-- TABLE: ctfrontier.primary_purpose
CREATE TABLE ctfrontier.primary_purpose
(
	primary_purpose_id integer NOT NULL DEFAULT nextval('ctfrontier.primary_purpose_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT primary_purpose_pkey PRIMARY KEY(primary_purpose_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.primary_purpose
	OWNER to "postgres";

-- TABLE: ctfrontier.intervention_model
CREATE TABLE ctfrontier.intervention_model
(
	intervention_model_id integer NOT NULL DEFAULT nextval('ctfrontier.intervention_model_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT intervention_model_pkey PRIMARY KEY(intervention_model_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.intervention_model
	OWNER to "postgres";

-- TABLE: ctfrontier.observational_model
CREATE TABLE ctfrontier.observational_model
(
	observational_model_id integer NOT NULL DEFAULT nextval('ctfrontier.observational_model_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT observational_model_pkey PRIMARY KEY(observational_model_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.observational_model
	OWNER to "postgres";

-- TABLE: ctfrontier.allocation_model
CREATE TABLE ctfrontier.allocation_model
(
	allocation_model_id integer NOT NULL DEFAULT nextval('ctfrontier.allocation_model_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT allocation_model_pkey PRIMARY KEY(allocation_model_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.allocation_model
	OWNER to "postgres";

-- TABLE: ctfrontier.time_perspective
CREATE TABLE ctfrontier.time_perspective
(
	time_perspective_id integer NOT NULL DEFAULT nextval('ctfrontier.time_perspective_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT time_perspective_pkey PRIMARY KEY(time_perspective_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.time_perspective
	OWNER to "postgres";

-- TABLE: ctfrontier.masking
CREATE TABLE ctfrontier.masking
(
	masking_id integer NOT NULL DEFAULT nextval('ctfrontier.masking_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT masking_pkey PRIMARY KEY(masking_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.masking
	OWNER to "postgres";

-- TABLE: ctfrontier.facility
CREATE TABLE ctfrontier.facility
(
	facility_id integer NOT NULL DEFAULT nextval('ctfrontier.facility_id_seq'::regclass),
	status text COLLATE pg_catalog."default",
	name text COLLATE pg_catalog."default",
	city text COLLATE pg_catalog."default",
	state text COLLATE pg_catalog."default",
	zip text COLLATE pg_catalog."default",
	country text COLLATE pg_catalog."default",
	latitude decimal,
	longitude decimal,
	CONSTRAINT facility_pkey PRIMARY KEY(facility_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.facility
	OWNER to "postgres";

-- TABLE: ctfrontier.intervention_type
CREATE TABLE ctfrontier.intervention_type
(
	intervention_type_id integer NOT NULL DEFAULT nextval('ctfrontier.intervention_type_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT intervention_type_pkey PRIMARY KEY(intervention_type_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.intervention_type
	OWNER to "postgres";

-- TABLE: ctfrontier.facility_role
CREATE TABLE ctfrontier.facility_role
(
	facility_role_id integer NOT NULL DEFAULT nextval('ctfrontier.facility_role_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT facility_role_pkey PRIMARY KEY(facility_role_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.facility_role
	OWNER to "postgres";

-- TABLE: ctfrontier.official_role
CREATE TABLE ctfrontier.official_role
(
	official_role_id integer NOT NULL DEFAULT nextval('ctfrontier.official_role_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT official_role_pkey PRIMARY KEY(official_role_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.official_role
	OWNER to "postgres";

-- TABLE: ctfrontier.responsible_party_type
CREATE TABLE ctfrontier.responsible_party_type
(
	responsible_party_type_id integer NOT NULL DEFAULT nextval('ctfrontier.responsible_party_type_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT responsible_party_type_pkey PRIMARY KEY(responsible_party_type_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.responsible_party_type
	OWNER to "postgres";

-- TABLE: ctfrontier.affiliate
CREATE TABLE ctfrontier.affiliate
(
	affiliate_id integer NOT NULL DEFAULT nextval('ctfrontier.affiliate_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT affiliate_pkey PRIMARY KEY(affiliate_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.affiliate
	OWNER to "postgres";

-- TABLE: ctfrontier.organization
CREATE TABLE ctfrontier.organization
(
	organization_id integer NOT NULL DEFAULT nextval('ctfrontier.organization_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT organization_pkey PRIMARY KEY(organization_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.organization
	OWNER to "postgres";

-- TABLE: ctfrontier.group_code
CREATE TABLE ctfrontier.group_code
(
	group_code_id integer NOT NULL DEFAULT nextval('ctfrontier.group_code_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT group_code_pkey PRIMARY KEY(group_code_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.group_code
	OWNER to "postgres";

-- TABLE: ctfrontier.result_type
CREATE TABLE ctfrontier.result_type
(
	result_type_id integer NOT NULL DEFAULT nextval('ctfrontier.result_type_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT result_type_pkey PRIMARY KEY(result_type_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.result_type
	OWNER to "postgres";

-- TABLE: ctfrontier.category
CREATE TABLE ctfrontier.category
(
	category_id integer NOT NULL DEFAULT nextval('ctfrontier.category_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT category_pkey PRIMARY KEY(category_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.category
	OWNER to "postgres";

-- TABLE: ctfrontier.classification
CREATE TABLE ctfrontier.classification
(
	classification_id integer NOT NULL DEFAULT nextval('ctfrontier.classification_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT classification_pkey PRIMARY KEY(classification_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.classification
	OWNER to "postgres";

-- TABLE: ctfrontier.study_type
CREATE TABLE ctfrontier.study_type
(
	study_type_id integer NOT NULL DEFAULT nextval('ctfrontier.study_type_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	create_date timestamp,
	CONSTRAINT study_type_pkey PRIMARY KEY(study_type_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.study_type
	OWNER to "postgres";

-- TABLE: ctfrontier.date_type
CREATE TABLE ctfrontier.date_type
(
	date_type_id integer NOT NULL DEFAULT nextval('ctfrontier.date_type_id_seq'::regclass),
	description text COLLATE pg_catalog."default",
	CONSTRAINT date_type_pkey PRIMARY KEY(date_type_id)
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.date_type
	OWNER to "postgres";

-- TABLE: ctfrontier.study
CREATE TABLE ctfrontier.study
(
	study_id integer NOT NULL DEFAULT nextval('ctfrontier.study_id_seq'::regclass),
	nct_id text COLLATE pg_catalog."default",
	nlm_download_date_description text COLLATE pg_catalog."default",
	study_first_submitted_date date,
	last_update_submitted_date date,
	results_first_submitted_date date,
	disposition_first_submitted_date date,
	start_month_year text COLLATE pg_catalog."default",
	start_date date,
	start_date_type integer NOT NULL,
	verification_month_year text COLLATE pg_catalog."default",
	verification_date date,
	completion_month_year text COLLATE pg_catalog."default",
	completion_date date,
	completion_date_type integer NOT NULL,
	primary_completion_month_year text COLLATE pg_catalog."default",
	primary_completion_date date,
	primary_completion_date_type integer NOT NULL,
	study_first_submitted_qc_date date,
	study_first_posted_date date,
	results_first_submitted_qc_date date,
	results_first_posted_date date,
	disposition_first_submitted_qc_date date,
	disposition_first_posted_date date,
	last_update_submitted_qc_date date,
	last_update_posted_date date,
	target_duration text COLLATE pg_catalog."default",
	study_type_id integer NOT NULL,
	acronym text COLLATE pg_catalog."default",
	baseline_population text COLLATE pg_catalog."default",
	brief_title text COLLATE pg_catalog."default",
	official_title text COLLATE pg_catalog."default",
	overall_status text COLLATE pg_catalog."default",
	last_known_status text COLLATE pg_catalog."default",
	phase text COLLATE pg_catalog."default",
	enrollment integer,
	enrollment_type text COLLATE pg_catalog."default",
	source text COLLATE pg_catalog."default",
	limitations_and_caveats text COLLATE pg_catalog."default",
	number_of_arms integer,
	number_of_groups integer,
	why_stopped text COLLATE pg_catalog."default",
	has_expanded_access boolean,
	expanded_access_type_individual boolean,
	expanded_access_type_intermediate boolean,
	expanded_access_type_treatment boolean,
	has_dmc boolean,
	is_fda_regulated_drug boolean,
	is_fda_regulated_device boolean,
	is_unapproved_device boolean,
	is_ppsd boolean,
	is_us_export boolean,
	biospec_retention text COLLATE pg_catalog."default",
	biospec_description text COLLATE pg_catalog."default",
	plan_to_share_ipd text COLLATE pg_catalog."default",
	plan_to_share_ipd_description text COLLATE pg_catalog."default",
	ipd_time_frame text COLLATE pg_catalog."default",
	ipd_access_criteria text COLLATE pg_catalog."default",
	ipd_url text COLLATE pg_catalog."default",
	created_at timestamp,
	updated_at timestamp,
	hashed_json text COLLATE pg_catalog."default",
	CONSTRAINT study_pkey PRIMARY KEY(study_id),
	CONSTRAINT study_start_date_type_fkey FOREIGN KEY (start_date_type)
		REFERENCES ctfrontier.date_type (date_type_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT study_completion_date_type_fkey FOREIGN KEY (completion_date_type)
		REFERENCES ctfrontier.date_type (date_type_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT study_primary_completion_date_type_fkey FOREIGN KEY (primary_completion_date_type)
		REFERENCES ctfrontier.date_type (date_type_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT study_study_type_id_fkey FOREIGN KEY (study_type_id)
		REFERENCES ctfrontier.study_type (study_type_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.study
	OWNER to "postgres";

-- TABLE: ctfrontier.brief_summary
CREATE TABLE ctfrontier.brief_summary
(
	brief_summary_id integer NOT NULL DEFAULT nextval('ctfrontier.brief_summary_id_seq'::regclass),
	study_id integer NOT NULL,
	description text COLLATE pg_catalog."default",
	CONSTRAINT brief_summary_pkey PRIMARY KEY(brief_summary_id),
	CONSTRAINT brief_summary_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.brief_summary
	OWNER to "postgres";

-- TABLE: ctfrontier.browse_condition
CREATE TABLE ctfrontier.browse_condition
(
	browse_condition_id integer NOT NULL DEFAULT nextval('ctfrontier.browse_condition_id_seq'::regclass),
	study_id integer NOT NULL,
	mesh_term text COLLATE pg_catalog."default",
	CONSTRAINT browse_condition_pkey PRIMARY KEY(browse_condition_id),
	CONSTRAINT browse_condition_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.browse_condition
	OWNER to "postgres";

-- TABLE: ctfrontier.browse_intervention
CREATE TABLE ctfrontier.browse_intervention
(
	browse_intervention_id integer NOT NULL DEFAULT nextval('ctfrontier.browse_intervention_id_seq'::regclass),
	study_id integer NOT NULL,
	mesh_term text COLLATE pg_catalog."default",
	CONSTRAINT browse_intervention_pkey PRIMARY KEY(browse_intervention_id),
	CONSTRAINT browse_intervention_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.browse_intervention
	OWNER to "postgres";

-- TABLE: ctfrontier.condition
CREATE TABLE ctfrontier.condition
(
	condition_id integer NOT NULL DEFAULT nextval('ctfrontier.condition_id_seq'::regclass),
	study_id integer NOT NULL,
	name text COLLATE pg_catalog."default",
	CONSTRAINT condition_pkey PRIMARY KEY(condition_id),
	CONSTRAINT condition_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.condition
	OWNER to "postgres";

-- TABLE: ctfrontier.detailed_description
CREATE TABLE ctfrontier.detailed_description
(
	detailed_description_id integer NOT NULL DEFAULT nextval('ctfrontier.detailed_description_id_seq'::regclass),
	study_id integer NOT NULL,
	description text COLLATE pg_catalog."default",
	CONSTRAINT detailed_description_pkey PRIMARY KEY(detailed_description_id),
	CONSTRAINT detailed_description_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.detailed_description
	OWNER to "postgres";

-- TABLE: ctfrontier.document
CREATE TABLE ctfrontier.document
(
	document_id integer NOT NULL DEFAULT nextval('ctfrontier.document_id_seq'::regclass),
	study_id integer NOT NULL,
	study_document_id text COLLATE pg_catalog."default",
	document_type text COLLATE pg_catalog."default",
	url text COLLATE pg_catalog."default",
	comment text COLLATE pg_catalog."default",
	CONSTRAINT document_pkey PRIMARY KEY(document_id),
	CONSTRAINT document_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.document
	OWNER to "postgres";

-- TABLE: ctfrontier.provided_document
CREATE TABLE ctfrontier.provided_document
(
	provided_document_id integer NOT NULL DEFAULT nextval('ctfrontier.provided_document_id_seq'::regclass),
	study_id integer NOT NULL,
	document_type text COLLATE pg_catalog."default",
	has_protocol boolean,
	has_icf boolean,
	has_sap boolean,
	document_date date,
	url text COLLATE pg_catalog."default",
	CONSTRAINT provided_document_pkey PRIMARY KEY(provided_document_id),
	CONSTRAINT provided_document_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.provided_document
	OWNER to "postgres";

-- TABLE: ctfrontier.eligibility
CREATE TABLE ctfrontier.eligibility
(
	eligibility_id integer NOT NULL DEFAULT nextval('ctfrontier.eligibility_id_seq'::regclass),
	study_id integer NOT NULL,
	population text COLLATE pg_catalog."default",
	sampling_method text COLLATE pg_catalog."default",
	gender text COLLATE pg_catalog."default",
	gender_based boolean,
	gender_description text COLLATE pg_catalog."default",
	minimum_age text COLLATE pg_catalog."default",
	maximum_age text COLLATE pg_catalog."default",
	healthy_volunteers text COLLATE pg_catalog."default",
	criteria text COLLATE pg_catalog."default",
	CONSTRAINT eligibility_pkey PRIMARY KEY(eligibility_id),
	CONSTRAINT eligibility_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.eligibility
	OWNER to "postgres";

-- TABLE: ctfrontier.id_information
CREATE TABLE ctfrontier.id_information
(
	id_information_id integer NOT NULL DEFAULT nextval('ctfrontier.id_information_id_seq'::regclass),
	study_id integer NOT NULL,
	id_type_id text COLLATE pg_catalog."default",
	id_value text COLLATE pg_catalog."default",
	CONSTRAINT id_information_pkey PRIMARY KEY(id_information_id),
	CONSTRAINT id_information_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.id_information
	OWNER to "postgres";

-- TABLE: ctfrontier.keyword
CREATE TABLE ctfrontier.keyword
(
	keyword_id integer NOT NULL DEFAULT nextval('ctfrontier.keyword_id_seq'::regclass),
	study_id integer NOT NULL,
	name text COLLATE pg_catalog."default",
	CONSTRAINT keyword_pkey PRIMARY KEY(keyword_id),
	CONSTRAINT keyword_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.keyword
	OWNER to "postgres";

-- TABLE: ctfrontier.external_link
CREATE TABLE ctfrontier.external_link
(
	external_link_id integer NOT NULL DEFAULT nextval('ctfrontier.external_link_id_seq'::regclass),
	study_id integer NOT NULL,
	url text COLLATE pg_catalog."default",
	description text COLLATE pg_catalog."default",
	CONSTRAINT external_link_pkey PRIMARY KEY(external_link_id),
	CONSTRAINT external_link_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.external_link
	OWNER to "postgres";

-- TABLE: ctfrontier.sponsor
CREATE TABLE ctfrontier.sponsor
(
	sponsor_id integer NOT NULL DEFAULT nextval('ctfrontier.sponsor_id_seq'::regclass),
	study_id integer NOT NULL,
	agency_class text COLLATE pg_catalog."default",
	lead_or_collaborator text COLLATE pg_catalog."default",
	name text COLLATE pg_catalog."default",
	CONSTRAINT sponsor_pkey PRIMARY KEY(sponsor_id),
	CONSTRAINT sponsor_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.sponsor
	OWNER to "postgres";

-- TABLE: ctfrontier.study_reference
CREATE TABLE ctfrontier.study_reference
(
	study_reference_id integer NOT NULL DEFAULT nextval('ctfrontier.study_reference_id_seq'::regclass),
	study_id integer NOT NULL,
	pmid text COLLATE pg_catalog."default",
	reference_type text COLLATE pg_catalog."default",
	citation text COLLATE pg_catalog."default",
	CONSTRAINT study_reference_pkey PRIMARY KEY(study_reference_id),
	CONSTRAINT study_reference_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.study_reference
	OWNER to "postgres";

-- TABLE: ctfrontier.result_agreement
CREATE TABLE ctfrontier.result_agreement
(
	result_agreement_id integer NOT NULL DEFAULT nextval('ctfrontier.result_agreement_id_seq'::regclass),
	study_id integer NOT NULL,
	pi_employee text COLLATE pg_catalog."default",
	agreement text COLLATE pg_catalog."default",
	CONSTRAINT result_agreement_pkey PRIMARY KEY(result_agreement_id),
	CONSTRAINT result_agreement_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.result_agreement
	OWNER to "postgres";

-- TABLE: ctfrontier.pending_result
CREATE TABLE ctfrontier.pending_result
(
	pending_result_id integer NOT NULL DEFAULT nextval('ctfrontier.pending_result_id_seq'::regclass),
	study_id integer NOT NULL,
	event text COLLATE pg_catalog."default",
	event_date_description text COLLATE pg_catalog."default",
	event_date date,
	CONSTRAINT pending_result_pkey PRIMARY KEY(pending_result_id),
	CONSTRAINT pending_result_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.pending_result
	OWNER to "postgres";

-- TABLE: ctfrontier.outcome
CREATE TABLE ctfrontier.outcome
(
	outcome_id integer NOT NULL DEFAULT nextval('ctfrontier.outcome_id_seq'::regclass),
	study_id integer NOT NULL,
	outcome_type text COLLATE pg_catalog."default",
	title text COLLATE pg_catalog."default",
	description text COLLATE pg_catalog."default",
	time_frame text COLLATE pg_catalog."default",
	population text COLLATE pg_catalog."default",
	anticipated_posting_month_year text COLLATE pg_catalog."default",
	anticipated_posting_date date,
	units text COLLATE pg_catalog."default",
	units_analyze text COLLATE pg_catalog."default",
	dispersion_type text COLLATE pg_catalog."default",
	param_type text COLLATE pg_catalog."default",
	CONSTRAINT outcome_pkey PRIMARY KEY(outcome_id),
	CONSTRAINT outcome_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.outcome
	OWNER to "postgres";

-- TABLE: ctfrontier.participant_flow
CREATE TABLE ctfrontier.participant_flow
(
	participant_flow_id integer NOT NULL DEFAULT nextval('ctfrontier.participant_flow_id_seq'::regclass),
	study_id integer NOT NULL,
	pre_assignment_details text COLLATE pg_catalog."default",
	recruitment_details text COLLATE pg_catalog."default",
	CONSTRAINT participant_flow_pkey PRIMARY KEY(participant_flow_id),
	CONSTRAINT participant_flow_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.participant_flow
	OWNER to "postgres";

-- TABLE: ctfrontier.central_contact
CREATE TABLE ctfrontier.central_contact
(
	central_contact_id integer NOT NULL DEFAULT nextval('ctfrontier.central_contact_id_seq'::regclass),
	study_id integer NOT NULL,
	contact_type_id integer NOT NULL,
	name text COLLATE pg_catalog."default",
	phone text COLLATE pg_catalog."default",
	email text COLLATE pg_catalog."default",
	CONSTRAINT central_contact_pkey PRIMARY KEY(central_contact_id),
	CONSTRAINT central_contact_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT central_contact_contact_type_id_fkey FOREIGN KEY (contact_type_id)
		REFERENCES ctfrontier.contact_type (contact_type_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.central_contact
	OWNER to "postgres";

-- TABLE: ctfrontier.study_country
CREATE TABLE ctfrontier.study_country
(
	study_country_id integer NOT NULL DEFAULT nextval('ctfrontier.study_country_id_seq'::regclass),
	country_id integer NOT NULL,
	study_id integer NOT NULL,
	CONSTRAINT study_country_pkey PRIMARY KEY(study_country_id),
	CONSTRAINT study_country_country_id_fkey FOREIGN KEY (country_id)
		REFERENCES ctfrontier.country (country_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT study_country_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.study_country
	OWNER to "postgres";

-- TABLE: ctfrontier.design_group
CREATE TABLE ctfrontier.design_group
(
	design_group_id integer NOT NULL DEFAULT nextval('ctfrontier.design_group_id_seq'::regclass),
	study_id integer NOT NULL,
	group_type_id integer NOT NULL,
	title text COLLATE pg_catalog."default",
	description text COLLATE pg_catalog."default",
	CONSTRAINT design_group_pkey PRIMARY KEY(design_group_id),
	CONSTRAINT design_group_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT design_group_group_type_id_fkey FOREIGN KEY (group_type_id)
		REFERENCES ctfrontier.group_type (group_type_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.design_group
	OWNER to "postgres";

-- TABLE: ctfrontier.design_outcome
CREATE TABLE ctfrontier.design_outcome
(
	design_outcome_id integer NOT NULL DEFAULT nextval('ctfrontier.design_outcome_id_seq'::regclass),
	study_id integer NOT NULL,
	outcome_type_id integer NOT NULL,
	measure text COLLATE pg_catalog."default",
	time_frame text COLLATE pg_catalog."default",
	population text COLLATE pg_catalog."default",
	description text COLLATE pg_catalog."default",
	CONSTRAINT design_outcome_pkey PRIMARY KEY(design_outcome_id),
	CONSTRAINT design_outcome_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT design_outcome_outcome_type_id_fkey FOREIGN KEY (outcome_type_id)
		REFERENCES ctfrontier.outcome_type (outcome_type_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.design_outcome
	OWNER to "postgres";

-- TABLE: ctfrontier.study_facility
CREATE TABLE ctfrontier.study_facility
(
	study_facility_id integer NOT NULL DEFAULT nextval('ctfrontier.study_facility_id_seq'::regclass),
	study_id integer NOT NULL,
	facility_id integer NOT NULL,
	CONSTRAINT study_facility_pkey PRIMARY KEY(study_facility_id),
	CONSTRAINT study_facility_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT study_facility_facility_id_fkey FOREIGN KEY (facility_id)
		REFERENCES ctfrontier.facility (facility_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.study_facility
	OWNER to "postgres";

-- TABLE: ctfrontier.facility_contact
CREATE TABLE ctfrontier.facility_contact
(
	facility_contact_id integer NOT NULL DEFAULT nextval('ctfrontier.facility_contact_id_seq'::regclass),
	study_id integer NOT NULL,
	facility_id integer NOT NULL,
	contact_type text COLLATE pg_catalog."default",
	name text COLLATE pg_catalog."default",
	email text COLLATE pg_catalog."default",
	phone text COLLATE pg_catalog."default",
	CONSTRAINT facility_contact_pkey PRIMARY KEY(facility_contact_id),
	CONSTRAINT facility_contact_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT facility_contact_facility_id_fkey FOREIGN KEY (facility_id)
		REFERENCES ctfrontier.facility (facility_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.facility_contact
	OWNER to "postgres";

-- TABLE: ctfrontier.intervention
CREATE TABLE ctfrontier.intervention
(
	intervention_id integer NOT NULL DEFAULT nextval('ctfrontier.intervention_id_seq'::regclass),
	study_id integer NOT NULL,
	intervention_type_id integer NOT NULL,
	name text COLLATE pg_catalog."default",
	description text COLLATE pg_catalog."default",
	CONSTRAINT intervention_pkey PRIMARY KEY(intervention_id),
	CONSTRAINT intervention_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT intervention_intervention_type_id_fkey FOREIGN KEY (intervention_type_id)
		REFERENCES ctfrontier.intervention_type (intervention_type_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.intervention
	OWNER to "postgres";

-- TABLE: ctfrontier.intervention_other_name
CREATE TABLE ctfrontier.intervention_other_name
(
	intervention_other_name_id integer NOT NULL DEFAULT nextval('ctfrontier.intervention_other_name_id_seq'::regclass),
	study_id integer NOT NULL,
	intervention_id integer NOT NULL,
	name text COLLATE pg_catalog."default",
	CONSTRAINT intervention_other_name_pkey PRIMARY KEY(intervention_other_name_id),
	CONSTRAINT intervention_other_name_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT intervention_other_name_intervention_id_fkey FOREIGN KEY (intervention_id)
		REFERENCES ctfrontier.intervention (intervention_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.intervention_other_name
	OWNER to "postgres";

-- TABLE: ctfrontier.overall_official
CREATE TABLE ctfrontier.overall_official
(
	overall_official_id integer NOT NULL DEFAULT nextval('ctfrontier.overall_official_id_seq'::regclass),
	study_id integer NOT NULL,
	role text COLLATE pg_catalog."default",
	name text COLLATE pg_catalog."default",
	affiliate_id integer NOT NULL,
	CONSTRAINT overall_official_pkey PRIMARY KEY(overall_official_id),
	CONSTRAINT overall_official_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT overall_official_affiliate_id_fkey FOREIGN KEY (affiliate_id)
		REFERENCES ctfrontier.affiliate (affiliate_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.overall_official
	OWNER to "postgres";

-- TABLE: ctfrontier.result_contact
CREATE TABLE ctfrontier.result_contact
(
	result_contact_id integer NOT NULL DEFAULT nextval('ctfrontier.result_contact_id_seq'::regclass),
	study_id integer NOT NULL,
	organization_id integer NOT NULL,
	name text COLLATE pg_catalog."default",
	phone text COLLATE pg_catalog."default",
	email text COLLATE pg_catalog."default",
	CONSTRAINT result_contact_pkey PRIMARY KEY(result_contact_id),
	CONSTRAINT result_contact_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT result_contact_organization_id_fkey FOREIGN KEY (organization_id)
		REFERENCES ctfrontier.organization (organization_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.result_contact
	OWNER to "postgres";

-- TABLE: ctfrontier.outcome_analysis
CREATE TABLE ctfrontier.outcome_analysis
(
	outcome_analysis_id integer NOT NULL DEFAULT nextval('ctfrontier.outcome_analysis_id_seq'::regclass),
	study_id integer NOT NULL,
	outcome_id integer NOT NULL,
	non_inferiority_type text COLLATE pg_catalog."default",
	non_inferiority_description text COLLATE pg_catalog."default",
	param_type text COLLATE pg_catalog."default",
	param_value decimal,
	dispersion_type text COLLATE pg_catalog."default",
	dispersion_value decimal,
	p_value double precision,
	p_value_modifier text COLLATE pg_catalog."default",
	ci_n_sides text COLLATE pg_catalog."default",
	ci_percent decimal,
	ci_lower_limit decimal,
	ci_upper_limit decimal,
	ci_upper_limit_na_comment text COLLATE pg_catalog."default",
	p_value_description text COLLATE pg_catalog."default",
	method text COLLATE pg_catalog."default",
	method_description text COLLATE pg_catalog."default",
	estimate_description text COLLATE pg_catalog."default",
	other_analysis_description text COLLATE pg_catalog."default",
	groups_description text COLLATE pg_catalog."default",
	CONSTRAINT outcome_analysis_pkey PRIMARY KEY(outcome_analysis_id),
	CONSTRAINT outcome_analysis_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT outcome_analysis_outcome_id_fkey FOREIGN KEY (outcome_id)
		REFERENCES ctfrontier.outcome (outcome_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.outcome_analysis
	OWNER to "postgres";

-- TABLE: ctfrontier.facility_investigator
CREATE TABLE ctfrontier.facility_investigator
(
	facility_investigator_id integer NOT NULL DEFAULT nextval('ctfrontier.facility_investigator_id_seq'::regclass),
	study_id integer NOT NULL,
	facility_id integer NOT NULL,
	facility_role_id integer NOT NULL,
	name text COLLATE pg_catalog."default",
	CONSTRAINT facility_investigator_pkey PRIMARY KEY(facility_investigator_id),
	CONSTRAINT facility_investigator_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT facility_investigator_facility_id_fkey FOREIGN KEY (facility_id)
		REFERENCES ctfrontier.facility (facility_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT facility_investigator_facility_role_id_fkey FOREIGN KEY (facility_role_id)
		REFERENCES ctfrontier.facility_role (facility_role_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.facility_investigator
	OWNER to "postgres";

-- TABLE: ctfrontier.result_group
CREATE TABLE ctfrontier.result_group
(
	result_group_id integer NOT NULL DEFAULT nextval('ctfrontier.result_group_id_seq'::regclass),
	study_id integer NOT NULL,
	group_code_id integer NOT NULL,
	result_type_id integer NOT NULL,
	title text COLLATE pg_catalog."default",
	description text COLLATE pg_catalog."default",
	CONSTRAINT result_group_pkey PRIMARY KEY(result_group_id),
	CONSTRAINT result_group_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT result_group_group_code_id_fkey FOREIGN KEY (group_code_id)
		REFERENCES ctfrontier.group_code (group_code_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT result_group_result_type_id_fkey FOREIGN KEY (result_type_id)
		REFERENCES ctfrontier.result_type (result_type_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.result_group
	OWNER to "postgres";

-- TABLE: ctfrontier.baseline_count
CREATE TABLE ctfrontier.baseline_count
(
	baseline_count_id integer NOT NULL DEFAULT nextval('ctfrontier.baseline_count_id_seq'::regclass),
	study_id integer NOT NULL,
	result_group_id integer NOT NULL,
	group_code_id integer NOT NULL,
	units text COLLATE pg_catalog."default",
	scope text COLLATE pg_catalog."default",
	count integer,
	CONSTRAINT baseline_count_pkey PRIMARY KEY(baseline_count_id),
	CONSTRAINT baseline_count_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT baseline_count_result_group_id_fkey FOREIGN KEY (result_group_id)
		REFERENCES ctfrontier.result_group (result_group_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT baseline_count_group_code_id_fkey FOREIGN KEY (group_code_id)
		REFERENCES ctfrontier.group_code (group_code_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.baseline_count
	OWNER to "postgres";

-- TABLE: ctfrontier.reported_event
CREATE TABLE ctfrontier.reported_event
(
	reported_event_id integer NOT NULL DEFAULT nextval('ctfrontier.reported_event_id_seq'::regclass),
	study_id integer NOT NULL,
	result_group_id integer NOT NULL,
	group_code_id integer NOT NULL,
	time_frame text COLLATE pg_catalog."default",
	event_type text COLLATE pg_catalog."default",
	default_vocab text COLLATE pg_catalog."default",
	default_assessment text COLLATE pg_catalog."default",
	subjects_affected integer,
	subjects_at_risk integer,
	description text COLLATE pg_catalog."default",
	event_count integer,
	organ_system text COLLATE pg_catalog."default",
	adverse_event_term text COLLATE pg_catalog."default",
	frequency_threshold integer,
	vocab text COLLATE pg_catalog."default",
	assessment text COLLATE pg_catalog."default",
	CONSTRAINT reported_event_pkey PRIMARY KEY(reported_event_id),
	CONSTRAINT reported_event_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT reported_event_result_group_id_fkey FOREIGN KEY (result_group_id)
		REFERENCES ctfrontier.result_group (result_group_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT reported_event_group_code_id_fkey FOREIGN KEY (group_code_id)
		REFERENCES ctfrontier.group_code (group_code_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.reported_event
	OWNER to "postgres";

-- TABLE: ctfrontier.milestone
CREATE TABLE ctfrontier.milestone
(
	milestone_id integer NOT NULL DEFAULT nextval('ctfrontier.milestone_id_seq'::regclass),
	study_id integer NOT NULL,
	result_group_id integer NOT NULL,
	group_code_id integer NOT NULL,
	period text COLLATE pg_catalog."default",
	title text COLLATE pg_catalog."default",
	description text COLLATE pg_catalog."default",
	count integer,
	CONSTRAINT milestone_pkey PRIMARY KEY(milestone_id),
	CONSTRAINT milestone_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT milestone_result_group_id_fkey FOREIGN KEY (result_group_id)
		REFERENCES ctfrontier.result_group (result_group_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT milestone_group_code_id_fkey FOREIGN KEY (group_code_id)
		REFERENCES ctfrontier.group_code (group_code_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.milestone
	OWNER to "postgres";

-- TABLE: ctfrontier.drop_withdrawal
CREATE TABLE ctfrontier.drop_withdrawal
(
	drop_withdrawal_id integer NOT NULL DEFAULT nextval('ctfrontier.drop_withdrawal_id_seq'::regclass),
	study_id integer NOT NULL,
	result_group_id integer NOT NULL,
	group_code_id integer NOT NULL,
	period text COLLATE pg_catalog."default",
	reason text COLLATE pg_catalog."default",
	count integer,
	CONSTRAINT drop_withdrawal_pkey PRIMARY KEY(drop_withdrawal_id),
	CONSTRAINT drop_withdrawal_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT drop_withdrawal_result_group_id_fkey FOREIGN KEY (result_group_id)
		REFERENCES ctfrontier.result_group (result_group_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT drop_withdrawal_group_code_id_fkey FOREIGN KEY (group_code_id)
		REFERENCES ctfrontier.group_code (group_code_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.drop_withdrawal
	OWNER to "postgres";

-- TABLE: ctfrontier.responsible_party
CREATE TABLE ctfrontier.responsible_party
(
	responsible_party_id integer NOT NULL DEFAULT nextval('ctfrontier.responsible_party_id_seq'::regclass),
	study_id integer NOT NULL,
	responsible_party_type_id integer NOT NULL,
	name text COLLATE pg_catalog."default",
	title text COLLATE pg_catalog."default",
	organization_id integer NOT NULL,
	affiliate_id integer NOT NULL,
	CONSTRAINT responsible_party_pkey PRIMARY KEY(responsible_party_id),
	CONSTRAINT responsible_party_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT responsible_party_responsible_party_type_id_fkey FOREIGN KEY (responsible_party_type_id)
		REFERENCES ctfrontier.responsible_party_type (responsible_party_type_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT responsible_party_organization_id_fkey FOREIGN KEY (organization_id)
		REFERENCES ctfrontier.organization (organization_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT responsible_party_affiliate_id_fkey FOREIGN KEY (affiliate_id)
		REFERENCES ctfrontier.affiliate (affiliate_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.responsible_party
	OWNER to "postgres";

-- TABLE: ctfrontier.outcome_analysis_group
CREATE TABLE ctfrontier.outcome_analysis_group
(
	outcome_analysis_group_id integer NOT NULL DEFAULT nextval('ctfrontier.outcome_analysis_group_id_seq'::regclass),
	study_id integer NOT NULL,
	outcome_analysis_id integer NOT NULL,
	result_group_id integer NOT NULL,
	group_code_id integer NOT NULL,
	CONSTRAINT outcome_analysis_group_pkey PRIMARY KEY(outcome_analysis_group_id),
	CONSTRAINT outcome_analysis_group_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT outcome_analysis_group_outcome_analysis_id_fkey FOREIGN KEY (outcome_analysis_id)
		REFERENCES ctfrontier.outcome_analysis (outcome_analysis_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT outcome_analysis_group_result_group_id_fkey FOREIGN KEY (result_group_id)
		REFERENCES ctfrontier.result_group (result_group_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT outcome_analysis_group_group_code_id_fkey FOREIGN KEY (group_code_id)
		REFERENCES ctfrontier.group_code (group_code_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.outcome_analysis_group
	OWNER to "postgres";

-- TABLE: ctfrontier.outcome_count
CREATE TABLE ctfrontier.outcome_count
(
	outcome_count_id integer NOT NULL DEFAULT nextval('ctfrontier.outcome_count_id_seq'::regclass),
	study_id integer NOT NULL,
	outcome_id integer NOT NULL,
	result_group_id integer NOT NULL,
	group_code_id integer NOT NULL,
	scope text COLLATE pg_catalog."default",
	units text COLLATE pg_catalog."default",
	count integer,
	CONSTRAINT outcome_count_pkey PRIMARY KEY(outcome_count_id),
	CONSTRAINT outcome_count_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT outcome_count_outcome_id_fkey FOREIGN KEY (outcome_id)
		REFERENCES ctfrontier.outcome (outcome_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT outcome_count_result_group_id_fkey FOREIGN KEY (result_group_id)
		REFERENCES ctfrontier.result_group (result_group_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT outcome_count_group_code_id_fkey FOREIGN KEY (group_code_id)
		REFERENCES ctfrontier.group_code (group_code_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.outcome_count
	OWNER to "postgres";

-- TABLE: ctfrontier.baseline_measurement
CREATE TABLE ctfrontier.baseline_measurement
(
	baseline_measurement_id integer NOT NULL DEFAULT nextval('ctfrontier.baseline_measurement_id_seq'::regclass),
	study_id integer NOT NULL,
	result_group_id integer NOT NULL,
	group_code_id integer NOT NULL,
	classification_id integer NOT NULL,
	category_id integer NOT NULL,
	units text COLLATE pg_catalog."default",
	title text COLLATE pg_catalog."default",
	description text COLLATE pg_catalog."default",
	param_type text COLLATE pg_catalog."default",
	param_value text COLLATE pg_catalog."default",
	param_value_num decimal,
	dispersion_type text COLLATE pg_catalog."default",
	dispersion_value text COLLATE pg_catalog."default",
	dispersion_value_num decimal,
	dispersion_lower_limit decimal,
	dispersion_upper_limit decimal,
	explanation_of_na text COLLATE pg_catalog."default",
	CONSTRAINT baseline_measurement_pkey PRIMARY KEY(baseline_measurement_id),
	CONSTRAINT baseline_measurement_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT baseline_measurement_result_group_id_fkey FOREIGN KEY (result_group_id)
		REFERENCES ctfrontier.result_group (result_group_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT baseline_measurement_group_code_id_fkey FOREIGN KEY (group_code_id)
		REFERENCES ctfrontier.group_code (group_code_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT baseline_measurement_classification_id_fkey FOREIGN KEY (classification_id)
		REFERENCES ctfrontier.classification (classification_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT baseline_measurement_category_id_fkey FOREIGN KEY (category_id)
		REFERENCES ctfrontier.category (category_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.baseline_measurement
	OWNER to "postgres";

-- TABLE: ctfrontier.outcome_measurement
CREATE TABLE ctfrontier.outcome_measurement
(
	outcome_measurement_id integer NOT NULL DEFAULT nextval('ctfrontier.outcome_measurement_id_seq'::regclass),
	study_id integer NOT NULL,
	outcome_id integer NOT NULL,
	result_group_id integer NOT NULL,
	group_code_id integer NOT NULL,
	classification_id integer NOT NULL,
	category_id integer NOT NULL,
	title text COLLATE pg_catalog."default",
	description text COLLATE pg_catalog."default",
	units text COLLATE pg_catalog."default",
	param_type text COLLATE pg_catalog."default",
	param_value text COLLATE pg_catalog."default",
	param_value_num decimal,
	dispersion_type text COLLATE pg_catalog."default",
	dispersion_value text COLLATE pg_catalog."default",
	dispersion_value_num decimal,
	dispersion_lower_limit decimal,
	dispersion_upper_limit decimal,
	explanation_of_na text COLLATE pg_catalog."default",
	CONSTRAINT outcome_measurement_pkey PRIMARY KEY(outcome_measurement_id),
	CONSTRAINT outcome_measurement_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT outcome_measurement_outcome_id_fkey FOREIGN KEY (outcome_id)
		REFERENCES ctfrontier.outcome (outcome_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT outcome_measurement_result_group_id_fkey FOREIGN KEY (result_group_id)
		REFERENCES ctfrontier.result_group (result_group_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT outcome_measurement_group_code_id_fkey FOREIGN KEY (group_code_id)
		REFERENCES ctfrontier.group_code (group_code_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT outcome_measurement_classification_id_fkey FOREIGN KEY (classification_id)
		REFERENCES ctfrontier.classification (classification_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT outcome_measurement_category_id_fkey FOREIGN KEY (category_id)
		REFERENCES ctfrontier.category (category_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.outcome_measurement
	OWNER to "postgres";

-- TABLE: ctfrontier.design
CREATE TABLE ctfrontier.design
(
	design_id integer NOT NULL DEFAULT nextval('ctfrontier.design_id_seq'::regclass),
	study_id integer NOT NULL,
	primary_purpose_id integer NOT NULL,
	intervention_model_id integer NOT NULL,
	observational_model_id integer NOT NULL,
	allocation_model_id integer NOT NULL,
	time_perspective_id integer NOT NULL,
	masking_id integer NOT NULL,
	intervention_model_description text COLLATE pg_catalog."default",
	masking_description text COLLATE pg_catalog."default",
	subject_masked boolean,
	caregiver_masked boolean,
	investigator_masked boolean,
	outcomes_assessor_masked boolean,
	CONSTRAINT design_pkey PRIMARY KEY(design_id),
	CONSTRAINT design_study_id_fkey FOREIGN KEY (study_id)
		REFERENCES ctfrontier.study (study_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT design_primary_purpose_id_fkey FOREIGN KEY (primary_purpose_id)
		REFERENCES ctfrontier.primary_purpose (primary_purpose_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT design_intervention_model_id_fkey FOREIGN KEY (intervention_model_id)
		REFERENCES ctfrontier.intervention_model (intervention_model_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT design_observational_model_id_fkey FOREIGN KEY (observational_model_id)
		REFERENCES ctfrontier.observational_model (observational_model_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT design_allocation_model_id_fkey FOREIGN KEY (allocation_model_id)
		REFERENCES ctfrontier.allocation_model (allocation_model_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT design_time_perspective_id_fkey FOREIGN KEY (time_perspective_id)
		REFERENCES ctfrontier.time_perspective (time_perspective_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION,
	CONSTRAINT design_masking_id_fkey FOREIGN KEY (masking_id)
		REFERENCES ctfrontier.masking (masking_id) MATCH SIMPLE
		ON UPDATE NO ACTION
		ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE ctfrontier.design
	OWNER to "postgres";

