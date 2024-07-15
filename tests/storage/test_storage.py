from osdu_client.services.storage.client import StorageClient


def test_storage_create_records_delete(storage_api_server, storage_client: StorageClient):
    storage_client.create_records_delete(
        x_collaboration="text",
        data_partition_id="text",

    )

def test_storage_create_replay(storage_api_server, storage_client: StorageClient):
    storage_client.create_replay(
        operation="text",
        filter=[],
        data_partition_id="text",

    )

def test_storage_create_whoami(storage_api_server, storage_client: StorageClient):
    storage_client.create_whoami(
        data_partition_id="text",

    )

def test_storage_delete_record(storage_api_server, storage_client: StorageClient):
    storage_client.delete_record(
        x_collaboration="text",
        id="text",
        data_partition_id="text",

    )

def test_storage_delete_whoami(storage_api_server, storage_client: StorageClient):
    storage_client.delete_whoami(
        data_partition_id="text",

    )

def test_storage_get_info(storage_api_server, storage_client: StorageClient):
    storage_client.get_info(
        data_partition_id="text",

    )

def test_storage_get_liveness_check(storage_api_server, storage_client: StorageClient):
    storage_client.get_liveness_check(
        data_partition_id="text",

    )

def test_storage_get_record(storage_api_server, storage_client: StorageClient):
    storage_client.get_record(
        x_collaboration="text",
        id="text",
        attribute="text",
        data_partition_id="text",

    )

def test_storage_get_record_version(storage_api_server, storage_client: StorageClient):
    storage_client.get_record_version(
        x_collaboration="text",
        id="text",
        version="text",
        attribute="text",
        data_partition_id="text",

    )

def test_storage_get_record_versions(storage_api_server, storage_client: StorageClient):
    storage_client.get_record_versions(
        x_collaboration="text",
        id="text",
        data_partition_id="text",

    )

def test_storage_get_replay_status(storage_api_server, storage_client: StorageClient):
    storage_client.get_replay_status(
        id="text",
        data_partition_id="text",

    )

def test_storage_get_whoami(storage_api_server, storage_client: StorageClient):
    storage_client.get_whoami(
        data_partition_id="text",

    )

def test_storage_head_whoami(storage_api_server, storage_client: StorageClient):
    storage_client.head_whoami(
        data_partition_id="text",

    )

def test_storage_options_whoami(storage_api_server, storage_client: StorageClient):
    storage_client.options_whoami(
        data_partition_id="text",

    )

def test_storage_patch_records(storage_api_server, storage_client: StorageClient):
    storage_client.patch_records(
        query={
            "ids": ["id-1"]
        },
        ops=[{"value": []}],
        x_collaboration="text",
        data_partition_id="text",

    )

def test_storage_patch_whoami(storage_api_server, storage_client: StorageClient):
    storage_client.patch_whoami(
        data_partition_id="text",

    )

def test_storage_purge_record(storage_api_server, storage_client: StorageClient):
    storage_client.purge_record(
        x_collaboration="text",
        id="text",
        data_partition_id="text",

    )

def test_storage_purge_record_versions(storage_api_server, storage_client: StorageClient):
    storage_client.purge_record_versions(
        x_collaboration="text",
        id="text",
        version_ids="text",
        limit="text",
        _form="text",
        data_partition_id="text",

    )

def test_storage_query_records(storage_api_server, storage_client: StorageClient):
    storage_client.query_records(
        records=["text"],
        attributes=["text"],
        x_collaboration="text",
        data_partition_id="text",

    )

def test_storage_query_records_batch(storage_api_server, storage_client: StorageClient):
    storage_client.query_records_batch(
        records=["text"],
        x_collaboration="text",
        frame_of_reference="text",
        data_partition_id="text",

    )

def test_storage_query_records_from_kind(storage_api_server, storage_client: StorageClient):
    storage_client.query_records_from_kind(
        x_collaboration="text",
        cursor="text",
        limit="text",
        kind="text",
        data_partition_id="text",

    )

def test_storage_update_records(storage_api_server, storage_client: StorageClient):
    storage_client.update_records(
        x_collaboration="text",
        skipdupes="text",
        data_partition_id="text",

    )

