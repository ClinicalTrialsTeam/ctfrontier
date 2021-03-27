from rest_framework.test import APIRequestFactory
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ctgov.models import BasicSearch
from ctgov.api.serializers import BasicSearchDocumentSerializer

factory = APIRequestFactory()
