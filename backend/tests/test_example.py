from pytest_postgresql import factories
from rest_framework import status
from rest_framework.test import (
    APIRequestFactory,
    APITestCase,
    URLPatternsTestCase,
)
from django.urls import include, path
import ctgov.api.views as views


# def test_main_postgres(postgresql):
#     cur = postgresql.cursor()
#     cur.execute('CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);')
#     postgresql.commit()
#     cur.close()


# postgresql_proc2 = factories.postgresql_proc(port=9876)
# postgresql2 = factories.postgresql('postgresql_proc2')


# def test_two_postgreses(postgresql, postgresql2):
#     cur = postgresql.cursor()
#     cur.execute('CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);')
#     postgresql.commit()
#     cur.close()

#     cur = postgresql2.cursor()
#     cur.execute('CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);')
#     postgresql2.commit()
#     cur.close()


# postgresql_my_proc = factories.postgresql_proc(
#     port=None, unixsocketdir='/var/run')
# postgresql_my = factories.postgresql('postgresql_my_proc')

postgresql_external = factories.postgresql("postgresql_nooproc")

# factory = APIRequestFactory()
# request = factory.post('/notes/', {'title': 'new idea'}, format='json')


class TestRequestBasicSearchTest(APITestCase, URLPatternsTestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = views.BasicSearchApiView.as_view()
        self.uri = "/basic_search"

    urlpatterns = [path("api/", include("ctgov.api.urls"))]

    #  def test_list(self):
    #     request = self.factory.get(self.uri)
    #     response = self.view(request)
    #     self.assertEqual(response.status_code, 200,
    #                      'Expected Response Code 200, received {0} instead.'
    #                      .format(response.status_code))

    def test_request_basic(self):
        # url = reverse("basic_search")
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
        request = self.factory.post(self.uri, data, format="json")
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(len(response.data), 1)
