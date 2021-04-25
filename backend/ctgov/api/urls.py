from django.urls import path, include
from .views import (
    BriefSummariesListApiView,
    SearchStudiesApiView,
    CountriesListApiView,
)

urlpatterns = [
    path("brief_summaries", BriefSummariesListApiView.as_view()),
    path("search_studies", SearchStudiesApiView.as_view()),
    path("countries", CountriesListApiView.as_view()),
    path("healthz", include("health_check.urls")),
]
