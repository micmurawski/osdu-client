from osdu_client.services.register.client import RegisterClient


def test_register_create_action(register_api_server, register_client: RegisterClient):
    register_client.create_action(
        id="text",
        name="text",
        description="text",
        contact_email="text",
        img="https://example.url",
        url="https://example.url",
        filter={},
        data_partition_id="text",

    )

def test_register_create_action_get(register_api_server, register_client: RegisterClient):
    register_client.create_action_get(
        id="text",
        kind="text",
        acl={},
        legal={},
        data={},
        data_partition_id="text",

    )

def test_register_create_action_test(register_api_server, register_client: RegisterClient):
    register_client.create_action_test(
        action={},
        test_payload={},
        data_partition_id="text",

    )

def test_register_create_ddms(register_api_server, register_client: RegisterClient):
    register_client.create_ddms(
        id="text",
        name="text",
        description="text",
        contact_email="text",
        interfaces=[{
            "schema": {}
        }],
        data_partition_id="text",

    )

def test_register_create_subscription(register_api_server, register_client: RegisterClient):
    register_client.create_subscription(
        name="text",
        description="text",
        topic="text",
        push_endpoint="text",
        secret={},
        data_partition_id="text",

    )

def test_register_delete_action(register_api_server, register_client: RegisterClient):
    register_client.delete_action(
        id="text",
        data_partition_id="text",

    )

def test_register_delete_ddms(register_api_server, register_client: RegisterClient):
    register_client.delete_ddms(
        id="text",
        data_partition_id="text",

    )

def test_register_delete_subscription(register_api_server, register_client: RegisterClient):
    register_client.delete_subscription(
        id="text",
        data_partition_id="text",

    )

def test_register_get_action(register_api_server, register_client: RegisterClient):
    register_client.get_action(
        id="text",
        data_partition_id="text",

    )

def test_register_get_d(register_api_server, register_client: RegisterClient):
    register_client.get_d(
        id="text",
        type="text",
        localid="text",
        data_partition_id="text",

    )

def test_register_get_ddms(register_api_server, register_client: RegisterClient):
    register_client.get_ddms(
        id="text",
        data_partition_id="text",

    )

def test_register_get_info(register_api_server, register_client: RegisterClient):
    register_client.get_info(
        data_partition_id="text",

    )

def test_register_get_subscription(register_api_server, register_client: RegisterClient):
    register_client.get_subscription(
        id="text",
        data_partition_id="text",

    )

def test_register_get_topics(register_api_server, register_client: RegisterClient):
    register_client.get_topics(
        data_partition_id="text",

    )

def test_register_query_ddms(register_api_server, register_client: RegisterClient):
    register_client.query_ddms(
        type="text",
        data_partition_id="text",

    )

def test_register_update_subscription_secret(register_api_server, register_client: RegisterClient):
    register_client.update_subscription_secret(
        secret_type="HMAC",
        value={},
        id="text",
        data_partition_id="text",

    )

