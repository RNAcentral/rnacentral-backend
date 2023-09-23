from django.urls import reverse
from .base import ApiV2BaseClass


class AccessionTests(ApiV2BaseClass):
    def test_accession_endpoint(self):
        url = reverse("accession-detail", kwargs={"pk": self.accession})
        self._test_url(url)

    def test_get_wrong_accession(self):
        url = reverse("accession-detail", kwargs={"pk": "FOOBAR"})
        self._test_wrong_param(url)
