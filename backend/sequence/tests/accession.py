from django.urls import reverse
from .base import ApiV2BaseClass


class AccessionTests(ApiV2BaseClass):

    def test_accession_endpoint(self):
        """Test accession endpoint."""
        url = reverse("accession-detail", kwargs={"pk": self.accession})
        self._test_url(url)
