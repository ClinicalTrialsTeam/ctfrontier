## API Endpoints

### Clinical Studies Search API
#### Parameters

The end point for Clinical Studies Search API is:
<http://127.0.0.1:8000/ctgov/api/search_studies>

#### If metadata is required, pass "metadata_required"="True"; if metadata is not required (for example, during pagination) pass empty string as "metadata_required="".

Example query located in `database/examples/search_studies_query.json`:

	{
		"status":["Recruiting", "Completed", "Active, not recruiting"],
		"condition":"",
		"other_terms":"",
		"country":"",
		"intervention":"",
		"target":"",
		"nct_id":"",
		"eligibility_criteria":"",
		"modality":"",
		"sponsor":"",
		"phase":["Phase 1", "Phase 2", "Phase 3"],
		"start_date_from":"2019-01-01",
		"start_date_to":"2020-01-01",
		"primary_completion_date_from":"",
		"primary_completion_date_to":"",
		"first_posted_date_from":"",
		"first_posted_date_to":"",
		"results_first_posted_date_from":"",
		"results_first_posted_date_to":"",
		"last_update_posted_date_from":"",
		"last_update_posted_date_to":"",
		"study_results":"",
		"study_type":"",
		"eligibility_age":"",
		"eligibility_age_group": ["child", "adult", "older adult"],
		"eligibility_gender":"",
		"eligibility_ethnicity": ["White / Caucasian", "Hispanic or Latino"],
		"eligibility_condition":"",
		"eligibility_healthy_volunteer":"",
		"study_title_acronym":"",
		"study_outcome_measure":"",
		"study_collaborator":"",
		"study_ids":"",
		"study_location_terms":"",
		"study_funder_type":"",
		"study_document_type":"",
		"study_results_submitted":"",
		"study_roa":["Oral", "Intradermal", "Intravenous"],
		"condition_terms":"",
		"city":"",
		"state":"",
		"first":"",
		"last":"",
		"metadata_required":"True"
	}


1. Pass all of the above 'post' parameters with exact name. You can choose to pass only those parameters that have value entered/selected by user. You don't need to pass all parameters. If none of the parameters are passed, the API will get first 100 records from database.

1. 'first' and 'last' parameters are for pagination. If these parameters are blank or not passed, Django API will assume first = 0 and last = 100.

Example curl command with a timer using the example json:

`time curl -X POST http://127.0.0.1:8000/ctgov/api/search_studies -d database/examples/search_studies_query.json`

#### Output

#### Please note search results now contains "metadata" information. This means ReactJS parsing needs to be modified accordingly.

