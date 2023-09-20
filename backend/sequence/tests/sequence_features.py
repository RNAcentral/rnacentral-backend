from django.urls import reverse
from .base import ApiV2BaseClass


class SequenceFeatureTests(ApiV2BaseClass):
    def test_sequence_feature_endpoint(self):
        """Test sequence features endpoint."""
        url = reverse(
            "rna-sequence-features", kwargs={"upi": self.upi, "taxid": self.taxid}
        )
        self._test_url(url)
