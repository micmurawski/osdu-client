import os
from calendar import timegm
from datetime import datetime

import jwt
import requests

from osdu_client.auth import AuthBackendInterface


class AuthorizationError(Exception):
    pass


class Auth(AuthBackendInterface):
    def __init__(
        self,
        client_id,
        client_secret,
        auth_authorize_url,
        auth_token_url,
        iss,
        osduonaws_base_url,
        principal_client_id=None,
        principal_client_secret=None,
    ) -> None:
        self.iss = iss
        self.client_id = client_id
        self.client_secret = client_secret
        self.principal_client_id = principal_client_id
        self.principal_client_secret = principal_client_secret
        self.auth_authorize_url = auth_authorize_url
        self.auth_token_url = auth_token_url
        self.osduonaws_base_url = osduonaws_base_url

    def get_headers(self):
        return {
            "Authorization": f"Bearer {self.access_token}",
            "data-partition-id": self.data_partition_id,
        }

    def get_base_url(self):
        return self.osduonaws_base_url

    def get_service_principal_access_token(self) -> str:
        response = requests.post(
            url=self.auth_token_url,
            data={
                "grant_type": "client_credentials",
                "scope": "osduOnAws/osduOnAWSService",
            },
            auth=(self.principal_client_id, self.principal_client_secret),
        )
        if not response.ok:
            raise AuthorizationError(response.text)

        return response.json()

    def verify(self, access_token):
        response = requests.post(
            self.auth_token_url,
            auth=(self.client_id, self.client_secret),
            data={
                "grant_type": "urn:pingidentity.com:oauth2:grant_type:validate_bearer",
                "token": access_token,
                "client_id": self.client_id,
            },
        )
        if not response.ok:
            raise AuthorizationError("Token is invalid")

    def is_expired(self, raise_excpetion=True):
        if self.remaining_time <= 0:
            if raise_excpetion:
                raise AuthorizationError("User authorization token expired.")
            else:
                return True
        return False

    @property
    def remaining_time(self):
        return self.claims["exp"] - timegm(datetime.utcnow().utctimetuple())

    @staticmethod
    def decode(access_token):
        decoded = jwt.decode(access_token, options={"verify_signature": False})
        return decoded

    def is_authorized(self, verify=False, raise_exception=False):
        result = not self.is_expired(raise_excpetion=raise_exception)
        try:
            if verify:
                self.verify(self._access_token)
        except jwt.exceptions.PyJWTError as e:
            raise AuthorizationError(str(e)) from e

        return result

    def get_sd_connection_string(self, log_level=None):
        seismic_ddms_api = os.path.join(self.osduonaws_base_url, "api/seismic-store/v3")
        sd_conn_str = (
            f"sd_authority_url={seismic_ddms_api};"
            f"sd_api_key=xxx;auth_token_url={self.auth_token_url};"
            f"sdtoken={self.access_token};"
            f"client_id={self.client_id};client_secret={self.client_secret};"
            f"refresh_token={None};scopes=openid email"
        )
        if log_level:
            sd_conn_str += f";LogLevel={log_level}"

        return sd_conn_str