Sample result below. Note that 'intervention_name' and 'location_name' are pipe delimited values. You have to parse them to display as a list in html.


	{
		"metadata": [
			{
				"results_count": "148"
			}
		],
		"search_results": [
			{
				"status": "Completed",
				"brief_title": "Combination Chemotherapy, Bone Marrow Transplantation, and 	Radiation Therapy in Treating Infants With Acute Lymphoblastic Leukemia",
				"nct_id": "NCT00002785",
				"condition_name": "Leukemia",
				"intervention_name": "filgrastim|asparaginase|cyclophosphamide|cyclosporine|cytarabine|daunorubicin hydrochloride|dexamethasone|etoposide|leucovorin calcium|mercaptopurine|mesna|methotrexate|methylprednisolone|pegaspargase|prednisone|therapeutic hydrocortisone|vincristine sulfate|allogeneic bone marrow transplantation|low-LET cobalt-60 gamma ray therapy|low-LET photon therapy",
				"location_name": "Long Beach Memorial Medical Center|Children's Hospital Los Angeles|Jonsson Comprehensive Cancer Center, UCLA|Children's Hospital of Orange County|UCSF Cancer Center and Cancer Research Institute|Children's Hospital of Denver|Children's National Medical Center|University of Chicago Cancer Research Center|Indiana University Cancer Center|University of Iowa Hospitals and Clinics|University of Michigan Comprehensive Cancer Center|University of Minnesota Cancer Center|Mayo Clinic Cancer Center|Children's Mercy Hospital - Kansas City|University of Nebraska Medical Center|Kaplan Cancer Center|Memorial Sloan-Kettering Cancer Center|Herbert Irving Comprehensive Cancer Center|Lineberger Comprehensive Cancer Center, UNC|Children's Hospital Medical Center - Cincinnati|Ireland Cancer Center|Children's Hospital of Columbus|Doernbecher Children's Hospital|Children's Hospital of Philadelphia|Children's Hospital of Pittsburgh|Vanderbilt Cancer Center|University of Texas - MD Anderson Cancer Center|Huntsman Cancer Institute|Children's Hospital and Regional Medical Center - Seattle|University of Wisconsin Comprehensive Cancer Center|Princess Margaret Hospital for Children|British Columbia Children's Hospital|IWK Grace Health Centre",
				"study_phase": "Phase 2",
				"sponsor_name": "Children's Oncology Group|National Cancer Institute (NCI)",
				"study_brief_desc": "\n      RATIONALE: Drugs used in chemotherapy use different ways to stop cancer cells from dividing\r\n      so they stop growing or die. Combining more than one drug may kill more cancer cells. Bone\r\n      marrow transplantation may allow the doctor to give higher doses of chemotherapy and kill\r\n      more cancer cells. Radiation therapy uses high-energy x-rays to damage cancer cells.\r\n\r\n      PURPOSE: Phase II trial to study the effectiveness of combination chemotherapy, bone marrow\r\n      transplantation, and radiation therapy in treating infants with acute lymphoblastic leukemia.\r\n    ",
				"primary_outcome_measures": "Event Free Survival",
				"secondary_outcome_measures": null,
				"study_start_date": "2016-09-30",
				"primary_completion_date": "2018-04-30"
			},
			{
				"status": "Completed",
				"brief_title": "Antineoplaston Therapy in Treating Children With Low-Grade Astrocytoma",
				"nct_id": "NCT00003468",
				"condition_name": "Low Grade Astrocytomas",
				"intervention_name": "Antineoplaston therapy (Atengenal + Astugenal)",
				"location_name": "Burzynski Clinic",
				"study_phase": "Phase 2",
				"sponsor_name": "Burzynski Research Institute",
				"study_brief_desc": "\n      RATIONALE: Current therapies for children with low grade astrocytomas that have not responded\r\n      to standard therapy provide limited benefit to the patient. The anti-cancer properties of\r\n      Antineoplaston therapy suggest that it may prove beneficial in the treatment of children with\r\n      low grade astrocytomas that have not responded to standard therapy\r\n\r\n      PURPOSE: This study is being performed to determine the effects (good and bad) that\r\n      Antineoplaston therapy has on children (> 6 months of age) with low grade astrocytomas that\r\n      has not responded to standard therapy.\r\n    ",
				"primary_outcome_measures": "Number of Participants With Objective Response",
				"secondary_outcome_measures": "Percentage of Participants Who Survived",
				"study_start_date": "2016-09-30",
				"primary_completion_date": "2021-01-31"
			},
			{
				"status": "Completed",
				"brief_title": "Study of a-Interferon With Adriamycin, Bleomycin, Velban, and Dacarbazine (ABVD) With Hodgkin's Disease",
				"nct_id": "NCT01404936",
				"condition_name": "Lymphoma",
				"intervention_name": "Interferon-2A|Adriamycin|Bleomycin|Velban|Dacarbazine",
				"location_name": "UT MD Anderson Cancer Center",
				"study_phase": "Phase 2",
				"sponsor_name": "M.D. Anderson Cancer Center|Schering-Plough",
				"study_brief_desc": "\n      This is a clinical research study of interferon (IFN) plus chemotherapy with the standard\r\n      combination of Adriamycin, Bleomycin, Velban, and Dacarbazine (ABVD). The treatment will be\r\n      given to patients with Hodgkin's disease. The study will look at whether adding IFN to ABVD\r\n      improves the immune response against Hodgkin's disease, and will determine whether the\r\n      toxicity of ABVD is increased by adding IFN.\r\n    ",
				"primary_outcome_measures": "Participants' Response",
				"secondary_outcome_measures": null,
				"study_start_date": "2016-09-30",
				"primary_completion_date": "2017-09-01"
			}	
		]
	}

### Countries API

The end point for Countries API is:
<http://127.0.0.1:8000/ctgov/api/countries>

Countries API will return a unique list of countries associated with studies in the following format.

	[
	    {
	        "name": "Afghanistan"
	    },
	    {
	        "name": "Albania"
	    },
	    {
	        "name": "Algeria"
	    },
	    {
	        "name": "American Samoa"
	    },
	    {
	        "name": "Andorra"
	    },
	    {
	        "name": "Angola"
	    },
	    {
	        "name": "Antarctica"
	    }
	    {
	        ...
	    }
	]

### Conditions API

The end point for Countries API is:
<http://127.0.0.1:8000/ctgov/api/conditions>

Conditions API will return unique list of conditions associated with clinical trials in the following format.

	[
		{
			"mesh_term": "22q11 Deletion Syndrome"
		},
		{
			"mesh_term": "Abdomen, Acute"
		},
		{
			"mesh_term": "Abdominal Abscess"
		},
		{
			"mesh_term": "Abdominal Injuries"
		},
		{
			"mesh_term": "Abdominal Neoplasms"
		},
		{
			"mesh_term": "Abdominal Pain"
		},
		{
			...
		}
	]

