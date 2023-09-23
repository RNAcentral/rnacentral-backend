from django.urls import reverse
from .base import ApiV2BaseClass


class RfamTests(ApiV2BaseClass):
    def test_rfam_endpoint(self):
        url = reverse("rfam-hits", kwargs={"upi": self.upi})
        self._test_url(url)

    def test_rfam_get_result(self):
        url = reverse("rfam-hits", kwargs={"upi": "URS00008D09BC"})
        self._test_return_results(url)

    def test_rfam_no_results(self):
        url = reverse("rfam-hits", kwargs={"upi": self.upi})
        self._test_return_no_results(url)
