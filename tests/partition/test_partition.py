from osdu_client.services.partition.client import PartitionClient

def test_partition_create_partitions(partition_api_server, partition_client: PartitionClient):
    partition_client.create_partitions(
        properties={},
        partition_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_partition_delete_partition(partition_api_server, partition_client: PartitionClient):
    partition_client.delete_partition(
        partition_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_partition_get_info(partition_api_server, partition_client: PartitionClient):
    partition_client.get_info(
        data_partition_id="text",
        tenant="text",
    )

def test_partition_get_liveness_check(partition_api_server, partition_client: PartitionClient):
    partition_client.get_liveness_check(
        data_partition_id="text",
        tenant="text",
    )

def test_partition_get_partition(partition_api_server, partition_client: PartitionClient):
    partition_client.get_partition(
        partition_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_partition_list_partitions(partition_api_server, partition_client: PartitionClient):
    partition_client.list_partitions(
        data_partition_id="text",
        tenant="text",
    )

def test_partition_update_partitions(partition_api_server, partition_client: PartitionClient):
    partition_client.update_partitions(
        properties={},
        partition_id="text",
        data_partition_id="text",
        tenant="text",
    )