### States API

The end point for States API is:
<http://127.0.0.1:8000/ctgov/api/states>

States API will return unique list of states in USA that are associated with clinical trials facilities in the following format.

	[
		{
			"state": "Alabama"
		},
		{
			"state": "Alaska"
		},
		{
			"state": "Arizona"
		},
		{
			"state": "Arkansas"
		},
		{
			"state": "California"
		},
		{
			"state": "Colorado"
		},
		{
			"state": "Connecticut"
		},
		{
			"state": "Delaware"
		},
		{
			...
		}
	]


### Cities API

The end point for Cities API is:
<http://127.0.0.1:8000/ctgov/api/cities>

Cities API will return unique list of cities associated with clinical trials facilities in the following format

	[
		{
			"city": "서울시"
		},
		{
			"city": "성북구"
		},
		{
			"city": "전주시"
		},
		{
			"city": "£ód?"
		},
		{
			"city": "£ódx"
		},
		{
			"city": "02-791 Warszawa"
		},
		{
			"city": "1000 Brussels"
		},
		{
			"city": "1007,Shimonagakubo,Nagaizumi-cho,Sunto-gun"
		},
		{
			"city": "10230 142 St Nw # 25, Edmonton"
		},
		{
			"city": "#108 3947 50A Avenue"
		},
		{
			"city": "10 Siqueirosa str., St. Petersburg"
		},
		{
			...
		}
	]

### Study Detail API

The endpoint for Study Detail API is:
http://localhost:8000/ctgov/api/study_detail

Study Detail API will return details of a single clinical study corresponding to the NCT number passed as API parameter

Example query located in `database/examples/study_detail_query.json`:
The POST request to the API should be as below.

	{
		"nct_id": "NCT03142139"
	}

#### Output

