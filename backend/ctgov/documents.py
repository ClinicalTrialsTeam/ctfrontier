from django_elasticsearch_dsl import Document, fields, Index
from elasticsearch_dsl import analyzer, tokenizer
from .models import SearchStudies

studies = Index("search_studies")
studies.settings(number_of_shards=1, number_of_replicas=0)
text_analyzer = analyzer(
    "text_analyzer",
    tokenizer="standard",
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)
fuzzy_analyzer = analyzer(
    "fuzzy_analyzer",
    tokenizer=tokenizer("trigram", "edge_ngram", min_gram=1, max_gram=20),
    filter=["lowercase", "stop", "snowball"],
    char_filter=["html_strip"],
)


@studies.doc_type
class ClinicalTrialsSearchStudies(Document):
    status = fields.TextField(
        analyzer=text_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    brief_title = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    nct_id = fields.TextField(
        analyzer=text_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    condition_name = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    country_name = fields.TextField(
        analyzer=text_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    city_name = fields.TextField()

    state_name = fields.TextField(
        analyzer=text_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    intervention_name = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    eligibility_criteria = fields.TextField(
        analyzer=text_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    study_brief_desc = fields.TextField(
        analyzer=text_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    location_name = fields.TextField()
    sponsor_name = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )

    study_start_date = fields.DateField()
    primary_completion_date = fields.DateField()
    study_first_posted_date = fields.DateField()
    results_first_posted_date = fields.DateField()
    last_update_posted_date = fields.DateField()

    study_type = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    eligibility_gender = fields.TextField(
        analyzer=text_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    sponsor_name = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    study_ids = fields.TextField(
        analyzer=text_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    funder_type = fields.TextField(
        analyzer=text_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    results_submitted_qc_not_done = fields.DateField()
    results_submitted_qc_done = fields.DateField()

    document_types = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    official_title = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    acronym = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    primary_outcome_measures = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    secondary_outcome_measures = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )

    eligibility_min_age_numeric = fields.FloatField()
    eligibility_max_age_numeric = fields.FloatField()

    study_phase = fields.TextField(
        analyzer=text_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )

    class Django(object):
        model = SearchStudies
