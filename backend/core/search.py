from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text, Date
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models


connections.create_connection()


def bulk_indexing():
    ResponsibleParties.init()
    es = Elasticsearch()
    bulk(
        client=es,
        actions=(
            b.indexing()
            for b in models.ResponsibleParties.objects.all().iterator()
        ),
    )


class ResponsibleParties(Document):
    nct = Text()
    responsible_party_type = Text()
    name = Text()
    title = Text()
    organization = Text()
    affiliation = Text()

    class Meta:
        index = "responsible_parties"