Sample result of Study Detail API is given below.

	[
		{
			"nct_id": "NCT03142139",
			"brief_title": "Does Timeliness of DTaP-IPV-Hib Vaccination Affect Development of Atopic Dermatitis Before 1 Year of Age?",
			"official_title": "Timing of Vaccination With the Non-live DTaP-IPV-Hib Vaccine and Development of Atopic Dermatitis Before 1 Year of Age - a Danish Register Based Cohort Study",
			"study_brief_desc": "\n      It has been found that the non-live vaccine against Diphtheria, Tetanus, and Pertussis (DTP)\r\n      in addition to its disease specific effects may have so called \"non-specific effects\" with\r\n      the potential to affect sensitivity towards vaccine unrelated pathogens, resulting in excess\r\n      mortality(Aaby, Kollmann, & Benn, 2014).\r\n\r\n      A recent study from Australia found that delayed vaccination with the first dose of\r\n      Diphtheria, Tetanus, and acellular Pertussis(DTaP)-containing vaccine is associated with\r\n      reduced risk of atopic dermatitis (aOR: 0.57; 95% CI: 0.34-0.97, P = 0.04) and reduced use of\r\n      medication against atopic dermatitis (aOR: 0.45; 95% CI: 0.24-0.83, P = 0.01)(Kiraly et al.,\r\n      2016).\r\n\r\n      This register based observational study aims to extend the existing knowledge on non-specific\r\n      effects of non-live vaccines by testing the above finding, that delayed vaccination with\r\n      Diphtheria, Tetanus, acellular Pertussis - Inactivated Polio vaccine - Haemophilus influenzae\r\n      type b (DTaP-IPV-Hib) is associated with lower risk of developing atopic dermatitis before 1\r\n      year of age in the Danish birth cohorts from 1997-2012.\r\n    ",
			"study_detailed_desc": "\n      It has been found that the non-live vaccine against Diphtheria, Tetanus, and Pertussis (DTP)\r\n      in addition to its disease specific effects may have so called non-specific effects with the\r\n      potential to affect resistance towards vaccine unrelated pathogens, resulting in excess\r\n      mortality and morbidity(Aaby et al., 2014). These immunomodifying effects may affect\r\n      development of atopic dermatitis through increased immunological sensitivity(Nilsson, Gruber,\r\n      Granstrom, Bjorksten, & Kjellman, 1998). A recent study from Australia found that delayed\r\n      vaccination with the first dose of Diphtheria, Tetanus, and acellular\r\n      Pertussis(DTaP)-containing vaccine is associated with reduced eczema (aOR: 0.57; 95% CI:\r\n      0.34-0.97, P = 0.04) and reduced use of medication against atopic dermatitis (aOR: 0.45; 95%\r\n      CI: 0.24-0.83, P = 0.01)(Kiraly et al., 2016). The present study aims to test the above\r\n      finding and investigate the effect of timeliness of vaccination with DTaP-IPV-Hib (with or\r\n      without PCV) on development of atopic dermatitis before 1 year of age among Danish children\r\n      born between 1997 and 2012. From 1997 to 2012 children in Denmark were scheduled to receive\r\n      the 1st, 2nd, and 3rd dose of DTaP-IPV-Hib at 3, 5, and 12 months respectively.\r\n\r\n      Primary investigation:\r\n\r\n      Research question 1.a Is delayed vaccination with the first dose of DTaP-IPV-Hib (vaccination\r\n      at or after 4 months of age) associated with a reduced risk of development of atopic\r\n      dermatitis from 4 months and until but not including 12 months of age compared with receiving\r\n      the first dose of DTaP-IPV-Hib before 4 months of age?\r\n\r\n      Secondary investigations:\r\n\r\n      Research question 1.b Among children with a timely 1st dose of DTaP-IPV-Hib (vaccination\r\n      before 4 months of age), is delayed vaccination with the second dose of DTaP-IPV-Hib\r\n      (vaccination at or after 6 months of age) associated with a reduced risk of development of\r\n      atopic dermatitis from 6 months and until but not including 12 months of age compared with\r\n      receiving the second dose of DTaP-IPV-Hib before 6 months of age?\r\n\r\n      Research question 2. Is receipt of DTaP-IPV-Hib associated with development of atopic\r\n      dermatitis from 3 months and until but not including 8 months of age compared with being\r\n      unvaccinated?\r\n\r\n      Data assessment Information on development of atopic dermatitis and vaccination status is\r\n      assessed at baseline (which is 4 months of age (research question 1.a.),6 months of age\r\n      (research question 1.b.) and 3 months of age (research question 2.)) and through follow up\r\n      (until 1 year of age). Confounder information is assessed at 3 months of age for all\r\n      analyses.\r\n\r\n      Development of atopic dermatitis is assessed according to an algorithm described in detail\r\n      under \"9. Outcome measures\", which uses information on prescriptions and hospitalizations up\r\n      until one year after the last age of outcome assessment (1 year of age in this study) to\r\n      confirm a case. Children must therefore be alive and living in Denmark until 2 years of age\r\n      representative of age at end of follow-up plus 1 year.\r\n\r\n      The Danish national registers contains individual-level information on a broad range of\r\n      health and social factors. Every child born in Denmark receives a unique personal\r\n      identification number (ID) at birth, which follows the individual through life. Using the ID\r\n      it is possible to link information from the different registers at an individual level.\r\n\r\n      Confounders:\r\n\r\n      The investigators will seek to retain information on potential confounders from the Danish\r\n      registers. Potential confounders will be assessed at 3 months of age and included in the\r\n      adjusted analyses.\r\n\r\n      Information on sex, season of birth, death, emigration, parental identity, sibling's identity\r\n      and exact address will be obtained from the Danish Civil Registration System. The\r\n      investigators will use information on parental identity to link every child to its parents\r\n      and obtain information on parents' origin of birth, single parenthood and the number of\r\n      children in the household. The investigators will furthermore derive information on\r\n      population density based on information on the municipality in which the child lives.\r\n      Information on parental and sibling's identity will be used to link information on family\r\n      history of atopic dermatitis to the child. Atopic dermatitis is categorized according to the\r\n      algorithm described in detail under \"9. Outcome measures\".\r\n\r\n      The variables; caesarean section, preterm birth, birthweight, and maternal smoking during\r\n      pregnancy is obtained from the Danish Medical Birth Register, which contains information on\r\n      all live and stillbirths in Denmark. Antibiotic use is recorded in the Danish National\r\n      Prescription Register. Information on chronic disease is obtained from in the Danish national\r\n      patient registry. Household income is obtained from the Danish registers on personal income\r\n      and transfer payment.\r\n\r\n      Maternal highest education is obtained from the Danish education registers.\r\n\r\n      The dataset is expected to contain close to complete information on confounders. Hence, it is\r\n      expected that children with missing confounder information constitute an ignorable proportion\r\n      of the complete study population, wherefore the investigators aim to conduct complete case\r\n      analyses only.\r\n\r\n      Statistical model for research question 1.a +1.b; investigation of the effect of timing of\r\n      vaccination.\r\n\r\n      For investigation of the effect of timing of the first and second dose of DTaP-IPV-Hib with\r\n      or without PCV, a Binary regression model will be used to estimate the adjusted relative risk\r\n      of developing atopic dermatitis from baseline (age for categorized timely vaccination) until\r\n      one year of age, among delayed vaccinated compared to timely vaccinated children. The\r\n      analysis will include all abovementioned potential confounders. Absolute risk differences\r\n      will be reported if relevant.\r\n\r\n      Intended subgroup and sensitivity analysis for the primary investigation (research question\r\n      1.a)\r\n\r\n      The following presents a priory identified relevant subgroup and sensitivity analyses. If\r\n      relevant, additional analysis will be included with the aim to pursue potential tendencies\r\n      revealed in the data analysis.\r\n\r\n        1. Sex differential effect Data will be analyzed for effect modification by sex because of\r\n           evidence of sex-differential non-specific effects of vaccines (Aaby et al., 2014) and\r\n           also sex-differential atopic sensitization associated with delayed vaccination (Kiraly\r\n           et al., 2016).\r\n\r\n        2. Further subgroup analyses\r\n\r\n             -  Effect modification by PCV vaccination. PCV was enrolled into the Danish\r\n                vaccination schedule during the years of this investigation. Hence, it will be\r\n                investigated if potential NSEs of DTaP-IPV-Hib vary according to receipt of PCV.\r\n\r\n             -  Exploratory analysis of effect modification.\r\n\r\n             -  Subgroup analysis, which only includes first born children; Parents of children\r\n                with older siblings may be more familiar with AD, which may result in a less\r\n                frequent health care seeking behavior. Parents of children with older siblings, who\r\n                have had AD themselves, may further have prescription medicines in the home from\r\n                treatment of prior cases of AD among the siblings. Hence, cases of AD categorized\r\n                based on disease specific prescriptions may be misclassified if the parents do not\r\n                get a new prescription for that child.\r\n\r\n        3. Sensitivity analyses\r\n\r\n             -  Sensitivity analysis to investigate if the results are affected by inclusion of\r\n                children with no DTaP-IPV-Hib before 1 year of age.\r\n\r\n             -  Investigation of reverse causation: A Cox regression will be conducted to\r\n                investigate if presence of atopic dermatitis is associated with subsequent delayed\r\n                vaccination.\r\n\r\n             -  Inclusion of negative control outcome/exposure; In similar studies, it has been\r\n                suspected that there may be a risk of ascertainment bias, whereby parents of\r\n                children who are delayed vaccinated, represent parents with a general lower health\r\n                care seeking behavior, which could result in lower levels of AD diagnosis among\r\n                their children. In order to accommodate this potential unmeasured confounder, the\r\n                investigators will seek to identify a relevant negative control exposure or\r\n                outcome, which will help indicate the strength of a potential interference from\r\n                this unmeasured confounder.\r\n\r\n      Statistical model for investigation of research question 2; investigation of the effect of\r\n      being vaccinated with DTaP-IPV-Hib with or without PCV compared with being non-vaccinated.\r\n\r\n      For investigation of the effect of being vaccinated with DTaP-IPV-Hib compared with being\r\n      non-vaccinated a Cox proportional hazards regression with age as the underlying time will be\r\n      used to estimate the adjusted HR of developing atopic dermatitis among children vaccinated\r\n      with DTaP-IPV-Hib compared with unvaccinated children. Vaccination status will be assessed\r\n      from time of scheduled vaccination (3 months of age) and set as a time dependent variable\r\n      with the categories unvaccinated and vaccinated.\r\n\r\n      As vaccination status is included as a time dependent variable, the group of unvaccinated\r\n      children will inherently become smaller with time as they get vaccinated. In order to assure\r\n      sufficient group sizes, children will only be followed until 8 months of age.\r\n\r\n      The model will include all identified potential confounding factors listed above. All\r\n      co-variates will be included as fixed variables and assessed at baseline (3 months of age).\r\n\r\n      Proportional hazard assumption will be examined.\r\n\r\n      Sensitivity analysis for the Cox regression\r\n\r\n      - Delayed diagnosis; Atopic dermatitis does not become apparent until the child has scratched\r\n      the affected skin. Furthermore, it may take weeks to months before the parents become aware\r\n      that this is not something which is passing, and bring the child to a doctor. Therefore, it\r\n      is very likely that actual onset of AD is weeks/months prior to date of diagnosis by the\r\n      healthcare professionals or receipt of disease specific prescriptions. Due to this delay,\r\n      there is a risk of differential misclassification, whereby cases of AD may be falsely\r\n      ascribed to the vaccinated exposure group. A sensitivity analysis will account for this delay\r\n      by setting the date for onset of AD prior to onset according to the AD algorithm. Primary\r\n      health care facilities will be contacted in order to gain expert insight on approximate delay\r\n      from onset of symptoms to receipt of prescription medicines or referral to a hospital.\r\n    ",
			"status": "Completed",
			"study_phase": null,
			"study_start_date": "1997-01-01",
			"primary_completion_date": "2014-12-31",
			"study_first_posted_date": "2017-05-05",
			"results_first_posted_date": null,
			"last_update_posted_date": "2017-05-09",
			"results_submitted_qc_not_done": null,
			"results_submitted_qc_done": null,
			"study_type": "Observational",
			"condition_name": "Atopic Dermatitis",
			"intervention_name": "RQ1a: Delayed vs. timely vaccination with the 1st dose of DTaP-IPV-Hib|RQ1b: Delayed vs. timely vaccination with the 2nd dose of DTaP-IPV-Hib|RQ2: Vaccination with DTaP-IPV-Hib compared to being unvaccinated",
			"eligibility_criteria": "\n        Inclusion Criteria:\r\n\r\n          -  Born in Denmark between between 1 January 1997 - 31 December 2012\r\n\r\n        Exclusion Criteria:\r\n\r\n          -  Do not receive 1st dose of DTaP-IPV-Hib before 1 year of age\r\n\r\n          -  Died before 24 months of age\r\n\r\n          -  Migrate before 24 months of age\r\n\r\n          -  Receive any vaccines other than DTaP-IPV-Hib, with or without PCV before 12 months of\r\n             age\r\n\r\n          -  Develop Atopic Dermatitis prior to baseline\r\n\r\n          -  Have missing confounder information\r\n      ",
			"eligibility_gender": "All",
			"eligibility_min_age": "24 Months",
			"eligibility_max_age": "24 Months",
			"sponsor_name": "Bandim Health Project|Murdoch Childrens Research Institute",
			"funder_type": "Other",
			"primary_outcome_measures": "Atopic dermatitis (AD)",
			"secondary_outcome_measures": "Receipt of medication for atopic dermatitis (only for the primary investigation 1.a)",
			"study_ids": "DTaP-Delay",
			"document_types": null,
			"is_unapproved_device": null,
			"acronym": null,
			"healthy_volunteers": "",
			"location_name": null,
			"country_name": null,
			"city_name": null,
			"state_name": null
		}
	]


