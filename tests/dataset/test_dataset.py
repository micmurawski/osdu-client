from osdu_client.services.dataset.client import DatasetClient


def test_dataset_create_or_update_dataset_registry(dataset_api_server, dataset_client: DatasetClient):
    dataset_client.create_or_update_dataset_registry(
        dataset_registries=[{"acl": {}, "data": {}}],
        data_partition_id="text",
    )


def test_dataset_get_dataset_registries(dataset_api_server, dataset_client: DatasetClient):
    dataset_client.get_dataset_registries(
        dataset_registry_ids=["text"],
        data_partition_id="text",
    )


def test_dataset_get_dataset_registry(dataset_api_server, dataset_client: DatasetClient):
    dataset_client.get_dataset_registry(
        id="text",
        data_partition_id="text",
    )


def test_dataset_get_info(dataset_api_server, dataset_client: DatasetClient):
    dataset_client.get_info(
        data_partition_id="text",
    )


def test_dataset_get_liveness_check(dataset_api_server, dataset_client: DatasetClient):
    dataset_client.get_liveness_check(
        data_partition_id="text",
    )


def test_dataset_get_retrieval_instructions(dataset_api_server, dataset_client: DatasetClient):
    dataset_client.get_retrieval_instructions(
        id="text",
        expiry_time="text",
        data_partition_id="text",
    )


def test_dataset_get_retrieval_instructions_for_multiple_datasets(dataset_api_server, dataset_client: DatasetClient):
    dataset_client.get_retrieval_instructions_for_multiple_datasets(
        dataset_registry_ids=["text"],
        expiry_time="text",
        data_partition_id="text",
    )


def test_dataset_get_revoke_url(dataset_api_server, dataset_client: DatasetClient):
    dataset_client.get_revoke_url(
        kind_sub_type="text",
        data_partition_id="text",
    )


def test_dataset_get_storage_instructions(dataset_api_server, dataset_client: DatasetClient):
    dataset_client.get_storage_instructions(
        kind_sub_type="text",
        expiry_time="text",
        data_partition_id="text",
    )
