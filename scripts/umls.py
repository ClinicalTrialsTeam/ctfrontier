"""
UMLS API SCRIPT
To use this file you must create a .env file in the same folder
with the environment variable UMLS_API_KEY.
To get a UMLS_API_KEY, create an account at https://uts.nlm.nih.gov/uts/.
Requirements listed in umls-requirements.txt,
install with `pip install -r umls-requirements.txt`
"""
import requests
from os import getenv
from os.path import join, dirname
from dotenv import load_dotenv
from lxml.html import fromstring
import json

# load dotenv
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

AUTH_BASE_URI = "https://utslogin.nlm.nih.gov"
API_KEY = getenv("UMLS_API_KEY")
SERVICE = "http://umlsks.nlm.nih.gov"
API_BASE_URI = "https://uts-ws.nlm.nih.gov/rest"


class UMLSAuthentication:
    """Class for getting UMLS authentication tickets"""

    _instance = None

    def __init__(self):
        raise RuntimeError("Call instance() instead")

    @classmethod
    def instance(cls):
        """Singleton instance"""
        if not cls._instance:
            cls._instance = cls.__new__(cls)
        return cls._instance

    @property
    def tgt(self):
        """Get a Ticket Generating Ticket and save it for future requests"""
        if not hasattr(self, "_tgt"):
            r = requests.post(
                f"{AUTH_BASE_URI}/cas/v1/api-key", data={"apikey": API_KEY}
            )
            r.raise_for_status
            response = fromstring(r.text)
            self._tgt = response.xpath("//form/@action")[0]
        return self._tgt

    def get_service_ticket(self):
        """Get a single-use Service Ticket using the stored TGT"""
        r = requests.post(self.tgt, data={"service": SERVICE})
        r.raise_for_status
        return r.text


def umls_search(phrase):
    page_number = 1
    results = []

    while True:
        st = UMLSAuthentication.instance().get_service_ticket()

        query = {"string": phrase, "ticket": st, "pageNumber": page_number}

        r = requests.get(f"{API_BASE_URI}/search/current", params=query)

        data = json.loads(r.text)["result"]

        if data["results"][0]["ui"] == "NONE":
            break

        results.extend(data["results"])
        page_number += 1

    return results


# example search
phrase = "fracture of carpal bone"
search_results = umls_search(phrase)
print(f"Got {len(search_results)} total results for term '{phrase}'")
