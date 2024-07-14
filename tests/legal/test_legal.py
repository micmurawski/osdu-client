from osdu_client.services.legal.client import LegalClient

def test_legal_create_legaltags(legal_api_server, legal_client: LegalClient):
    legal_client.create_legaltags(
        name="text",
        description="text",
        properties={},
        data_partition_id="text",
        tenant="text",
    )

def test_legal_create_legaltags_batch_get(legal_api_server, legal_client: LegalClient):
    legal_client.create_legaltags_batch_get(
        names=["text"],
        data_partition_id="text",
        tenant="text",
    )

def test_legal_create_legaltags_query(legal_api_server, legal_client: LegalClient):
    legal_client.create_legaltags_query(
        query_list=["text"],
        operator_list=["text"],
        sort_by="text",
        sort_order="text",
        limit=10,
        valid="text",
        data_partition_id="text",
        tenant="text",
    )

def test_legal_create_legaltags_validate(legal_api_server, legal_client: LegalClient):
    legal_client.create_legaltags_validate(
        names=["text"],
        data_partition_id="text",
        tenant="text",
    )

def test_legal_delete_legaltags(legal_api_server, legal_client: LegalClient):
    legal_client.delete_legaltags(
        name="text",
        data_partition_id="text",
        tenant="text",
    )

def test_legal_get_info(legal_api_server, legal_client: LegalClient):
    legal_client.get_info(
        data_partition_id="text",
        tenant="text",
    )

def test_legal_get_jobs_update_legal_tag_status(legal_api_server, legal_client: LegalClient):
    legal_client.get_jobs_update_legal_tag_status(
        data_partition_id="text",
        tenant="text",
    )

def test_legal_get_legaltag(legal_api_server, legal_client: LegalClient):
    legal_client.get_legaltag(
        name="text",
        data_partition_id="text",
        tenant="text",
    )

def test_legal_get_legaltags_properties(legal_api_server, legal_client: LegalClient):
    legal_client.get_legaltags_properties(
        data_partition_id="text",
        tenant="text",
    )

def test_legal_get_liveness_check(legal_api_server, legal_client: LegalClient):
    legal_client.get_liveness_check(
        data_partition_id="text",
        tenant="text",
    )

def test_legal_get_readiness_check(legal_api_server, legal_client: LegalClient):
    legal_client.get_readiness_check(
        data_partition_id="text",
        tenant="text",
    )

def test_legal_list_legaltags(legal_api_server, legal_client: LegalClient):
    legal_client.list_legaltags(
        valid="text",
        data_partition_id="text",
        tenant="text",
    )

def test_legal_update_legaltags(legal_api_server, legal_client: LegalClient):
    legal_client.update_legaltags(
        name="text",
        contract_id="text",
        description="text",
        expiration_date="text",
        extension_properties={},
        data_partition_id="text",
        tenant="text",
    )

