import os
from json import JSONDecodeError
from typing import AnyStr, Dict, List, Optional

import requests

from osdu_client.auth import AuthInterface

from .base_api import BaseOSDUAPIClient


class SDDMSException(Exception):
    pass


class SDDMSAPIClient(BaseOSDUAPIClient):
    service_path = "api/seismic-store/v3"

    def __init__(self, osdu_auth_backend: AuthInterface):
        self.osdu_auth_backend = osdu_auth_backend

    def create_new_subproject(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,

        admin: AnyStr = None,
        storage_class: AnyStr = None,
        storage_location: AnyStr = None,
        legal_tags: AnyStr = None,
    ):
        request_body = {
            "admin": admin or "admin@testing.com",
            "storage_class": storage_class or "REGIONAL",
            "storage_location": (storage_location).upper(),
        }

        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"subproject/tenant/{tenant_id}/subproject/{subproject_id}",
        )

        headers = self.osdu_auth_backend.headers
        # put legal tags into headers
        if legal_tags:
            headers.update({"ltag": legal_tags})

        response = requests.post(
            url=url,
            headers=headers,
            json=request_body,
        )

        if response.status_code // 100 != 2:
            raise SDDMSException(response.text)

        return response.json()

    def get_sddms_dataset(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        path: Optional[AnyStr] = "/",
        fetch_meta: bool = False,


    ):
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"dataset/tenant/{tenant_id}/subproject/{subproject_id}/dataset/{dataset_id}",
        )
        # fill path & meta params
        params = {"path": path, "seismicmeta": fetch_meta}
        response = requests.get(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )

        if response.status_code // 100 != 2:
            raise SDDMSException(response.text)

        return response.json()

    def get_sddms_dataset_permission(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        path: Optional[AnyStr] = "/"
    ):
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"dataset/tenant/{tenant_id}/subproject/{subproject_id}/dataset/{dataset_id}/permission",
        )
        # fill path & meta params
        params = {"path": path}
        response = requests.get(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )

        if response.status_code // 100 != 2:
            raise SDDMSException(response.text)

        return response.json()

    def delete_sddms_dataset(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        path: Optional[AnyStr] = "/"
    ):
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"dataset/tenant/{tenant_id}/subproject/{subproject_id}/dataset/{dataset_id}",
        )
        # fill path & meta params
        params = {"path": path}
        response = requests.delete(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )

        if response.status_code // 100 != 2:
            raise SDDMSException(response.text)

        return response.json()

    def get_sddms_datasets(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr
    ):
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"dataset/tenant/{tenant_id}/subproject/{subproject_id}",
        )
        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise SDDMSException(response.text)

        return response.json()

    def get_sddms_subprojects(
        self,
        *,
        tenant_id: AnyStr
    ):
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"subproject/tenant/{tenant_id}",
        )

        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise SDDMSException(response.text)

        return {"subprojects": response.json()}

    def create_sddms_dataset(
        self,
        *,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        legal_tags: List[AnyStr],
        gtags: List[AnyStr],
        other_relevant_data_countries: List[AnyStr],
        data: Dict,
        type: AnyStr,
        slm: Dict = {},
        path: AnyStr = None,
        kind: AnyStr = None,
        id: AnyStr = None,
        parents: List[AnyStr] = []
    ) -> Dict:
        tenant_id, *_ = kind.split(":")

        request_body = {
            "type": type,
            "gtags": gtags,
            "seismicmeta": {
                "ancestry": {"parents": parents},
                "kind": kind,
                "legal": {
                    "legaltags": legal_tags,
                    "otherRelevantDataCountries": other_relevant_data_countries,
                },
                "slm": slm,
                "data": data,
            },
        }

        if id:
            _prefix, _ = kind.rsplit(":", 1)
            request_body["seismicmeta"]["id"] = f"{_prefix}:{id}"

        params = {"path": path, "seismicmeta": True}
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"dataset/tenant/{tenant_id}/subproject/{subproject_id}/dataset/{dataset_id}",
        )
        response = requests.post(
            url=url,
            headers=self.osdu_auth_backend.headers,
            json=request_body,
            params=params,
        )

        if response.status_code // 100 != 2:
            raise SDDMSException(response.text)

        return response.json()

    def update_sddms_dataset_filemetadata(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        metadata: Dict = {},
        filemetadata: Dict = {},
        path: AnyStr = None,
        close: AnyStr = None
    ) -> Dict:
        request_body = {
            "metadata": metadata,
            "filemetadata": filemetadata,
        }
        params = {"path": path, "close": close}
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"dataset/tenant/{tenant_id}/subproject/{subproject_id}/dataset/{dataset_id}",
        )
        response = requests.patch(
            url=url,
            headers=self.osdu_auth_backend.headers,
            json=request_body,
            params=params,
        )

        if response.status_code // 100 != 2:
            raise SDDMSException(response.json())

        return response.json()

    def lock_sddms_dataset(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        path: AnyStr = None,
        openmode: AnyStr = "write",
        wid: AnyStr = None
    ) -> Dict:

        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"dataset/tenant/{tenant_id}/subproject/{subproject_id}/dataset/{dataset_id}/lock",
        )
        params = {"path": path, "openmode": openmode, "wid": wid}
        response = requests.put(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )

        if response.status_code // 100 != 2:
            raise SDDMSException(response.text)

        return True

    def unlock_sddms_dataset(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        path: AnyStr,
        openmode: AnyStr
    ) -> Dict:

        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"dataset/tenant/{tenant_id}/subproject/{subproject_id}/dataset/{dataset_id}/unlock",
        )
        params = {"path": path, "openmode": openmode}
        response = requests.put(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )

        if response.status_code // 100 != 2:
            raise SDDMSException(response.text)

        return response.json()

    def patch_sddms_dataset(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        metadata: Dict = {},
        filemetadata: Dict = {},
        seismicmeta: Dict = None
    ):

        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"dataset/tenant/{tenant_id}/subproject/{subproject_id}/dataset/{dataset_id}",
        )
        request_body = {"metadata": metadata, "filemetadata": filemetadata}

        if seismicmeta:
            request_body["seismicmeta"] = seismicmeta

        response = requests.patch(
            url=url, headers=self.osdu_auth_backend.headers, json=request_body
        )

        if response.status_code // 100 != 2:
            raise SDDMSException(response.text)

        return response.json()

    def get_gcs_access_token(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        dataset_path: AnyStr = "/",
        readonly=False
    ) -> Dict:

        url = os.path.join(
            self.osdu_auth_backend.base_url,
            "api/seismic-store/v3/utility/gcs-access-token",
        )
        # NOTE: shortcircuit the sd path logic, to use generic subproject sd:// for token access
        # if dataset_path == "/":
        #    sdpath = f"sd://{tenant_id}/{subproject_id}/{dataset_id}"
        # else:
        #    # sdpath = f"sd://{tenant_id}/{subproject_id}/{dataset_path}/{dataset_id}"
        #    sdpath = os.path.join("sd://", tenant_id, subproject_id)
        #    print(sdpath)
        #    sdpath = os.path.join(sdpath, dataset_path.strip("/"))
        #    print(sdpath)
        #    sdpath = os.path.join(sdpath, dataset_id)

        sdpath = f"sd://{tenant_id}/{subproject_id}"
        params = {
            "sdpath": sdpath,
            "readonly": readonly,
        }
        response = requests.get(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )

        if response.status_code // 100 != 2:
            try:
                raise SDDMSException(response.json())
            except JSONDecodeError:
                raise SDDMSException(response.text)

        return response.json()
