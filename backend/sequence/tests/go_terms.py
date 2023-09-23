from django.urls import reverse
from .base import ApiV2BaseClass

from ..api.go_terms.viewsets import GoTermsViewSet


class GoTermsTests(ApiV2BaseClass):
    def test_go_annotations_endpoint(self):
        url = reverse("go-annotations", kwargs={"rna_id": self.upi})
        self._test_url(url)

    def test_ensembl_compara_get_result(self):
        url = reverse("go-annotations", kwargs={"rna_id": "URS0000338542_9606"})
        self._test_return_results(url)

    def test_ensembl_compara_no_results(self):
        url = reverse("go-annotations", kwargs={"rna_id": self.upi})
        self._test_return_no_results(url)

    def test_get_view_name(self):
        view = GoTermsViewSet()
        view.request = None
        view.kwargs = {"rna_id": self.upi}

        view_name = view.get_view_name()
        expected_name = "Gene Ontology annotations"

        self.assertEqual(view_name, expected_name)
