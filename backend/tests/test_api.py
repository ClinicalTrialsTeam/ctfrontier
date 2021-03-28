from rest_framework.test import APIRequestFactory
from rest_framework import status
from rest_framework.test import APITestCase
from ctgov.models import BasicSearch
from django.urls import reverse
from mock import Mock


factory = APIRequestFactory()


class RequestBasicSearchTest(APITestCase):
    def test_request_basic(self):
        url = reverse("basic_search")
        data = {
            "status": "Recruiting",
            "condition": "",
            "other_terms": "POETYK",
            "country": "",
            "intervention": "",
            "target": "",
            "nct_id": "",
            "eligibility_criteria": "",
            "modality": "exercise",
            "sponsor": "",
            "phase": "",
            "start_date_from": "",
            "start_date_to": "",
            "primary_completion_date_from": "",
            "primary_completion_date_to": "",
            "first_posted_date_from": "",
            "first_posted_date_to": "",
            "results_first_posted_date_from": "",
            "results_first_posted_date_to": "",
            "last_update_posted_date_from": "",
            "last_update_posted_date_to": "",
            "first": "",
            "last": "",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
