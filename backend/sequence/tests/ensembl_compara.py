from django.urls import reverse
from .base import ApiV2BaseClass


class EnsemblComparaTests(ApiV2BaseClass):
    def test_ensembl_compara_endpoint(self):
        url = reverse("ensembl-compara", kwargs={"urs_taxid": self.upi})
        self._test_url(url)

    def test_ensembl_compara_get_result(self):
        url = reverse("ensembl-compara", kwargs={"urs_taxid": "URS00002B3204_9606"})
        self._test_return_results(url)

    def test_ensembl_compara_no_results(self):
        url = reverse("ensembl-compara", kwargs={"urs_taxid": self.upi})
        self._test_return_no_results(url)
