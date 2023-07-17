import os
from typing import Dict

import requests

from .base_api import BaseOSDUAPIClient
from .exceptions import OSDUAPIError


class SchemaAPIError(OSDUAPIError):
    pass


class SchemaAPIClient(BaseOSDUAPIClient):
    service_path = "api/schema-service/v1/schema"

    def get_schema(self, *, id: str) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            f"{self.service_path}/{id}",
        )
        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if not response.ok:
            raise SchemaAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()

    def get_schemas(self) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
        )
        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if not response.ok:
            raise SchemaAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()

    def create_schema(
        self, *, schema: Dict
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
        )
        response = requests.post(
            url=url, headers=self.osdu_auth_backend.headers, json=schema
        )

        if not response.ok:
            raise SchemaAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()

    def update_schema(
        self, *, schema: Dict
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
        )
        response = requests.put(
            url=url, headers=self.osdu_auth_backend.headers, json=schema
        )

        if not response.ok:
            raise SchemaAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()
