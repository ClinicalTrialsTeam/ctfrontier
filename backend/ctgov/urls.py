from django.urls import path, include


urlpatterns = [
    path("api/", include("ctgov.api.urls")),
]
