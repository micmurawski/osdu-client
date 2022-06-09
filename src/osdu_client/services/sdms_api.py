import os
from json import JSONDecodeError
from typing import AnyStr, Dict, List, Optional
from urllib import response

import requests

from .base_api import BaseOSDUAPIClient
from .exceptions import OSDUAPIError


class SDMSAPIError(OSDUAPIError):
    pass


class SDMSTokenAPI:
    def create_impersonation_token(
        self, *, user_token: AnyStr, resources: List[Dict], metadata: Dict
    ) -> Dict:
        headers = self.osdu_auth_backend.headers
        headers["user-token"] = user_token
        url = os.path.join(
            self.osdu_auth_backend.base_url, self.service_path, f"impersonation-token"
        )
        request_body = {"resources": resources, "metadata": metadata}
        response = requests.post(
            url=url, headers=headers, json=request_body
        )
        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()

    def refresh_impersonation_token(
        self, *, impersonation_token: AnyStr, impersonation_token_context: AnyStr
    ) -> Dict:
        headers = self.osdu_auth_backend.headers
        headers["impersonation-token"] = impersonation_token
        headers["impersonation-token-context"] = impersonation_token_context
        url = os.path.join(
            self.osdu_auth_backend.base_url, self.service_path, f"impersonation-token"
        )
        response = requests.put(url=url, headers=headers)
        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()


class SDMSAppsAPI:
    def register_app(self, *, email: AnyStr, sdpath: AnyStr) -> Dict:
        params = {"email": email, "sdpath": sdpath}
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"app",
        )
        response = requests.post(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )
        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()

    def retrive_registered_apps(self, *, sdpath: AnyStr) -> Dict:
        params = {"sdpath": sdpath}
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"app",
        )
        response = requests.get(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )
        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return {"apps": response.json()}

    def set_trusted_app(self, *, email: AnyStr, sdpath: AnyStr) -> Dict:
        params = {"email": email, "sdpath": sdpath}
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"app/trusted",
        )
        response = requests.post(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )
        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()

    def retrive_trusted_apps(self, *, sdpath: AnyStr) -> Dict:
        params = {"sdpath": sdpath}
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"app/trusted",
        )
        response = requests.get(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )
        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return {"apps": response.json()}


