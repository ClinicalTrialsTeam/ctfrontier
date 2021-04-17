from django_elasticsearch_dsl import Document, fields, Index
from elasticsearch_dsl import analyzer, tokenizer
from .models import SearchStudies

CLINICALTRIALS_BASIC_SEARCH_INDEX = Index("basic_search")

CLINICALTRIALS_BASIC_SEARCH_INDEX.settings(
    number_of_shards=1, number_of_replicas=0
)


@CLINICALTRIALS_BASIC_SEARCH_INDEX.document
class ClinicalTrialsBasicSearch(Document):
    class Index:
        name = "search_studies"

        text_analyzer = analyzer(
            "text_analyzer",
            tokenizer="standard",
            filter=["standard", "lowercase", "stop", "snowball"],
            char_filter=["html_strip"],
        )

        fuzzy_analyzer = analyzer(
            "fuzzy_analyzer",
            tokenizer=tokenizer(
                "trigram", "edge_gram", min_gram=1, max_gram=20
            ),
            filter=["standard", "lowercase", "stop", "snowball"],
            char_filter=["html_strip"],
        )

        status = fields.TextField(
            analyzer=text_analyzer,
            fields={"raw": fields.TextField(analyzer="keyword")},
        )

        brief_title = fields.TextField(
            analyzer=fuzzy_analyzer,
            fields={"raw": fields.TextField(analyzer="keyword")},
        )

        condition_name = fields.TextField(
            analyzer=fuzzy_analyzer,
            fields={"raw": fields.TextField(analyzer="keyword")},
        )

        study_detailed_desc = fields.TextField(
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

    class Django:
        model = SearchStudies

        fields = [
            "status",
            "brief_title",
            "condition_name",
            "study_detailed_desc",
            "country_name",
            "intervention_name",
            "eligibility_criteria",
            "study_brief_desc",
            "location_name",
        ]
