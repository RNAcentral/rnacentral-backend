from django.urls import reverse
from .base import ApiV2BaseClass


class XrefTests(ApiV2BaseClass):
    def test_xref_endpoint(self):
        url = reverse("rna-xrefs", kwargs={"upi": self.upi})
        self._test_url(url)

    def test_xref_get_result(self):
        url = reverse("rna-xrefs", kwargs={"upi": self.upi})
        self._test_return_results(url)

    def test_xref_with_taxid_get_result(self):
        url = reverse("rna-xrefs", kwargs={"upi": self.upi, "taxid": self.taxid})
        self._test_return_results(url)

    def test_xref_no_results(self):
        url = reverse("rna-xrefs", kwargs={"upi": 1})
        self._test_return_no_results(url)
