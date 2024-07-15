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
    ) -> dict:
        """

        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            correlation_id (str):
            user_agent (str):
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            Return all policies from OPA directly that match partition_bundle_root data-partition-id in header (if bundles are enabled).
        This API gives the list of all the defined policies and it includes the policy definitions in the raw Rego form.
        It performs authorization check. The user making the call needs to be either service.policy.user or service.policy.admin in the provided data partition.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
        Return a policy directly from OPA with no filtering
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            policy_id (str):
            correlation_id (str):
            user_agent (str):
            x_user_id (str): identifier the user in the query
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
        Return an instance policy from OPA directly.
        Args:
            data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
            policy_id (str):
            correlation_id (str):
            user_agent (str):
            x_user_id (str): identifier the user in the query
        Returns:
            response data (dict)
        Raises:
            OSDUValidation: if request values are wrong.
            OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            Return an policy for a partition id from OPA.
        Requires data-partition-id in header.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                policy_id (str):
                data_partition (str):
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            ## Delete a partition policy
        * This API requires admin privileges (service.policy.admin) in the provided data partition.
        * Partition ID in header and in path must match
        * Policy_id must end with a ".rego"

        ### Possible http return status codes:
        * 200 - no error
        * 202 - accepted
        * 400 - bad request
            * for example, if data_partition in path doesn't match data-partition-id in header
        * 401 - unauthorized
        * 403 - forbidden
            * for example, if calling with only user privs
        * 404 - not found
        * 422 - validation Error
            * for example, if policy_id doesn't end with ".rego"
        * 500 - server error
        * 501 - not implemented
            * for example, if bundles are not supported.
        * 503 - service not available
            * for example, if issues with bundles server

        Errors will include some detail in returning json.

        Return json:
        ```
            {
                "policy_id": string,
                "data_partition": string,
                "status": bool,
                "message": string,
                "result": string json from OPA
            }
        ```
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                policy_id (str):
                data_partition (str):
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            ## Create or update a policy with given policy_id for a given data partition.
        This API will create/update policy definition with provided Rego expression included in file and assign it with provided id.

        * This API requires admin privileges (service.policy.admin) in the provided data partition.
        * Partition ID in header and in path must match
        * Policy_id must end with a ".rego"

        ### Possible http return status codes:
        * 200 - no error
        * 202 - accepted
        * 400 - bad request
            * for example, if data_partition in path doesn't match data-partition-id in header
        * 401 - unauthorized
        * 403 - forbidden
            * for example, if calling with only user privs
        * 422 - validation Error
            * for example, if policy_id doesn't end with ".rego"
            * for example, if package declaration issue
        * 500 - server error
        * 501 - not implemented
            * for example, if bundles are not supported.
        * 503 - service not available
            * for example, if issues with bundles server

        Errors will include some detail in returning json.

        Return json:
        ```
            {
                "policy_id": string,
                "data_partition": string,
                "opa_payload": string,
                "status_code": http status code
                "status": bool
                "message": string
            }
        ```
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                policy_id (str):
                data_partition (str):
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            ## Evaulate Policies
        This API is to help you evaluate policies.

        If include_auth is True, then in your file data token, xuserid and data partition id will be ignored in the file and information from the headers
        of the request will be used for this information.

        ### Example:
        For example file data for policy dataauthz.rego:
        Where XXXX is the data partition and YYYY is a legal tag
        ```json
        {
            "input": {
                "operation": "update",
                "records": [
                    {
                        "id":"XXXX:test:1.4.1654807204111",
                        "kind":"XXXX:bulkupdate:test:1.1.1654807204111",
                        "legal":{
                            "legaltags":[
                                "YYYY"
                            ],
                            "otherRelevantDataCountries":["US"],
                            "status":"compliant"
                        },
                        "acls":{
                            "viewers":["data.default.viewers@XXXX.group"],
                            "owners":["data.default.owners@XXXX.group"]
                        }
                    }
                ]
            }
        }
        ```
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                policy_id (str):
                include_auth (str): Update posted data to include auth (token, xuserid and data partition id) from headers
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
        correlation_id: str | None = None,
        user_agent: str | None = None,
        x_user_id: str | None = None,
        query: str,
        input: dict,
        unknowns: list[str],
        data_partition_id: str | None = None,
    ) -> dict:
        """
            ## Translate policy
        Given an OPA query that should be partially evaluated, return an ElasticSearch request body

        In the body of the request the JSON schema should match "TranslateItem".
        Please note: xuserid, token and datapartitionid are now actively inserted into input request
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
                query (str):
                input (dict):
                unknowns (list[str]):
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if correlation_id is not None:
            headers["correlation-id"] = correlation_id
        if user_agent is not None:
            headers["user-agent"] = user_agent
        if x_user_id is not None:
            headers["x-user-id"] = x_user_id

        request_data = {
            "query": query,
            "input": input,
            "unknowns": unknowns,
        }

        if self.validation:
            validate_data(request_data, TranslateItem)

        url = urljoin(self.base_url, self.service_path, "api/policy/v1/translate")
        response = requests.post(url, headers=headers, json=request_data)
        if not response.ok:
            raise PolicyAPIError(response.text, response.status_code)
        return response.json()

    def get_api_policy_v1_info(
        self,
        *,
        correlation_id: str | None = None,
        user_agent: str | None = None,
        data_partition_id: str | None = None,
    ) -> dict:
        """
            Return Service version information.
        Expected returned JSON is in "InfoOut" schema, which include Services and ServiceDetail schemas.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                correlation_id (str):
                user_agent (str):
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            # Compile - Partially evaluate a query.
        The Compile API allows you to partially evaluate Rego queries and obtain a simplified version of the policy.

        ### Metrics
        When query parameter metrics=true, the API response will include detailed performance metrics from OPA.
        OPA currently supports the following query performance metrics:

            timer_rego_input_parse_ns: time taken (in nanoseconds) to parse the input
            timer_rego_query_parse_ns: time taken (in nanonseconds) to parse the query.
            timer_rego_query_compile_ns: time taken (in nanonseconds) to compile the query.
            timer_rego_query_eval_ns: time taken (in nanonseconds) to evaluate the query.
            timer_rego_module_parse_ns: time taken (in nanoseconds) to parse the input policy module.
            timer_rego_module_compile_ns: time taken (in nanoseconds) to compile the loaded policy modules.
            timer_server_handler_ns: time take (in nanoseconds) to handle the API request.

        ### Instrumentation
        To enable query instrumentation, specify metrics=true and instrument=true query parameters when executing the API call.
        Query instrumentation can help diagnose performance problems, however, it can add significant overhead to query evaluation.
        We recommend leaving query instrumentation off unless you are debugging a performance problem.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                metrics (str): Include report detailed performance metrics on requested on individual API call. Returned inline with the API response
                instrument (str): Include instrumentation data wth detailed performance metrics on requested on individual API call. Returned inline with the API response
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            Experimental tenant API for retrieving OPA bundle config for a data partition.
        These details are read from OPA configmap.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                all_data (str):
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            Experimental tenant API for updating OPA bundle config for a data partition.
        Adding new partitions is not supported in M20.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                service (str):
                polling_min_delay_seconds (str):
                polling_max_delay_seconds (str):
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            Experimental tenant API for deleting tenant OPA bundle config for a data partition.
        Deleting partitions is not supported in M20.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            ## Health check endpoint, which does not depend on OPA.
        This API does not require any headers or authentication.

        The /health endpoint responds with a 200 HTTP status code when the service pod can receive requests.
        The endpoint indicates that the service pod is healthy and reachable.
        It does not indicate that the service is ready to serve requests.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                correlation_id (str):
                user_agent (str):
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            ## Health check endpoint, which depends on OPA being available and healthy.
        This API does not require any headers or authentication.

        ### Possible http return status codes:
        * 200 - no error
        * 501 - not implemented
        * 503 - service not available

        The /ready endpoint responds with a 200 HTTP status code if the overall application works.
        The endpoint indicates that the service is ready to serve requests.
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                correlation_id (str):
                user_agent (str):
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            # Validate Policy
        This API checks to make sure the rego is valid and the naming of the policy package is acceptable.

        If template parameter is True, then the incoming file will automatically replace the following during validation:
        - data_partition
        - DATA_PARTITION
        - name with policy_id without ".rego" suffix
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                policy_id (str):
                template (str):
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            Experimental Backup API.

        Allows downloading the bundle for a data partition.

        Bundle filename will be in the form bundle-`data partition`-`date`.tar.gz
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            Experimental bootstrap API for creating and updating bundle to default.
        This should be used when adding a partition to OSDU.

        Without force:

            * This method is only allowed if the partition doesn't already have a bundle.
            * If the bundle already exists it will return 405 METHOD_NOT_ALLOWED.
            * Policy Service can be configured to ignore force.

        May return:

            * HTTP_202_ACCEPTED - updated
            * HTTP_201_CREATED - created
            * HTTP_405_METHOD_NOT_ALLOWED - not allowed
            * HTTP_424_FAILED_DEPENDENCY - bundle server caused failure
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                force (str):
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
    ) -> dict:
        """
            Return detail configuration details.
        Diagnostic API
            Args:
                data_partition_id (str): identifier of the data partition to query. If None sets by auth session.
                correlation_id (str):
                user_agent (str):
                x_user_id (str): identifier the user in the query
            Returns:
                response data (dict)
            Raises:
                OSDUValidation: if request values are wrong.
                OSDUAPIError: if response is 4XX or 5XX
        """
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
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
