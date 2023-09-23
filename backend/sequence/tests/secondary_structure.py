from django.urls import reverse
from .base import ApiV2BaseClass


class SecondaryStructureTests(ApiV2BaseClass):
    def test_secondary_structure_endpoint(self):
        url = reverse("rna-2d-svg", kwargs={"upi": "URS00000F9D45"})
        self._test_url(url)

    def test_secondary_structure_wrong_pk(self):
        url = reverse("rna-2d-svg", kwargs={"upi": "FOOBAR"})
        self._test_wrong_param(url)
