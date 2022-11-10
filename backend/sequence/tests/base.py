from rest_framework.test import APIClient, APITestCase


class ApiV2BaseClass(APITestCase):
    """Base class for API tests."""

    upi = "URS000075A546"
    taxid = "9606"
    accession = "Y09527.1:2562..2627:tRNA"

    def _test_url(self, url, data=None, follow=False, **extra):
        """Auxiliary function for testing the API with and without trailing slash."""
        client = APIClient()
        response = client.get(url, data=data, follow=follow, **extra)
        self.assertEqual(response.status_code, 200)
        return response
