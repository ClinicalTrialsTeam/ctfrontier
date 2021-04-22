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
    intervention_name = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    eligibility_criteria = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )
    study_brief_desc = fields.TextField(
        analyzer=fuzzy_analyzer,
        fields={"raw": fields.TextField(analyzer="keyword")},
    )

    class Django(object):
        model = SearchStudies
