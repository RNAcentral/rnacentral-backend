from django.urls import reverse
from .base import ApiV2BaseClass

from ..api.qc_status.viewsets import QcStatusViewSet


class QcStatusTests(ApiV2BaseClass):
    def test_qc_status_endpoint(self):
        url = reverse("qc-status", kwargs={"pk": self.urs_taxid})
        self._test_url(url)

    def test_qc_status_wrong_pk(self):
        url = reverse("qc-status", kwargs={"pk": "FOOBAR"})
        self._test_wrong_param(url)

    def test_get_qc_status_view_name(self):
        view = QcStatusViewSet()
        view.request = None
        view.kwargs = {"pk": self.urs_taxid}

        view_name = view.get_view_name()
        expected_name = "QC Status"

        self.assertEqual(view_name, expected_name)
