from osdu_client.utils import urljoin
from osdu_client.services.base import BaseOSDUAPIClient
from osdu_client.exceptions import OSDUAPIError
import requests


class NotificationAPIError(OSDUAPIError):
    pass


class NotificationClient(BaseOSDUAPIClient):
    def record_changed(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "push-handlers/records-changed")
        response = requests.post(url, headers=headers)
        if not response.ok:
            raise NotificationAPIError(response.text, response.status_code)
        return response.json()

    def get_info(
        self, data_partition_id: str | None = None, tenant: str | None = None
    ) -> dict:
        headers = self.auth.headers
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, "info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise NotificationAPIError(response.text, response.status_code)
        return response.json()
