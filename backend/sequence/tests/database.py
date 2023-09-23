from django.urls import reverse
from .base import ApiV2BaseClass


class DatabaseTests(ApiV2BaseClass):
    def test_database_list_endpoint(self):
        url = reverse("database-list")
        self._test_url(url)

    def test_get_expert_db_data(self):
        url = reverse("database", kwargs={"pk": 1})
        self._test_url(url)

    def test_get_wrong_expert_db_id(self):
        url = reverse("database", kwargs={"pk": 999999})
        self._test_wrong_param(url)
