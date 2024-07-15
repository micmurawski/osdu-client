from __future__ import annotations

import requests

from osdu_client.exceptions import OSDUAPIError
from osdu_client.services.base import OSDUAPIClient
from osdu_client.utils import urljoin
from osdu_client.validation import validate_data

from .models import TranslateItem


class PolicyAPIError(OSDUAPIError):
    pass


class PolicyClient(OSDUAPIClient):
    service_path = ""

    def home_page(
        self,
        *,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent

        url = urljoin(self.base_url, self.service_path, "")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def get_api_policy_v1_policies(
        self,
        *,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        url = urljoin(self.base_url, self.service_path, "api/policy/v1/policies")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def get_fetch_policy(
        self,
        *,
        policy_id: str,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        url = urljoin(
            self.base_url, self.service_path, "api/policy/v1/policies/%s" % policy_id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def get_fetch_instance_policy(
        self,
        *,
        policy_id: str,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/policy/v1/policies/osdu/instance/%s" % policy_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def get_api_policy_v1_policies_osdu_partition(
        self,
        *,
        policy_id: str,
        data_partition: str,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/policy/v1/policies/osdu/partition/%s/%s" % (policy_id, data_partition),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def delete_partition_policy(
        self,
        *,
        policy_id: str,
        data_partition: str,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/policy/v1/policies/osdu/partition/%s/%s" % (policy_id, data_partition),
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def create_or_update_partition_policy(
        self,
        *,
        policy_id: str,
        data_partition: str,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        url = urljoin(
            self.base_url,
            self.service_path,
            "api/policy/v1/policies/osdu/partition/%s/%s" % (policy_id, data_partition),
        )
        response = requests.put(url, headers=headers)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def evaluate_policy(
        self,
        *,
        policy_id: str,
        include_auth: str | None = None,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        params = {
            "policy_id": policy_id,
        }
        if include_auth is not None:
            params["include_auth"] = include_auth

        url = urljoin(
            self.base_url, self.service_path, "api/policy/v1/evaluations/query"
        )
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def translate_policy_api(
        self,
        *,
        query: str,
        input: dict,
        unknowns: list[str],
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        data = {
            "query": query,
            "input": input,
            "unknowns": unknowns,
        }

        if self.validation:
            validate_data(data, TranslateItem, PolicyAPIError)

        url = urljoin(self.base_url, self.service_path, "api/policy/v1/translate")
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def get_api_policy_v1_info(
        self,
        *,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent

        url = urljoin(self.base_url, self.service_path, "api/policy/v1/info")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def create_api_policy_v1_compile(
        self,
        *,
        metrics: str | None = None,
        instrument: str | None = None,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        params = {}
        if metrics is not None:
            params["metrics"] = metrics
        if instrument is not None:
            params["instrument"] = instrument

        url = urljoin(self.base_url, self.service_path, "api/policy/v1/compile")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def get_tenant(
        self,
        *,
        all_data: str | None = None,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        params = {}
        if all_data is not None:
            params["all_data"] = all_data

        url = urljoin(self.base_url, self.service_path, "api/policy/v1/tenant")
        response = requests.get(url, headers=headers, params=params)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def update_tenant(
        self,
        *,
        service: str,
        polling_min_delay_seconds: str | None = None,
        polling_max_delay_seconds: str | None = None,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        params = {
            "service": service,
        }
        if polling_min_delay_seconds is not None:
            params["polling_min_delay_seconds"] = polling_min_delay_seconds
        if polling_max_delay_seconds is not None:
            params["polling_max_delay_seconds"] = polling_max_delay_seconds

        url = urljoin(self.base_url, self.service_path, "api/policy/v1/tenant")
        response = requests.put(url, headers=headers, params=params)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def delete_tenant(
        self,
        *,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        url = urljoin(self.base_url, self.service_path, "api/policy/v1/tenant")
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def get_health(
        self,
        *,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent

        url = urljoin(self.base_url, self.service_path, "api/policy/v1/health")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def get_ready(
        self,
        *,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent

        url = urljoin(self.base_url, self.service_path, "api/policy/v1/ready")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def validate_policy(
        self,
        *,
        policy_id: str,
        template: str | None = None,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        params = {}
        if template is not None:
            params["template"] = template

        url = urljoin(
            self.base_url, self.service_path, "api/policy/v1/validate/%s" % policy_id
        )
        response = requests.put(url, headers=headers, params=params)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def get_backup(
        self,
        *,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        url = urljoin(self.base_url, self.service_path, "api/policy/v1/backup")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def bootstrap(
        self,
        *,
        force: str | None = None,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        params = {}
        if force is not None:
            params["force"] = force

        url = urljoin(self.base_url, self.service_path, "api/policy/v1/bootstrap")
        response = requests.post(url, headers=headers, params=params)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def get_api_policy_v1_config(
        self,
        *,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        url = urljoin(self.base_url, self.service_path, "api/policy/v1/config")
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()
