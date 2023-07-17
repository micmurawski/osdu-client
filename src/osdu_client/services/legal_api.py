import os
from typing import List

import requests

from .base_api import BaseOSDUAPIClient
from .exceptions import OSDUAPIError


class LegalAPIException(OSDUAPIError):
    pass


class LegalAPIClient(BaseOSDUAPIClient):
    service_path = "api/legal/v1"

    def list_legal_tags(
        self,
        *,
        valid: bool = True,
        osdu_account_id: str = None,
        osdu_on_behalf_of: str = None,
    ) -> dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "legaltags",
        )
        params = {"valid": valid}
        headers = self.osdu_auth_backend.headers
        if osdu_account_id:
            headers["OSDU-Account-Id"] = osdu_account_id
        if osdu_on_behalf_of:
            headers["OSDU-On-Behalf-Of"] = osdu_on_behalf_of
        response = requests.get(url=url, headers=headers, params=params)

        if not response.ok:
            raise LegalAPIException(
                status_code=response.status_code, message=response.text
            )

        return response.json()

    def get_legal_tag(self, *,
                      name: str,
                      osdu_account_id: str = None,
                      osdu_on_behalf_of: str = None,
                      ) -> dict:
        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "legaltags",
            name
        )
        headers = self.osdu_auth_backend.headers
        if osdu_account_id:
            headers["OSDU-Account-Id"] = osdu_account_id
        if osdu_on_behalf_of:
            headers["OSDU-On-Behalf-Of"] = osdu_on_behalf_of
        response = requests.get(url=url, headers=headers)

        if not response.ok:
            raise LegalAPIException(
                status_code=response.status_code, message=response.text
            )

        return response.json()

    def create_legal_tag(
        self, *,
        name: str,
        description: str,
        country_of_origin: List[str],
        contract_id: str,
        originator: str,
        data_type: str,
        security_classification: str,
        personal_data: str,
        export_classification: str,
        expiration_date: str = None,
        extension_properties: dict = None,
        osdu_account_id: str = None,
        osdu_on_behalf_of: str = None,
    ) -> dict:

        request_body = dict(
            name=name,
            description=description,
            properties=dict(
                countryOfOrigin=country_of_origin,
                contractId=contract_id,
                originator=originator,
                dataType=data_type,
                securityClassification=security_classification,
                personalData=personal_data,
                exportClassification=export_classification,
            )
        )
        if expiration_date:
            request_body['properties']['expirationDate'] = expiration_date
        if extension_properties:
            request_body['properties']['extensionProperties'] = extension_properties

        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "legaltags"
        )
        headers = self.osdu_auth_backend.headers
        if osdu_account_id:
            headers["OSDU-Account-Id"] = osdu_account_id
        if osdu_on_behalf_of:
            headers["OSDU-On-Behalf-Of"] = osdu_on_behalf_of

        response = requests.post(url=url, json=request_body, headers=headers)

        if not response.ok:
            raise LegalAPIException(
                status_code=response.status_code, message=response.text
            )

        return response.json()

    def update_legal_tag(
        self, *
        name: str,
        contract_id: str,
        description: str,
        expiration_date: str = None,
        extension_properties: dict = None,
        osdu_account_id: str = None,
        osdu_on_behalf_of: str = None,
    ) -> dict:

        request_body = dict(
            name=name,
            description=description,
            contractId=contract_id,
        )
        if expiration_date:
            request_body['expirationDate'] = expiration_date
        if extension_properties:
            request_body['extensionProperties'] = extension_properties

        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "legaltags"
        )
        headers = self.osdu_auth_backend.headers
        if osdu_account_id:
            headers["OSDU-Account-Id"] = osdu_account_id
        if osdu_on_behalf_of:
            headers["OSDU-On-Behalf-Of"] = osdu_on_behalf_of

        response = requests.put(url=url, json=request_body, headers=headers)

        if not response.ok:
            raise LegalAPIException(
                status_code=response.status_code, message=response.text
            )

        return response.json()

    def get_legal_tags(
        self, *
        names: List[str],
        osdu_account_id: str = None,
        osdu_on_behalf_of: str = None,
    ) -> dict:

        request_body = dict(
            names=names,
        )

        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "legaltags:batchRetrieve"
        )
        headers = self.osdu_auth_backend.headers
        if osdu_account_id:
            headers["OSDU-Account-Id"] = osdu_account_id
        if osdu_on_behalf_of:
            headers["OSDU-On-Behalf-Of"] = osdu_on_behalf_of

        response = requests.post(url=url, json=request_body, headers=headers)

        if not response.ok:
            raise LegalAPIException(
                status_code=response.status_code, message=response.text
            )

        return response.json()

    def validate_legal_tags(
        self, *
        names: List[str],
        osdu_account_id: str = None,
        osdu_on_behalf_of: str = None,
    ) -> dict:

        request_body = dict(
            names=names,
        )

        url = os.path.join(
            self.osdu_auth_backend.base_url,
            self.service_path,
            "legaltags:validate"
        )
        headers = self.osdu_auth_backend.headers
        if osdu_account_id:
            headers["OSDU-Account-Id"] = osdu_account_id
        if osdu_on_behalf_of:
            headers["OSDU-On-Behalf-Of"] = osdu_on_behalf_of

        response = requests.post(url=url, json=request_body, headers=headers)

        if not response.ok:
            raise LegalAPIException(
                status_code=response.status_code, message=response.text
            )

        return response.json()