### Search Results Export API

The endpoint for Search Results Export API is:
http://localhost:8000/ctgov/api/search_results_export

Search Results Export API accepts same parameter list as that of Clinical Studies Search API except that "first", "last" and "metadata_required" parameters are not required. The API will return all the study records that match search conditions.

Example query located in `database/examples/search_results_export_query.json`:
The POST request to the API should be as below.

	{
		"status":"Recruiting|Completed|Active, not recruiting",
		"condition":"",
		"other_terms":"",
		"country":"",
		"intervention":"",
		"target":"",
		"nct_id":"",
		"eligibility_criteria":"",
		"modality":"",
		"sponsor":"",
		"phase":"Phase 1, Phase 2, Phase 3",
		"start_date_from":"2019-01-01",
		"start_date_to":"2020-01-01",
		"primary_completion_date_from":"",
		"primary_completion_date_to":"",
		"first_posted_date_from":"",
		"first_posted_date_to":"",
		"results_first_posted_date_from":"",
		"results_first_posted_date_to":"",
		"last_update_posted_date_from":"",
		"last_update_posted_date_to":"",
		"study_results":"",
		"study_type":"",
		"eligibility_age":"",
		"eligibility_age_group":"child, adult, older adult",
		"eligibility_gender":"",
		"eligibility_ethnicity":"",
		"eligibility_condition":"",
		"eligibility_healthy_volunteer":"",
		"study_title_acronym":"",
		"study_outcome_measure":"",
		"study_collaborator":"",
		"study_ids":"",
		"study_location_terms":"",
		"study_funder_type":"",
		"study_document_type":"",
		"study_results_submitted":"",
		"study_roa":"Oral, Intradermal, Intravenous",
		"condition_terms":"",
		"city":"",
		"state":""
	}

