from django.urls import path
from .views import (
    BriefSummariesListApiView,
    BasicSearchApiView,
    CountriesListApiView,
)

urlpatterns = [
    path(
        "brief_summaries",
        BriefSummariesListApiView.as_view(),
        name="brief_summaries",
    ),
    path(
        "basic_search",
        BasicSearchApiView.as_view(),
        name="basic_search",
    ),
    path(
        "countries",
        CountriesListApiView.as_view(),
        name="countries",
    ),
]
