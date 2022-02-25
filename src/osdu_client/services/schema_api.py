import os
from typing import AnyStr, Dict

import requests

from osdu_client.auth import AuthInterface

from .base_api import BaseOSDUAPIClient


class SchemaAPIClient(BaseOSDUAPIClient):
    service_path = "api/schema-service/v1/schema"

    def __init__(self, osdu_auth_backend: AuthInterface):
        self.osdu_auth_backend = osdu_auth_backend

    def get_schema(self, *, id: AnyStr, ):
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            f"{self.service_path}/{id}",
        )
        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise Exception(response.text)

        return response.json()

    def get_schemas(self):
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
        )
        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise Exception(response.text)

        return response.json()

    def create_schema(
        self, *, schema: Dict
    ):
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
        )
        response = requests.post(
            url=url, headers=self.osdu_auth_backend.headers, json=schema
        )

        if response.status_code // 100 != 2:
            raise Exception(response.text)

        return response.json()

    def update_schema(
        self, *, schema: Dict
    ):
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
        )
        response = requests.put(
            url=url, headers=self.osdu_auth_backend.headers, json=schema
        )

        if response.status_code // 100 != 2:
            raise Exception(response.text)

        return response.json()
