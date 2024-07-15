from osdu_client.services.welldelivery.client import WellDeliveryClient


def test_welldelivery_create_or_update_storage(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.create_or_update_storage(
        entity={},
        type="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_delete_entity(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.delete_entity(
        type="text",
        id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_delete_storage_version(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.delete_storage_version(
        type="text",
        id="text",
        version="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_activity_plans_by_well(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_activity_plans_by_well(
        well_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_bha_runs_v1_by_hole_section(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_bha_runs_v1_by_hole_section(
        hole_section_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_bha_runs_v1_by_wellbore_actual(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_bha_runs_v1_by_wellbore_actual(
        wellbore_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_entity(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_entity(
        type="text",
        id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_entity_version(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_entity_version(
        type="text",
        id="text",
        version="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_hole_sections_v1_by_wellbore(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_hole_sections_v1_by_wellbore(
        wellbore_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_operations_reports_by_time_range(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_operations_reports_by_time_range(
        start_time="text",
        end_time="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_operations_reports_with_refs_by_operations_report_id(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_operations_reports_with_refs_by_operations_report_id(
        operations_report_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_storage_version(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_storage_version(
        type="text",
        id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_version_number_list_actual_well(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_version_number_list_actual_well(
        name="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_version_number_list_actual_wellbore(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_version_number_list_actual_wellbore(
        well_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_version_number_list_planned_well(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_version_number_list_planned_well(
        name="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_version_number_list_planned_wellbore(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_version_number_list_planned_wellbore(
        well_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_version_number_list_well_activity_program(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_version_number_list_well_activity_program(
        well_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_well_activity_program(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_well_activity_program(
        well_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_well_activity_program_version(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_well_activity_program_version(
        well_id="text",
        wap_version="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_well_activity_program_version_with_refs(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_well_activity_program_version_with_refs(
        well_id="text",
        wap_version="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_well_activity_program_with_refs(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_well_activity_program_with_refs(
        well_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_well_activity_programs_full_content_by_well(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_well_activity_programs_full_content_by_well(
        well_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_well_by_name_actual(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_well_by_name_actual(
        name="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_well_by_name_planned(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_well_by_name_planned(
        name="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_well_version_by_name_actual(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_well_version_by_name_actual(
        name="text",
        version="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_well_version_by_name_planned(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_well_version_by_name_planned(
        name="text",
        version="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_wellbore_actual(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_wellbore_actual(
        well_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_wellbore_fluids_programs(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_wellbore_fluids_programs(
        wellbore_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_wellbore_fluids_reports(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_wellbore_fluids_reports(
        wellbore_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_wellbore_operations_reports(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_wellbore_operations_reports(
        wellbore_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_wellbore_operations_reports_latest(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_wellbore_operations_reports_latest(
        wellbore_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_wellbore_planned(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_wellbore_planned(
        well_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_wellbore_version_actual(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_wellbore_version_actual(
        well_id="text",
        wellbore_version="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_get_wellbore_version_planned(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.get_wellbore_version_planned(
        well_id="text",
        wellbore_version="text",
        data_partition_id="text",
        tenant="text",
    )

def test_welldelivery_purge_entity(welldelivery_api_server, welldelivery_client: WellDeliveryClient):
    welldelivery_client.purge_entity(
        type="text",
        id="text",
        data_partition_id="text",
        tenant="text",
    )

