DROP VIEW IF EXISTS basic_search;
DROP MATERIALIZED VIEW IF EXISTS basic_search_m;
DROP MATERIALIZED VIEW IF EXISTS search_studies;
DROP VIEW IF EXISTS all_sponsors_type;
DROP MATERIALIZED VIEW IF EXISTS all_sponsors_type;
DROP VIEW IF EXISTS all_documents;
DROP MATERIALIZED VIEW IF EXISTS all_documents;

DROP TABLE IF EXISTS ctgov.etl;

CREATE TABLE ctgov.etl
(
    last_run_date date,
    insert_current_offset integer Default(0),
    insert_max_rows integer Default(0),
    update_current_offset integer Default(0),
    update_max_rows integer Default(0)
)

TABLESPACE pg_default;

ALTER TABLE ctgov.etl
    OWNER to postgres;

INSERT INTO ctgov.etl(last_run_date)
SELECT CAST (max(created_at) AS date) + 1
FROM ctgov.studies;


CREATE MATERIALIZED VIEW ctgov.all_sponsors_type
TABLESPACE pg_default
AS
 SELECT sponsors.nct_id,
    array_to_string(array_agg(DISTINCT sponsors.agency_class), '|'::text) AS funder_type,
    array_to_string(array_agg(DISTINCT sponsors.name), '|'::text) AS names
   FROM ctgov.sponsors
  GROUP BY sponsors.nct_id
WITH DATA;

ALTER TABLE ctgov.all_sponsors_type
    OWNER TO postgres;

CREATE INDEX all_sponsors_nct_idx
    ON ctgov.all_sponsors_type USING btree
    (nct_id COLLATE pg_catalog."default")
    TABLESPACE pg_default;


CREATE MATERIALIZED VIEW ctgov.all_documents AS
SELECT
	documents.nct_id,
	array_to_string(array_agg(DISTINCT document_type), '|'::text) AS document_types
FROM ctgov.documents
GROUP BY documents.nct_id;

CREATE INDEX all_documents_nct_idx
    ON ctgov.documents USING btree
    (nct_id COLLATE pg_catalog."default")
    TABLESPACE pg_default;


CREATE MATERIALIZED VIEW ctgov.search_studies AS
SELECT 
	A.overall_status status, 
	A.brief_title, 
	A.official_title,
	A.nct_id,
	B.names condition_name,
	C.description study_detailed_desc, 
	D.names country_name,
	E.names intervention_name, 
	F.names keywords,
	G.criteria eligibility_criteria,
	G.gender eligibility_gender,
	G.minimum_age eligibility_min_age,
	(case 
	when G.minimum_age like '%Months%' 
		then round(cast(trim(G.minimum_age,' Months') as decimal)/ 12,2) 
	when G.minimum_age like '%Days%'
		then round(cast(trim(G.minimum_age,' Days') as decimal)/ (30*12),2)
	when G.minimum_age like '%Weeks%'
		then round(cast(trim(G.minimum_age,' Weeks') as decimal)/ (4*12),2) 
	when G.minimum_age like '%Years%'
		then round(cast(trim(G.minimum_age,' Years') as decimal),0)  
	else 0 end) eligibility_min_age_numeric,
	G.maximum_age eligibility_max_age,
	(case 
	when G.maximum_age like '%Months%' 
		then round(cast(trim(G.maximum_age,' Months') as decimal)/ 12,2) 
	when G.maximum_age like '%Days%'
		then round(cast(trim(G.maximum_age,' Days') as decimal)/ (30*12),2)
	when G.maximum_age like '%Weeks%'
		then round(cast(trim(G.maximum_age,' Weeks') as decimal)/ (4*12),2) 
	when G.maximum_age like '%Years%'
		then round(cast(trim(G.maximum_age,' Years') as decimal),0)  
	else 0 end) eligibility_max_age_numeric,

	G.healthy_volunteers,
	H.names location_name,
	I.description study_brief_desc,
	J.names sponsor_name,
	J.funder_type,
	A.phase study_phase,
	A.start_date study_start_date,
	A.primary_completion_date,
	A.study_first_posted_date,
	A.results_first_posted_date,
	A.last_update_posted_date,
	A.study_type,
	K.names primary_outcome_measures,
	L.names secondary_outcome_measures,
	M.names study_ids,
	N.document_types,
	A.is_unapproved_device,
	A.results_first_submitted_qc_date results_submitted_qc_not_done,
	A.results_first_posted_date results_submitted_qc_done,
	A.acronym,
	O.names city_name,
	P.names state_name
FROM 
	ctgov.studies A
LEFT JOIN ctgov.all_conditions B
	ON A.nct_id = B.nct_id
LEFT JOIN ctgov.detailed_descriptions C
	ON A.nct_id = C.nct_id
LEFT JOIN ctgov.all_countries D
	ON A.nct_id = D.nct_id
LEFT JOIN ctgov.all_interventions E
	ON A.nct_id = E.nct_id
LEFT JOIN all_keywords F
	ON A.nct_id = F.nct_id
LEFT JOIN eligibilities G
	ON A.nct_id = G.nct_id
LEFT JOIN all_facilities H
	ON A.nct_id = H.nct_id
LEFT JOIN brief_summaries I
	ON A.nct_id = I.nct_id
LEFT JOIN all_sponsors_type J
	ON A.nct_id = J.nct_id
LEFT JOIN all_primary_outcome_measures K
	ON A.nct_id = K.nct_id
LEFT JOIN all_secondary_outcome_measures L
	ON A.nct_id = L.nct_id
LEFT JOIN all_id_information M
	ON A.nct_id = M.nct_id
LEFT JOIN all_documents N
	ON A.nct_id = N.nct_id
LEFT JOIN all_cities O
	ON A.nct_id = O.nct_id
LEFT JOIN all_states P
	ON A.nct_id = P.nct_id
ORDER BY A.start_date;

CREATE INDEX search_studies_optimize_idx
    ON ctgov.search_studies USING btree
	(study_start_date ASC NULLS LAST,
	 nct_id ASC NULLS LAST
	)
INCLUDE (status, brief_title, official_title, nct_id)
	TABLESPACE pg_default;
