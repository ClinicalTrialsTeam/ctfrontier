from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import analyzer, tokenizer
from ctgov.models import Documents
from .models import ReportedEvents, BasicSearch


@registry.register_document
class ReportedEventsDocuments(Document):
    class Index:
        name = "reported_events"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = ReportedEvents

        fields = [
            "ctgov_group_code",
            "time_frame",
            "event_type",
            "default_vocab",
            "default_assessment",
            "subjects_affected",
            "subjects_at_risk",
            "description",
            "event_count",
            "organ_system",
            "adverse_event_term",
            "frequency_threshold",
            "vocab",
            "assessment",
        ]


@registry.register_document
class SearchDocuments(Document):
    class Index:
        name = "study_comments"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Documents

        fields = [
            "document_id",
            "document_type",
            "url",
            "comment",
        ]


@registry.register_document
class ClinicalTrialsBasicSearch(Document):
    class Index:
        name = "basic_search"

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

        nct_id = fields.TextField(
            analyzer=text_analyzer,
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
        model = BasicSearch

        fields = [
            "status",
            "brief_title",
            "nct_id",
            "condition_name",
            "study_detailed_desc",
            "country_name",
            "intervention_name",
            "eligibility_criteria",
            "study_brief_desc",
            "location_name",
        ]
