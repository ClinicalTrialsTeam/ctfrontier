CREATE VIEW basic_search AS
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
	H.names location_name,
	I.description study_brief_desc
FROM 
	studies A
LEFT JOIN all_conditions B
	ON A.nct_id = B.nct_id
LEFT JOIN detailed_descriptions C
	ON A.nct_id = C.nct_id
LEFT JOIN all_countries D
	ON A.nct_id = D.nct_id
LEFT JOIN all_interventions E
	ON A.nct_id = E.nct_id
LEFT JOIN all_keywords F
	ON A.nct_id = F.nct_id
LEFT JOIN eligibilities G
	ON A.nct_id = G.nct_id
LEFT JOIN all_facilities H
	ON A.nct_id = H.nct_id
LEFT JOIN brief_summaries I
	ON A.nct_id = I.nct_id
ORDER BY A.start_date