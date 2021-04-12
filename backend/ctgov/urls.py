from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsets import ClinicalTrialsBasicSearchView

router = DefaultRouter()
basic = router.register(
    r"basic_search",
    ClinicalTrialsBasicSearchView,
    basename="ClinicalTrialsBasicSearch",
)

urlpatterns = [
    path("api/", include("ctgov.api.urls")),
]
