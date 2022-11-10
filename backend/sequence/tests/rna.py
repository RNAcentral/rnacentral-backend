from django.urls import reverse
from .base import ApiV2BaseClass


class RnaTests(ApiV2BaseClass):

    def test_rna_endpoint(self):
        """Test RNAcentral sequence endpoint."""
        url = reverse("rna-detail", kwargs={"pk": self.upi})
        self._test_url(url)
