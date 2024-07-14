from __future__ import annotations

import requests

from osdu_client.utils import urljoin
from osdu_client.services.base import OSDUAPIClient
from osdu_client.exceptions import OSDUAPIError


class WellDeliveryAPIError(OSDUAPIError):
    pass


class WellDeliveryClient(OSDUAPIClient):
    service_path = "/api/well-delivery"

    def create_or_update_storage(
        self,
        *,
        entity: dict,
        type: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        data = {
            "Entity": entity,
        }

        url = urljoin(self.base_url, self.service_path, "storage/v1/%s" % type)
        response = requests.put(url, headers=headers, json=data)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_entity(
        self,
        *,
        type: str,
        id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "storage/v1/%s/%s" % (type, id))
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def delete_entity(
        self,
        *,
        type: str,
        id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(self.base_url, self.service_path, "storage/v1/%s/%s" % (type, id))
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_entity_version(
        self,
        *,
        type: str,
        id: str,
        version: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "storage/v1/%s/%s/%s" % (type, id, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def delete_storage_version(
        self,
        *,
        type: str,
        id: str,
        version: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "storage/v1/%s/%s/%s" % (type, id, version),
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_storage_version(
        self,
        *,
        type: str,
        id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "storage/v1/%s/versions/%s" % (type, id)
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def purge_entity(
        self,
        *,
        type: str,
        id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "storage/v1/%s/%s:purge" % (type, id)
        )
        response = requests.delete(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_version_number_list_well_activity_program(
        self,
        *,
        well_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wellActivityPrograms/v1/versions/by_well/%s" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_activity_program(
        self,
        *,
        well_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wellActivityPrograms/v1/by_well/%s" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_activity_program_version(
        self,
        *,
        well_id: str,
        wap_version: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wellActivityPrograms/v1/by_well/%s/%s" % (well_id, wap_version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_activity_program_with_refs(
        self,
        *,
        well_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wellActivityPrograms/v1/reference_tree/by_well/%s" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_activity_program_version_with_refs(
        self,
        *,
        well_id: str,
        wap_version: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wellActivityPrograms/v1/reference_tree/by_well/%s/%s"
            % (well_id, wap_version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_activity_programs_full_content_by_well(
        self,
        *,
        well_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wellActivityPrograms/v1/full_content/by_well/%s" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_activity_plans_by_well(
        self,
        *,
        well_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "activityPlans/v1/by_well/%s" % well_id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_version_number_list_actual_well(
        self,
        *,
        name: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wells/v1/versions/by_name/%s:actual" % name,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_by_name_actual(
        self,
        *,
        name: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "wells/v1/by_name/%s:actual" % name
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_version_by_name_actual(
        self,
        *,
        name: str,
        version: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wells/v1/by_name/%s/%s:actual" % (name, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_version_number_list_planned_well(
        self,
        *,
        name: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wells/v1/versions/by_name/%s:planned" % name,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_by_name_planned(
        self,
        *,
        name: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "wells/v1/by_name/%s:planned" % name
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_well_version_by_name_planned(
        self,
        *,
        name: str,
        version: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wells/v1/by_name/%s/%s:planned" % (name, version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_version_number_list_actual_wellbore(
        self,
        *,
        well_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wellbores/v1/versions/by_well/%s:actual" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_actual(
        self,
        *,
        well_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url, self.service_path, "wellbores/v1/by_well/%s:actual" % well_id
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_version_actual(
        self,
        *,
        well_id: str,
        wellbore_version: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wellbores/v1/by_well/%s/%s:actual" % (well_id, wellbore_version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_version_number_list_planned_wellbore(
        self,
        *,
        well_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wellbores/v1/versions/by_well/%s:planned" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_planned(
        self,
        *,
        well_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wellbores/v1/by_well/%s:planned" % well_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_version_planned(
        self,
        *,
        well_id: str,
        wellbore_version: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "wellbores/v1/by_well/%s/%s:planned" % (well_id, wellbore_version),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_hole_sections_v1_by_wellbore(
        self,
        *,
        wellbore_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "holeSections/v1/by_wellbore/%s" % wellbore_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_bha_runs_v1_by_hole_section(
        self,
        *,
        hole_section_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "bhaRuns/v1/by_holeSection/%s" % hole_section_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_bha_runs_v1_by_wellbore_actual(
        self,
        *,
        wellbore_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "bhaRuns/v1/by_wellbore/%s:actual" % wellbore_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def query_v1_by_well_batch(
        self,
        *,
        well_ids: list[str],
        content__type: str,
        type: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant
        headers.update(
            {
                "Content-Type": content__type,
            }
        )

        data = {
            "well_ids": well_ids,
        }

        url = urljoin(
            self.base_url, self.service_path, "query/v1/by_well/%s:batch" % type
        )
        response = requests.post(url, headers=headers, json=data)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def query_v1_by_wellbore_planned(
        self,
        *,
        type: str,
        wellbore_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "query/v1/%s/by_wellbore/%s:planned" % (type, wellbore_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def query_v1_by_wellbore_actual(
        self,
        *,
        type: str,
        wellbore_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "query/v1/%s/by_wellbore/%s:actual" % (type, wellbore_id),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_fluids_programs(
        self,
        *,
        wellbore_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "fluidsPrograms/v1/by_wellbore/%s" % wellbore_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_operations_reports(
        self,
        *,
        wellbore_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "operationsReports/v1/by_wellbore/%s" % wellbore_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_operations_reports_latest(
        self,
        *,
        wellbore_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "operationsReports/v1/latest/by_wellbore/%s" % wellbore_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_operations_reports_by_time_range(
        self,
        *,
        start_time: str,
        end_time: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "operationsReports/v1/by_timeRange/%s/%s" % (start_time, end_time),
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_operations_reports_with_refs_by_operations_report_id(
        self,
        *,
        operations_report_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "operationsReports/v1/reference_tree/by_operationsReport/%s"
            % operations_report_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()

    def get_wellbore_fluids_reports(
        self,
        *,
        wellbore_id: str,
        data_partition_id: str | None = None,
        tenant: str | None = None,
    ) -> dict:
        headers = self.auth.get_headers()
        if data_partition_id:
            headers["data-partition-id"] = data_partition_id
        if tenant:
            headers["tenant"] = tenant

        url = urljoin(
            self.base_url,
            self.service_path,
            "fluidsReports/v1/by_wellbore/%s" % wellbore_id,
        )
        response = requests.get(url, headers=headers)
        if not response.ok:
            raise WellDeliveryAPIError(response.text, response.status_code)
        return response.json()
