from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import Document, Text
from elasticsearch.helpers import streaming_bulk
from elasticsearch import Elasticsearch
from . import models


connections.create_connection(timeout=3000)


def bulk_indexing():
    ResponsibleParties.init()
    es = Elasticsearch(timeout=300, max_retries=10, retry_on_timeout=True)

    success, failed = 0, 0
    for ok, item in streaming_bulk(
        client=es,
        actions=(
            b.indexing()
            for b in models.ResponsibleParties.objects.all().iterator()
        ),
        chunk_size=100,
        max_retries=10,
        max_backoff=600,
        request_timeout=300,
    ):
        if not ok:
            print(f"Request failed: {item}")
            failed += 1
        else:
            print(f"Request succeeded: {item}")
            success += 1

    print(f"Completed with {success} success, {failed} failures")


class ResponsibleParties(Document):
    nct = Text()
    responsible_party_type = Text()
    name = Text()
    title = Text()
    organization = Text()
    affiliation = Text()

    class Meta:
        index = "responsible_parties"
