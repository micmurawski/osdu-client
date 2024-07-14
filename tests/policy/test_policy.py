from osdu_client.services.policy.client import PolicyClient

def test_policy_bootstrap(policy_api_server, policy_client: PolicyClient):
    policy_client.bootstrap(
        force="text",
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_create_api_policy_v1_compile(policy_api_server, policy_client: PolicyClient):
    policy_client.create_api_policy_v1_compile(
        metrics="text",
        instrument="text",
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_create_or_update_partition_policy(policy_api_server, policy_client: PolicyClient):
    policy_client.create_or_update_partition_policy(
        policy_id="text",
        data_partition="text",
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_delete_partition_policy(policy_api_server, policy_client: PolicyClient):
    policy_client.delete_partition_policy(
        policy_id="text",
        data_partition="text",
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_delete_tenant(policy_api_server, policy_client: PolicyClient):
    policy_client.delete_tenant(
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_evaluate_policy(policy_api_server, policy_client: PolicyClient):
    policy_client.evaluate_policy(
        policy_id="text",
        include_auth="text",
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_get_api_policy_v1_config(policy_api_server, policy_client: PolicyClient):
    policy_client.get_api_policy_v1_config(
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_get_api_policy_v1_info(policy_api_server, policy_client: PolicyClient):
    policy_client.get_api_policy_v1_info(
        correlation_id="text",
        user_agent="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_get_api_policy_v1_policies(policy_api_server, policy_client: PolicyClient):
    policy_client.get_api_policy_v1_policies(
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_get_api_policy_v1_policies_osdu_partition(policy_api_server, policy_client: PolicyClient):
    policy_client.get_api_policy_v1_policies_osdu_partition(
        policy_id="text",
        data_partition="text",
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_get_backup(policy_api_server, policy_client: PolicyClient):
    policy_client.get_backup(
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_get_fetch_instance_policy(policy_api_server, policy_client: PolicyClient):
    policy_client.get_fetch_instance_policy(
        policy_id="text",
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_get_fetch_policy(policy_api_server, policy_client: PolicyClient):
    policy_client.get_fetch_policy(
        policy_id="text",
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_get_health(policy_api_server, policy_client: PolicyClient):
    policy_client.get_health(
        correlation_id="text",
        user_agent="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_get_ready(policy_api_server, policy_client: PolicyClient):
    policy_client.get_ready(
        correlation_id="text",
        user_agent="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_get_tenant(policy_api_server, policy_client: PolicyClient):
    policy_client.get_tenant(
        all_data="text",
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_home_page(policy_api_server, policy_client: PolicyClient):
    policy_client.home_page(
        correlation_id="text",
        user_agent="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_translate_policy_api(policy_api_server, policy_client: PolicyClient):
    policy_client.translate_policy_api(
        query="text",
        input={},
        unknowns=["text"],
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_update_tenant(policy_api_server, policy_client: PolicyClient):
    policy_client.update_tenant(
        service="text",
        polling_min_delay_seconds="text",
        polling_max_delay_seconds="text",
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_policy_validate_policy(policy_api_server, policy_client: PolicyClient):
    policy_client.validate_policy(
        policy_id="text",
        template="text",
        correlation_id="text",
        user_agent="text",
        x_user_id="text",
        data_partition_id="text",
        tenant="text",
    )

