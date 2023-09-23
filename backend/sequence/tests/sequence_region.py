from django.urls import reverse
from .base import ApiV2BaseClass


class SequenceRegionTests(ApiV2BaseClass):
    def test_sequence_region_endpoint(self):
        url = reverse("genome-locations", kwargs={"urs_taxid": self.urs_taxid})
        self._test_url(url)

    def test_sequence_region_get_result(self):
        url = reverse("genome-locations", kwargs={"urs_taxid": self.urs_taxid})
        self._test_return_results(url)

    def test_sequence_region_no_results(self):
        url = reverse("genome-locations", kwargs={"urs_taxid": 1})
        self._test_return_no_results(url)
