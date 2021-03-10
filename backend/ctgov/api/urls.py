from django.conf.urls import url
from django.urls import path, include
from .views import (
    BriefSummariesListApiView,
    SearchApiView
)

urlpatterns = [
    path("brief_summaries", BriefSummariesListApiView.as_view()),
    path("search", SearchApiView.as_view()),
]
