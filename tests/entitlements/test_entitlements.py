from osdu_client.services.entitlements.client import EntitlementsClient

def test_entitlements_add_member(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.add_member(
        add_member_dto={},
        group_email="text",
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_create_group(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.create_group(
        group_info_dto={},
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_delete_group(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.delete_group(
        group_email="text",
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_delete_member(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.delete_member(
        member_email="text",
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_delete_member_from_group(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.delete_member_from_group(
        group_email="text",
        member_email="text",
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_get_count_group_members(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.get_count_group_members(
        group_email="text",
        role="text",
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_get_groups(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.get_groups(
        on_behalf_of="text",
        role_required="text",
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_get_groups_members(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.get_groups_members(
        group_email="text",
        role="text",
        include_type="text",
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_get_info(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.get_info(
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_get_liveness_check(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.get_liveness_check(
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_get_members_groups(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.get_members_groups(
        member_email="text",
        type={},
        appid="text",
        role_required="text",
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_get_readiness_check(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.get_readiness_check(
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_initiate_tenant(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.initiate_tenant(
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_list_partition_groups(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.list_partition_groups(
        type="text",
        cursor="text",
        limit="text",
        data_partition_id="text",
        tenant="text",
    )

def test_entitlements_patch_groups(entitlements_api_server, entitlements_client: EntitlementsClient):
    entitlements_client.patch_groups(
        update_group_request=[{}],
        group_email="text",
        data_partition_id="text",
        tenant="text",
    )

