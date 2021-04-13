from rest_framework import status
from rest_framework.test import APITestCase
from ctgov.models import SearchStudies


# Create your tests here.
class SearchStudiesTest(APITestCase):

    # Test to check status of post request and results count based on study status
    def test_completed_studies_count(self):
        url = "http://localhost:8000/ctgov/api/search_studies"
        data = {"status": "Completed"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SearchStudies.objects.count(), 198704)

    # Test to check status of post request and results count based on eligibility age
    def test_eligibility_age(self):
        url = "http://localhost:8000/ctgov/api/search_studies"
        data = {"eligibility_age": "55"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SearchStudies.objects.count(), 10196)

    # Test to check status of post request and results count based on eligibility minimum and maximum age
    def test_eligibility_age_range(self):
        url = "http://localhost:8000/ctgov/api/search_studies"
        data = {"eligibility_min_age": "25", "eligibility_max_age": "65"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SearchStudies.objects.count(), 21275)

    # Test to check status of post request and results count for funder_type=industry
    def test_funder_type(self):
        url = "http://localhost:8000/ctgov/api/search_studies"
        data = {"study_funder_type": "industry"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SearchStudies.objects.count(), 117049)

    # Test to check status of post request and results count for document type = Study Protocol
    def test_document_type(self):
        url = "http://localhost:8000/ctgov/api/search_studies"
        data = {"study_document_type": "Study Protocol"}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(SearchStudies.objects.count(), 1581)
