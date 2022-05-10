import os
from calendar import timegm
from datetime import datetime
from typing import Dict

import jwt
import requests
from osdu_client.services.entitlements_api import EntitlementsAPIClient
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
        if response.status_code != 200:
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
        if response.status_code != 200:
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


class User(Auth):
    def __init__(
        self,
        access_token,
        refresh_token=None,
        data_partition_id=os.environ['DATA_PARTITION_ID'],
    ) -> None:
        super().__init__(
            client_id=os.environ['CLIENT_ID'],
            client_secret=os.environ['CLIENT_SECRET'],
            auth_authorize_url=os.environ['AUTH_AUTHORIZE_URL'],
            auth_token_url=os.environ['AUTH_TOKEN_URL'],
            osduonaws_base_url=os.environ['OSDUONAWS_BASE_URL'],
            iss=os.environ['ISS'],
        )
        self._access_token = access_token
        self.refresh_token = refresh_token
        self.data_partition_id = data_partition_id
        self.claims = self.decode(access_token)

    def __repr__(self) -> str:
        type_ = type(self)
        module = type_.__module__
        qualname = type_.__qualname__
        return f"<{module}.{qualname}(mail={self.mail})>"

    @property
    def mail(self):
        return self.claims.get("mail")

    @staticmethod
    def create_from_headers(headers: Dict):
        _headers = {k.lower(): v for k, v in headers.items()}
        return User(
            access_token=_headers["authorization"].replace("Bearer ", ""),
            data_partition_id=_headers["data-partition-id"],
        )

    def refresh_tokens(self):
        data = {
            "grant_type": "refresh_token",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "refresh_token": self.refresh_token,
            "scope": "offline_access",
        }
        url = "https://sso-uat.shell.com/as/token.oauth2"
        response = requests.post(url, data=data)
        print(self.auth_token_url)
        print(response.status_code)
        print(response.json())
        self._access_token = response.json()["access_token"]

    @property
    def access_token(self):
        if not self.is_authorized():
            self.refresh_tokens()
        return self._access_token

    def is_entitled(self, group_name, raise_exception=False):
        for g in self.groups:
            if g["name"] == group_name:
                return True
        if raise_exception:
            raise AuthorizationError(
                f"User {self.username} is not entitled to {group_name}."
            )
        return False