#### Output

Sample result of Search Results Export API is below.

	[
		{
			"status": "Completed",
			"brief_title": "The Clinical Trial to Investigate the Pharmacokinetics and Safety/Tolerability of CKD-387 Under Fed Condition",
			"nct_id": "NCT03738449",
			"condition_name": "Type 2 Diabetes Mellitus",
			"intervention_name": "D484|CKD-387",
			"location_name": "Severance Hospital",
			"study_phase": "Phase 1",
			"sponsor_name": "Chong Kun Dang Pharmaceutical",
			"study_brief_desc": "\n      The purpose of this clinical trial is to evaluate the pharmacokinetics and\r\n      safety/tolerability after oral administration of CKD-387 and D484 under fed condition in\r\n      healthy adults.\r\n    ",
			"primary_outcome_measures": "Area under the plasma concentration of Metformin-time curve from time zero to time of last measurable concentration|Maximum plasma concentration of Metformin",
			"secondary_outcome_measures": "Apparent clearance of Metformin|Apparent volume of distribution of Metformin|Area under the plasma concentration of Metformin-time curve from time zero to infinity|Half-life of Metformin|Time to reach maximum (peak) plasma concentration of Metformin following drug administration",
			"study_start_date": "2019-01-08",
			"primary_completion_date": "2019-01-18"
		},
		{
			"status": "Completed",
			"brief_title": "Clinical Study to Evaluate Blood Concentrations of PF-06700841 After Oral Dose as Different Formulations",
			"nct_id": "NCT03765554",
			"condition_name": "Healthy Participants",
			"intervention_name": "PF-06700841 Immediate release tablets|PF-06700841 Modified release tablets",
			"location_name": "Pfizer Clinical Research Unit",
			"study_phase": "Phase 1",
			"sponsor_name": "Pfizer",
			"study_brief_desc": "\n      PF-06700841 is a dual Tyrosine kinase 2 (TYK2) Janus kinase 1 (JAK1) inhibitor that is being\r\n      developed for oral treatment of adult patients with Inflammatory Bowel Disease (IBD).This\r\n      open-label study will evaluate the pharmacokinetics of PF-06700841 following single oral\r\n      doses of immediate release (IR) and modified release (MR) tablets in healthy, adult\r\n      participants under fasted conditions. This is an open label, single dose, randomized, 2\r\n      period, 2- sequence crossover study in a single cohort of approximately 8 (minimum 6) healthy\r\n      participants.\r\n    ",
			"primary_outcome_measures": "Area under the plasma concentration-time curve from time zero to extrapolated infinite time (AUCinf) of PF-06700841 if data permit|Area under the plasma concentration-time curve from time zero to the last measured concentration (AUClast) of PF-06700841|Maximum Observed Plasma Concentration (Cmax) of PF-06700841|Time to reach maximum observed plasma concentration (Tmax) of PF-06700841",
			"secondary_outcome_measures": "Change from baseline in 12-Lead Electrocardiogram (ECG) parameters - PR interval, QRS complex, QT interval and QTC interval|Change from baseline in blood pressure|Change from baseline in heart rate|Change from baseline in oral temperature|Change from baseline in pulse rate|Number of participants with laboratory abnormalities|Number of participants with Treatment -Emergent Adverse Events (AEs), Serious Adverse Events (SAEs) and Discontinuation Due to AEs",
			"study_start_date": "2019-01-07",
			"primary_completion_date": "2019-04-03"
		},
		{
			...
		}
	]

