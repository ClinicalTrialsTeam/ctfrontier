from django.urls import path
from .views import (
    BriefSummariesListApiView,
    BasicSearchApiView,
    CountriesListApiView,
)

urlpatterns = [
    path("brief_summaries", BriefSummariesListApiView.as_view()),
    path("basic_search", BasicSearchApiView.as_view()),
    path("countries", CountriesListApiView.as_view()),
]
