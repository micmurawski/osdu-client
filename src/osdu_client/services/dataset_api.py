import os
from typing import Dict, List

import requests

from .base_api import BaseOSDUAPIClient
from .exceptions import OSDUAPIError


class DatasetAPIError(OSDUAPIError):
    pass


class DatasetAPIClient(BaseOSDUAPIClient):
    service_path = "api/dataset/v1"

    def get_storage_instructions(
        self, *, kind_sub_type: str
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "storageInstructions",
        )
        params = {"kindSubType": kind_sub_type}
        response = requests.post(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )

        if not response.ok:
            raise DatasetAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()

    def get_batch_retrieval_instructions(
        self,
        *,
        dataset_registry_ids: List[str]
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "retrievalInstructions",
        )
        response = requests.post(
            url=url,
            headers=self.osdu_auth_backend.headers,
            json={"datasetRegistryIds": dataset_registry_ids},
        )

        if not response.ok:
            raise DatasetAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()

    def get_retrieval_instructions(
        self,
        *,
        id: str
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "retrievalInstructions",
        )
        response = requests.get(
            url=url,
            headers=self.osdu_auth_backend.headers,
            params={"id": id},
        )

        if not response.ok:
            raise DatasetAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()

    def register_dataset(
        self,
        *,
        dataset_registries: List[Dict]
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "registerDataset",
        )
        response = requests.put(
            url=url,
            headers=self.osdu_auth_backend.headers,
            json={"datasetRegistries": dataset_registries},
        )

        if not response.ok:
            raise DatasetAPIError(
                status_code=response.status_code,
                message=response.text
            )

        return response.json()
