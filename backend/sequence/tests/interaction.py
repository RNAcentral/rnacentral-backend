from django.urls import reverse
from .base import ApiV2BaseClass


class InteractionTests(ApiV2BaseClass):
    def test_ensembl_compara_endpoint(self):
        url = reverse("interactions", kwargs={"urs_taxid": self.upi})
        self._test_url(url)

    def test_ensembl_compara_get_result(self):
        url = reverse("interactions", kwargs={"urs_taxid": "URS00004BEF81_559292"})
        self._test_return_results(url)

    def test_ensembl_compara_no_results(self):
        url = reverse("interactions", kwargs={"urs_taxid": self.upi})
        self._test_return_no_results(url)
