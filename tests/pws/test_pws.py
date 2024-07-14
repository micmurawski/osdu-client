from osdu_client.services.pws.client import PWSClient

def test_pws_create_projects(pws_api_server, pws_client: PWSClient):
    pws_client.create_projects(
        data_partition_id="text",
        tenant="text",
    )

def test_pws_create_projects_lifecycleevent(pws_api_server, pws_client: PWSClient):
    pws_client.create_projects_lifecycleevent(
        id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_pws_create_projects_resources(pws_api_server, pws_client: PWSClient):
    pws_client.create_projects_resources(
        id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_pws_create_projects_status(pws_api_server, pws_client: PWSClient):
    pws_client.create_projects_status(
        status="text",
        id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_pws_delete_projects_lifecycleevent(pws_api_server, pws_client: PWSClient):
    pws_client.delete_projects_lifecycleevent(
        id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_pws_delete_projects_resources(pws_api_server, pws_client: PWSClient):
    pws_client.delete_projects_resources(
        id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_pws_get_info(pws_api_server, pws_client: PWSClient):
    pws_client.get_info(
        data_partition_id="text",
        tenant="text",
    )

def test_pws_get_liveness_check(pws_api_server, pws_client: PWSClient):
    pws_client.get_liveness_check(
        data_partition_id="text",
        tenant="text",
    )

def test_pws_get_project(pws_api_server, pws_client: PWSClient):
    pws_client.get_project(
        id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_pws_get_projects(pws_api_server, pws_client: PWSClient):
    pws_client.get_projects(
        data_partition_id="text",
        tenant="text",
    )

def test_pws_get_projects_lifecycleevent(pws_api_server, pws_client: PWSClient):
    pws_client.get_projects_lifecycleevent(
        id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_pws_get_projects_resources(pws_api_server, pws_client: PWSClient):
    pws_client.get_projects_resources(
        id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_pws_get_projects_wip_resources(pws_api_server, pws_client: PWSClient):
    pws_client.get_projects_wip_resources(
        id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_pws_get_readiness_check(pws_api_server, pws_client: PWSClient):
    pws_client.get_readiness_check(
        data_partition_id="text",
        tenant="text",
    )

