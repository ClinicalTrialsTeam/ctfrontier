# documents.py

from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from ctgov.models import Documents
from .models import Sponsors


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
class SponsorsDocuments(Document):
    class Index:
        name = "sponsors"
        settings = {"number_of_shards": 1, "number_of_replicas": 0}

    class Django:
        model = Sponsors

        fields = [
            "agency_class",
            "lead_or_collaborator",
            "name",
        ]
