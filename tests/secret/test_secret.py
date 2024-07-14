from osdu_client.services.secret.client import SecretClient

def test_secret_create_secrets(secret_api_server, secret_client: SecretClient):
    secret_client.create_secrets(
        id="text",
        key="text",
        value="text",
        created_at="text",
        enabled=False,
        data_partition_id="text",
        tenant="text",
    )

def test_secret_create_secrets_get(secret_api_server, secret_client: SecretClient):
    secret_client.create_secrets_get(
        data_partition_id="text",
        tenant="text",
    )

def test_secret_create_secrets_recover(secret_api_server, secret_client: SecretClient):
    secret_client.create_secrets_recover(
        secret_name="text",
        data_partition_id="text",
        tenant="text",
    )

def test_secret_delete_secret(secret_api_server, secret_client: SecretClient):
    secret_client.delete_secret(
        secret_name="text",
        data_partition_id="text",
        tenant="text",
    )

def test_secret_get_health(secret_api_server, secret_client: SecretClient):
    secret_client.get_health(
        data_partition_id="text",
        tenant="text",
    )

def test_secret_get_info(secret_api_server, secret_client: SecretClient):
    secret_client.get_info(
        data_partition_id="text",
        tenant="text",
    )

def test_secret_get_secret(secret_api_server, secret_client: SecretClient):
    secret_client.get_secret(
        secret_name="text",
        data_partition_id="text",
        tenant="text",
    )

def test_secret_get_secrets_deleted(secret_api_server, secret_client: SecretClient):
    secret_client.get_secrets_deleted(
        secret_name="text",
        data_partition_id="text",
        tenant="text",
    )

def test_secret_list_secrets(secret_api_server, secret_client: SecretClient):
    secret_client.list_secrets(
        data_partition_id="text",
        tenant="text",
    )

def test_secret_update_secret(secret_api_server, secret_client: SecretClient):
    secret_client.update_secret(
        id="text",
        key="text",
        value="text",
        created_at="text",
        enabled=False,
        secret_name="text",
        data_partition_id="text",
        tenant="text",
    )

