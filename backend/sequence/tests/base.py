from rest_framework.test import APIClient, APITestCase


class ApiV2BaseClass(APITestCase):
    """Base class for API tests."""

    upi = "URS000075A546"
    taxid = "9606"
    urs_taxid = "URS000075A546_9606"
    accession = "Y09527.1:2562..2627:tRNA"

    def _test_url(self, url, data=None, follow=False, **extra):
        """Helper function for testing endpoint connectivity"""
        client = APIClient()
        response = client.get(url, data=data, follow=follow, **extra)
        self.assertEqual(response.status_code, 200)
        return response

    def _test_wrong_param(self, url, data=None, follow=False, **extra):
        """Helper function for testing using wrong parameters"""
        client = APIClient()
        response = client.get(url, data=data, follow=follow, **extra)
        self.assertEqual(response.status_code, 404)
        return response

    def _test_return_results(self, url, data=None, follow=False, **extra):
        """Helper function for testing endpoints that should return results"""
        client = APIClient()
        response = client.get(url, data=data, follow=follow, **extra)
        self.assertGreaterEqual(response.data["count"], 1)
        return response

    def _test_return_no_results(self, url, data=None, follow=False, **extra):
        """Helper function for testing endpoints with no results"""
        client = APIClient()
        response = client.get(url, data=data, follow=follow, **extra)
        self.assertEqual(response.data["count"], 0)
        return response
