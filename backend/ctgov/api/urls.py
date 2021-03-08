from django.conf.urls import url
from django.urls import path, include
from .views import (
    BriefSummariesListApiView,
)

urlpatterns = [
    path("brief_summaries", BriefSummariesListApiView.as_view()),
]
