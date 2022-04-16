import os
from typing import AnyStr, List

import requests

from osdu_client.auth import AuthInterface

from .base_api import BaseOSDUAPIClient


class DatasetAPIClient(BaseOSDUAPIClient):
    service_path = "api/dataset/v1"

    def __init__(self, osdu_auth_backend: AuthInterface):
        self.osdu_auth_backend = osdu_auth_backend

    def get_storage_instructions(
        self, *, kind_sub_type: AnyStr
    ):
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "getStorageInstructions",
        )
        params = {"kindSubType": kind_sub_type}
        response = requests.get(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )

        if response.status_code // 100 != 2:
            raise Exception(response.text)

        return response.json()

    def get_retrieval_instructions(
        self,
        *,
        dataset_registry_ids: List[AnyStr]
    ):
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "getRetrievalInstructions",
        )
        response = requests.post(
            url=url,
            headers=self.osdu_auth_backend.headers,
            json={"datasetRegistryIds": dataset_registry_ids},
        )

        if response.status_code // 100 != 2:
            raise Exception(response.text, response.status_code)

        return response.json()