### Trial Timelines API

The endpoint for Trial Timelines API is:
http://localhost:8000/ctgov/api/trial_timelines

Trial Timelines API returns nct_id, study_start_date, primary_completion_date and study_phase for the passed comma separated nct ids.

Example query located in `database/examples/trial_timelines_query.json`:
The POST request to the API should be as below.

	{
		"nct_ids":["NCT04727437", "NCT04322357", "NCT04727931"]
	}

#### Output

Sample result of Trial Timelines API is given below.

	[
		{
			"brief_title": "Prevalence of Cognitive Disorders in Newly Diagnosed Epilepsy",
			"status": "Not yet recruiting",
			"sponsor_name": "Central Hospital, Nancy, France",
			"nct_id": "NCT04727931",
			"study_start_date": "2021-03-01",
			"primary_completion_date": "2021-03-01",
			"study_phase": null
		},
		{
			"brief_title": "Weekend Steroids and Exercise as Therapy for DMD",
			"status": "Recruiting",
			"sponsor_name": "University of Florida|U.S. Army Medical Research and Development Command",
			"nct_id": "NCT04322357",
			"study_start_date": "2020-07-30",
			"primary_completion_date": "2022-10-31",
			"study_phase": "Phase 2"
		},
		{
			"brief_title": "STOPping Anticoagulation for Isolated or Incidental Subsegmental Pulmonary Embolism",
			"status": "Recruiting",
			"sponsor_name": "Cimar|Royal United Hospitals Bath NHS Foundation Trust|University of Birmingham",
			"nct_id": "NCT04727437",
			"study_start_date": "2021-04-30",
			"primary_completion_date": "2023-07-31",
			"study_phase": "Phase 3"
		}
	]

