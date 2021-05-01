from django.urls import path
from .views import (
    BriefSummariesListApiView,
    SearchStudiesApiView,
    CountriesListApiView,
    CountriesNewApiView,
    ConditionsListApiView,
    StatesListApiView,
    CitiesListApiView,
    StudyDetailApiView,
    TrialsDashboardApiView,
    SearchResultsExportApiView,
    TrialTimelinesApiView,
)


urlpatterns = [
    path("brief_summaries", BriefSummariesListApiView.as_view()),
    path("search_studies", SearchStudiesApiView.as_view()),
    path("countries", CountriesListApiView.as_view()),
    path("countries_new", CountriesNewApiView.as_view()),
    path("conditions", ConditionsListApiView.as_view()),
    path("states", StatesListApiView.as_view()),
    path("cities", CitiesListApiView.as_view()),
    path("study_detail", StudyDetailApiView.as_view()),
    path("trials_dashboard", TrialsDashboardApiView.as_view()),
    path("search_results_export", SearchResultsExportApiView.as_view()),
    path("trial_timelines", TrialTimelinesApiView.as_view()),
]
