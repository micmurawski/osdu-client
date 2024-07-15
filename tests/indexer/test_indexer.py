from osdu_client.services.indexer.client import IndexerClient


def test_indexer_delete_index(indexer_api_server, indexer_client: IndexerClient):
    indexer_client.delete_index(
        kind="text",
        data_partition_id="text",
        tenant="text",
    )

def test_indexer_get_info(indexer_api_server, indexer_client: IndexerClient):
    indexer_client.get_info(
        data_partition_id="text",
        tenant="text",
    )

def test_indexer_get_liveness_check(indexer_api_server, indexer_client: IndexerClient):
    indexer_client.get_liveness_check(
        data_partition_id="text",
        tenant="text",
    )

def test_indexer_get_readiness_check(indexer_api_server, indexer_client: IndexerClient):
    indexer_client.get_readiness_check(
        data_partition_id="text",
        tenant="text",
    )

def test_indexer_provision_partition(indexer_api_server, indexer_client: IndexerClient):
    indexer_client.provision_partition(
        data_partition_id="text",
        tenant="text",
    )

def test_indexer_reindex_kind(indexer_api_server, indexer_client: IndexerClient):
    indexer_client.reindex_kind(
        kind="text",
        cursor="text",
        force_clean="text",
        data_partition_id="text",
        tenant="text",
    )

def test_indexer_reindex_partition(indexer_api_server, indexer_client: IndexerClient):
    indexer_client.reindex_partition(
        force_clean="text",
        data_partition_id="text",
        tenant="text",
    )

def test_indexer_reindex_records(indexer_api_server, indexer_client: IndexerClient):
    indexer_client.reindex_records(
        record_ids=["text"],
        data_partition_id="text",
        tenant="text",
    )

