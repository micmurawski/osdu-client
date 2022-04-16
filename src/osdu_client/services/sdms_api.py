import os
from json import JSONDecodeError
from typing import AnyStr, Dict, List, Optional

import requests

from . import OSDUAPIException
from .base_api import BaseOSDUAPIClient


class SDMSException(OSDUAPIException):
    pass


class SDMSDatasetAPI:
    def retrieve_dataset(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        path: Optional[AnyStr] = "/",
        fetch_meta: bool = False
    ) -> Dict:
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
            raise SDMSException(response.text)

        return response.json()

    def retrieve_dataset_permission(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        path: Optional[AnyStr] = "/"
    ) -> Dict:
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
            raise SDMSException(response.text)

        return response.json()

    def delete_dataset(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        path: Optional[AnyStr] = "/"
    ) -> Dict:
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
            raise SDMSException(response.text)

        return response.json()

    def list_subprojects_datasets(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"dataset/tenant/{tenant_id}/subproject/{subproject_id}",
        )
        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise SDMSException(response.text)

        return response.json()

    def register_dataset(
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
            raise SDMSException(response.text)

        return response.json()

    def patch_datasets_metadata(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        metadata: Dict = {},
        filemetadata: Dict = {},
        seismicmeta: Dict = None,
        path: AnyStr = None,
        close: AnyStr = None
    ) -> Dict:
        request_body = {
            "metadata": metadata,
            "filemetadata": filemetadata,
        }
        if seismicmeta:
            request_body["seismicmeta"] = seismicmeta
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
            raise SDMSException(response.json())

        return response.json()

    def lock_dataset(
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
            raise SDMSException(response.text)

        return True

    def unlock_dataset(
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
            raise SDMSException(response.text)

        return response.json()


class SDMSUtilityAPI:
    def generate_gcs_access_token(
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
                raise SDMSException(response.json())
            except JSONDecodeError:
                raise SDMSException(response.text)

        return response.json()


class SDMSubprojectAPI:
    def create_new_subproject(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,

        admin: AnyStr = None,
        storage_class: AnyStr = None,
        storage_location: AnyStr = None,
        legal_tags: AnyStr = None
    ) -> Dict:
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
            raise SDMSException(response.text)

        return response.json()

    def get_sdms_subprojects(
        self,
        *,
        tenant_id: AnyStr
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"subproject/tenant/{tenant_id}",
        )

        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise SDMSException(response.text)

        return {"subprojects": response.json()}

    def get_sdms_subproject(self, *, tenant_id: AnyStr, subproject_id: AnyStr, translate_user_info=True) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"subproject/tenant/{tenant_id}",
            f"subproject/{subproject_id}"
        )
        query = {
            "translate-user-info": translate_user_info
        }

        response = requests.get(url=url, headers=self.osdu_auth_backend.headers, query=query)

        if response.status_code // 100 != 2:
            raise SDMSException(response.text)

        return response.json()

    def delete_sdms_subproject(self, *, tenant_id: AnyStr, subproject_id: AnyStr) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"subproject/tenant/{tenant_id}",
            f"subproject/{subproject_id}"
        )
        response = requests.delete(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise SDMSException(response.text)

        return response.json()

    def patch_sdms_subproject_metadata(self, *, tenant_id: AnyStr, subproject_id: AnyStr,
                                       ltag: AnyStr, acl: Dict = None, access_policy: AnyStr = None,
                                       recursive: AnyStr = None) -> Dict:
        requests_body = {}
        if acl:
            requests_body['acl'] = acl
        if access_policy:
            requests_body['access_policy'] = access_policy

        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"subproject/tenant/{tenant_id}",
            f"subproject/{subproject_id}"
        )
        headers = self.osdu_auth_backend.headers
        headers['ltag'] = ltag
        query = {}
        if recursive:
            query['recursive'] = recursive

        response = requests.patch(url=url, json=requests_body, headers=headers, query=query)

        if response.status_code // 100 != 2:
            raise SDMSException(response.text)

        return response.json()


class SDMSTenantAPI:
    def register_sdms_tenant(self, *, tenant_id: AnyStr, gcpid: AnyStr, esd: AnyStr, default_acl: AnyStr) -> Dict:
        requests_body = {
            "gcpid": gcpid,
            "esd": esd,
            "default_acl": default_acl
        }
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"tenant/{tenant_id}"
        )
        response = requests.post(url=url, json=requests_body, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise SDMSException(response.text)

        return response.json()

    def get_sdms_tenant(self, *, tenant_id: AnyStr) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"tenant/{tenant_id}"
        )
        response = requests.get(url=url, headers=self.osdu_auth_backend.headers)

        if response.status_code // 100 != 2:
            raise SDMSException(response.text)

        return response.json()


class SDMSAPIClient(
    BaseOSDUAPIClient, SDMSDatasetAPI, SDMSubprojectAPI,
    SDMSTenantAPI, SDMSUtilityAPI
):
    service_path = "api/seismic-store/v3"
