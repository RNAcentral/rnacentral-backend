from django.urls import reverse
from .base import ApiV2BaseClass

from ..api.rna_precomputed.viewsets import RnaPrecomputedViewSet


class RnaTests(ApiV2BaseClass):
    """Tests for Rna Precomputed data"""

    def test_rna_precomputed_endpoint(self):
        url = reverse("rna-detail", kwargs={"pk": self.upi})
        self._test_url(url)

    def test_rna_precomputed_wrong_pk(self):
        url = reverse("rna-detail", kwargs={"pk": "FOOBAR"})
        self._test_wrong_param(url)

    def test_get_rna_precomputed_view_name(self):
        view = RnaPrecomputedViewSet()
        view.request = None
        view.kwargs = {"pk": self.upi}

        view_name = view.get_view_name()
        expected_name = "RNA"

        self.assertEqual(view_name, expected_name)