### Trials Dashboard API

The endpoint for Trials Dashboard API is:
http://localhost:8000/ctgov/api/trials_dashboard

Trials Dashboard API accepts same parameter list as that of Clinical Studies Search API except that "first", "last" and "metadata_required" parameters are not required. The API will return trials count by phases, intervention types, status, top 10 sponsors and up to 100 nct_ids.

Example query located in `database/examples/trials_dashboard_query.json`:
The POST request to the API should be as below.

	{
		"status": ["Recruiting", "Completed", "Active, not recruiting"],
		"condition":"",
		"other_terms":"",
		"country":"",
		"intervention":"",
		"target":"",
		"nct_id":"",
		"eligibility_criteria":"",
		"modality":"",
		"sponsor":"",
		"phase": ["Phase 1", "Phase 2", "Phase 3"],
		"start_date_from":"2019-01-01",
		"start_date_to":"2020-01-01",
		"primary_completion_date_from":"",
		"primary_completion_date_to":"",
		"first_posted_date_from":"",
		"first_posted_date_to":"",
		"results_first_posted_date_from":"",
		"results_first_posted_date_to":"",
		"last_update_posted_date_from":"",
		"last_update_posted_date_to":"",
		"study_results":"",
		"study_type":"",
		"eligibility_age":"",
		"eligibility_age_group":["child", "adult", "older adult"],
		"eligibility_gender":"",
		"eligibility_ethnicity":"",
		"eligibility_condition":"",
		"eligibility_healthy_volunteer":"",
		"study_title_acronym":"",
		"study_outcome_measure":"",
		"study_collaborator":"",
		"study_ids":"",
		"study_location_terms":"",
		"study_funder_type":"",
		"study_document_type":"",
		"study_results_submitted":"",
		"study_roa":["Oral", "Intradermal", "Intravenous"],
		"condition_terms":"",
		"city":"",
		"state":""
	}

#### Output

Sample result of Trials Dashboard API is given below.

	{
		"sponsors": [
			{
				"name": "Boehringer Ingelheim",
				"trials_count": 24
			},
			{
				"name": "National Institute of Allergy and Infectious Diseases (NIAID)",
				"trials_count": 14
			},
			{
				"name": "Pfizer",
				"trials_count": 10
			},
			{
				"name": "GlaxoSmithKline",
				"trials_count": 10
			},
			{
				"name": "Celgene",
				"trials_count": 8
			},
			{
				"name": "Ain Shams University",
				"trials_count": 8
			},
			{
				"name": "Hoffmann-La Roche",
				"trials_count": 8
			},
			{
				"name": "AstraZeneca",
				"trials_count": 8
			},
			{
				"name": "Janssen Research & Development, LLC",
				"trials_count": 7
			},
			{
				"name": "Merck Sharp & Dohme Corp.",
				"trials_count": 7
			}
		],
		"phases": [
			{
				"study_phase": "Early Phase 1",
				"trials_count": 33
			},
			{
				"study_phase": "Phase 1",
				"trials_count": 290
			},
			{
				"study_phase": "Phase 1/Phase 2",
				"trials_count": 48
			},
			{
				"study_phase": "Phase 2",
				"trials_count": 172
			},
			{
				"study_phase": "Phase 2/Phase 3",
				"trials_count": 31
			},
			{
				"study_phase": "Phase 3",
				"trials_count": 108
			}
		],
		"interventions": [
			{
				"intervention_type": "Behavioral",
				"trials_count": 3
			},
			{
				"intervention_type": "Biological",
				"trials_count": 56
			},
			{
				"intervention_type": "Combination Product",
				"trials_count": 11
			},
			{
				"intervention_type": "Device",
				"trials_count": 12
			},
			{
				"intervention_type": "Diagnostic Test",
				"trials_count": 2
			},
			{
				"intervention_type": "Dietary Supplement",
				"trials_count": 10
			},
			{
				"intervention_type": "Drug",
				"trials_count": 609
			},
			{
				"intervention_type": "Genetic",
				"trials_count": 1
			},
			{
				"intervention_type": "Other",
				"trials_count": 51
			},
			{
				"intervention_type": "Procedure",
				"trials_count": 7
			},
			{
				"intervention_type": "Radiation",
				"trials_count": 4
			}
		],
		"status": [
			{
				"status": "Active, not recruiting",
				"trials_count": 70
			},
			{
				"status": "Completed",
				"trials_count": 264
			},
			{
				"status": "Recruiting",
				"trials_count": 348
			}
		],
		"nct_ids": [
			"NCT03560011",
			"NCT03526874",
			"NCT03775096",
			...
		]
	}
