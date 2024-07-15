from osdu_client.services.rafs.v2 import RAFSClient


def test_rafs_create_or_update_masterdata_records(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.create_or_update_masterdata_records(
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_create_or_update_pvt_records(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.create_or_update_pvt_records(
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_create_or_update_sa_records(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.create_or_update_sa_records(
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_create_or_update_sar_records(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.create_or_update_sar_records(
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_info(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_info(
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_masterdata_record(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_masterdata_record(
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_masterdata_record_version(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_masterdata_record_version(
        version="text",
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_masterdata_record_versions(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_masterdata_record_versions(
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_metrics(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_metrics(
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_pvt_data(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_pvt_data(
        record_id="text",
        analysis_type="text",
        dataset_id="text",
        columns_filter="text",
        rows_filter="text",
        columns_aggregation="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_pvt_record(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_pvt_record(
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_pvt_record_version(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_pvt_record_version(
        version="text",
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_pvt_record_versions(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_pvt_record_versions(
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_sa_content_schema(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_sa_content_schema(
        analysistype="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_sa_data(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_sa_data(
        record_id="text",
        analysis_type="text",
        dataset_id="text",
        columns_filter="text",
        rows_filter="text",
        columns_aggregation="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_sa_record(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_sa_record(
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_sa_record_version(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_sa_record_version(
        version="text",
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_sa_record_versions(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_sa_record_versions(
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_sa_types(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_sa_types(
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_sar_record(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_sar_record(
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_sar_record_specific_version(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_sar_record_specific_version(
        version="text",
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_sar_record_versions(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_sar_record_versions(
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_get_sar_source_data(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.get_sar_source_data(
        record_id="text",
        version="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_query_sa(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.query_sa(
        analysis_type="text",
        columns_filter="text",
        rows_filter="text",
        columns_aggregation="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_search_sa_data(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.search_sa_data(
        analysis_type="text",
        columns_filter="text",
        rows_filter="text",
        columns_aggregation="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_soft_delete_masterdata_record(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.soft_delete_masterdata_record(
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_soft_delete_pvt_record(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.soft_delete_pvt_record(
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_soft_delete_sa_record(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.soft_delete_sa_record(
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_soft_delete_sar_record(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.soft_delete_sar_record(
        record_id="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_upload_pvt_data(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.upload_pvt_data(
        record_id="text",
        analysis_type="text",
        data_partition_id="text",
        tenant="text",
    )

def test_rafs_upload_sa_data(rafs_api_server, rafs_client_v2: RAFSClient):
    rafs_client_v2.upload_sa_data(
        record_id="text",
        analysis_type="text",
        data_partition_id="text",
        tenant="text",
    )

