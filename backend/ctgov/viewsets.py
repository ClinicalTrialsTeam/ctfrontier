from django_elasticsearch_dsl_drf.filter_backends import (
    FilteringFilterBackend,
    IdsFilterBackend,
    OrderingFilterBackend,
    DefaultOrderingFilterBackend,
    SearchFilterBackend,
)
from django_elasticsearch_dsl_drf.viewsets import BaseDocumentViewSet
from django_elasticsearch_dsl_drf.pagination import PageNumberPagination

from .documents import ClinicalTrialsBasicSearch
from api.serializers import BasicSearchSerializer


class ClinicalTrialsBasicSearchView(BaseDocumentViewSet):
    """The BookDocument view."""

    document = ClinicalTrialsBasicSearch
    serializer_class = BasicSearchSerializer
    pagination_class = PageNumberPagination
    lookup_field = "nct_id"
    filter_backends = [
        FilteringFilterBackend,
        IdsFilterBackend,
        OrderingFilterBackend,
        DefaultOrderingFilterBackend,
        SearchFilterBackend,
    ]
    # Define search fields
    search_fields = (
        "condition_name",
        "brief_title",
    )
    # Define filter fields
    filter_fields = {
        "condition_name": "condition_name.raw",
        "brief_title": "brief_title.raw",
    }
    # Define ordering fields
    ordering_fields = {
        "condition_name": "condition_name.raw",
        "brief_title": "brief_title.raw",
    }
    # Specify default ordering
    ordering = (
        "condition_name",
        "brief_title",
    )
