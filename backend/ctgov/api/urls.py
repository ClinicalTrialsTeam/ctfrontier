from django.conf.urls import url
from django.urls import path, include
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