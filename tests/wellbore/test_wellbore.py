from osdu_client.services.wellbore.v3 import WellboreClient

def test_wellbore_create_or_update_wellbore_interval_set(wellbore_api_server, wellbore_client: WellboreClient):
    wellbore_client.create_or_update_wellbore_interval_set(
        data_partition_id="text",
        tenant="text",
    )

def test_wellbore_create_or_update_wellbore_v3(wellbore_api_server, wellbore_client: WellboreClient):
    wellbore_client.create_or_update_wellbore_v3(
        data_partition_id="text",
        tenant="text",
    )

def test_wellbore_create_or_update_wells(wellbore_api_server, wellbore_client: WellboreClient):
    wellbore_client.create_or_update_wells(
        data_partition_id="text",
        tenant="text",
    )

def test_wellbore_create_query_wellbore_welllogs(wellbore_api_server, wellbore_client: WellboreClient):
    wellbore_client.create_query_wellbore_welllogs(
        wellbore_attribute="text",
        data_partition_id="text",
        tenant="text",
    )

def test_wellbore_create_query_wellbores_wellboremarkersets(wellbore_api_server, wellbore_client: WellboreClient):
    wellbore_client.create_query_wellbores_wellboremarkersets(
        wellbore_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_wellbore_create_query_wellbores_welllogs(wellbore_api_server, wellbore_client: WellboreClient):
    wellbore_client.create_query_wellbores_welllogs(
        wellbore_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_wellbore_create_wellbore_markerset(wellbore_api_server, wellbore_client: WellboreClient):
    wellbore_client.create_wellbore_markerset(
        data_partition_id="text",
        tenant="text",
    )

def test_wellbore_create_wellboretrajectories(wellbore_api_server, wellbore_client: WellboreClient):
    wellbore_client.create_wellboretrajectories(
        data_partition_id="text",
        tenant="text",
    )

def test_wellbore_create_wellboretrajectories_data(wellbore_api_server, wellbore_client: WellboreClient):
    wellbore_client.create_wellboretrajectories_data(
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