class SDMSDatasetAPI:
    def retrieve_dataset(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        path: Optional[AnyStr] = "/",
        seismicmeta: bool = True,
        translate_user_info: bool = True,
        record_version: AnyStr = None
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"dataset/tenant/{tenant_id}/subproject/{subproject_id}/dataset/{dataset_id}",
        )
        # fill path & meta params
        params = {
            "path": path,
            "seismicmeta": seismicmeta,
            "translate-user-info": translate_user_info
        }
        if record_version:
            params["record_version"] = record_version
        response = requests.get(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()

    def retrieve_dataset_permission(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        path: Optional[AnyStr] = "/",
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

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()

    def delete_dataset(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        path: Optional[AnyStr] = "/",
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

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()

    def list_subprojects_datasets(
        self, *, tenant_id: AnyStr, subproject_id: AnyStr, gtags: List[AnyStr] = None, limit: int = 10, cursor: AnyStr = None,
        translate_user_info: bool = True
    ) -> Dict:

        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"dataset/tenant/{tenant_id}/subproject/{subproject_id}",
        )
        params = {
            "gtag": gtags,
            "limit": limit,
            "cursor": cursor,
            "translate-user-info": translate_user_info
        }
        response = requests.get(
            url=url, headers=self.osdu_auth_backend.headers, params=params)

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()

    def register_dataset(
        self,
        *,
        tenant_id: AnyStr,
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
        parents: List[AnyStr] = [],
        acls=None
    ) -> Dict:

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
        if acls:
            request_body["acls"] = acls

        if id:
            _prefix = kind.rsplit(":", 1)[0].replace("wks:", "")
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

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

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
        close: AnyStr = None,
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

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text
            )

        return response.json()

    def lock_dataset(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        path: AnyStr = None,
        openmode: AnyStr = "write",
        wid: AnyStr = None,
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

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return True

    def unlock_dataset(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        path: AnyStr
    ) -> Dict:

        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"dataset/tenant/{tenant_id}/subproject/{subproject_id}/dataset/{dataset_id}/unlock",
        )
        params = {"path": path}  # "openmode": openmode}
        response = requests.put(
            url=url, headers=self.osdu_auth_backend.headers, params=params
        )

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()


class SDMSUtilityAPI:
    def generate_gcs_access_token(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        dataset_id: AnyStr,
        dataset_path: AnyStr = "/",
        readonly=False,
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

        if not response.ok:
            try:
                raise SDMSAPIError(
                    status_code=response.status_code, message=response.json()
                )
            except JSONDecodeError:
                raise SDMSAPIError(
                    status_code=response.status_code, message=response.text
                )

        return response.json()


class SDMSubprojectAPI:
    def create_new_subproject(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        admin: AnyStr,
        storage_class: AnyStr = None,
        storage_location: AnyStr = None,
        legal_tags: AnyStr = None,
        acls: Dict = None,
    ) -> Dict:
        request_body = {
            "admin": admin,
            "storage_class": storage_class or "REGIONAL",
            "storage_location": (storage_location).upper(),
        }
        if acls:
            request_body["acls"] = acls

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

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()

    def list_subprojects(self, *, tenant_id: AnyStr) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"subproject/tenant/{tenant_id}",
        )

        response = requests.get(
            url=url, headers=self.osdu_auth_backend.headers)

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return {"subprojects": response.json()}

    def get_sdms_subproject(
        self, *, tenant_id: AnyStr, subproject_id: AnyStr, translate_user_info=True
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"subproject/tenant/{tenant_id}",
            f"subproject/{subproject_id}",
        )
        query = {"translate-user-info": translate_user_info}

        response = requests.get(
            url=url, headers=self.osdu_auth_backend.headers, query=query
        )

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()

    def delete_sdms_subproject(
        self, *, tenant_id: AnyStr, subproject_id: AnyStr
    ) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"subproject/tenant/{tenant_id}",
            f"subproject/{subproject_id}",
        )
        response = requests.delete(
            url=url, headers=self.osdu_auth_backend.headers)

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()

    def patch_sdms_subproject_metadata(
        self,
        *,
        tenant_id: AnyStr,
        subproject_id: AnyStr,
        ltag: AnyStr = None,
        acls: Dict = None,
        access_policy: AnyStr = None,
        recursive: AnyStr = None,
    ) -> Dict:
        requests_body = {}
        if acls:
            requests_body["acls"] = acls
        if access_policy:
            requests_body["access_policy"] = access_policy

        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            f"subproject/tenant/{tenant_id}",
            f"subproject/{subproject_id}",
        )
        headers = self.osdu_auth_backend.headers
        if ltag:
            headers["ltag"] = ltag
        query = {}
        if recursive:
            query["recursive"] = recursive

        response = requests.patch(
            url=url, json=requests_body, headers=headers, params=query
        )

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()


class SDMSTenantAPI:
    def register_sdms_tenant(
        self, *, tenant_id: AnyStr, gcpid: AnyStr, esd: AnyStr, default_acl: AnyStr
    ) -> Dict:
        requests_body = {"gcpid": gcpid,
                         "esd": esd, "default_acl": default_acl}
        url = os.path.join(
            self.osdu_auth_backend.base_url, self.service_path, f"tenant/{tenant_id}"
        )
        response = requests.post(
            url=url, json=requests_body, headers=self.osdu_auth_backend.headers
        )

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()

    def get_sdms_tenant(self, *, tenant_id: AnyStr) -> Dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url, self.service_path, f"tenant/{tenant_id}"
        )
        response = requests.get(
            url=url, headers=self.osdu_auth_backend.headers)

        if not response.ok:
            raise SDMSAPIError(
                status_code=response.status_code, message=response.text)

        return response.json()


class SDMSAPIClient(
    BaseOSDUAPIClient,
    SDMSDatasetAPI,
    SDMSubprojectAPI,
    SDMSTenantAPI,
    SDMSUtilityAPI,
    SDMSAppsAPI,
    SDMSTokenAPI,
):
    service_path = "api/seismic-store/v3"
