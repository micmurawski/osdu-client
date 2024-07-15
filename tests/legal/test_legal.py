from osdu_client.services.legal.client import LegalClient


def test_legal_create_legaltag(legal_api_server, legal_client: LegalClient):
    legal_client.create_legaltag(
        name="text",
        description="text",
        properties={},
        data_partition_id="text",

    )

def test_legal_delete_legaltag(legal_api_server, legal_client: LegalClient):
    legal_client.delete_legaltag(
        name="text",
        data_partition_id="text",

    )

def test_legal_get_batch_legaltags(legal_api_server, legal_client: LegalClient):
    legal_client.get_batch_legaltags(
        names=["text"],
        data_partition_id="text",

    )

def test_legal_get_info(legal_api_server, legal_client: LegalClient):
    legal_client.get_info(
        data_partition_id="text",

    )

def test_legal_get_legaltag(legal_api_server, legal_client: LegalClient):
    legal_client.get_legaltag(
        name="text",
        data_partition_id="text",

    )

def test_legal_get_legaltag_compliance_job_status(legal_api_server, legal_client: LegalClient):
    legal_client.get_legaltag_compliance_job_status(
        data_partition_id="text",

    )

def test_legal_get_legaltags_properties(legal_api_server, legal_client: LegalClient):
    legal_client.get_legaltags_properties(
        data_partition_id="text",

    )

def test_legal_get_liveness_check(legal_api_server, legal_client: LegalClient):
    legal_client.get_liveness_check(
        data_partition_id="text",

    )

def test_legal_get_readiness_check(legal_api_server, legal_client: LegalClient):
    legal_client.get_readiness_check(
        data_partition_id="text",

    )

def test_legal_list_legaltags(legal_api_server, legal_client: LegalClient):
    legal_client.list_legaltags(
        valid="text",
        data_partition_id="text",

    )

def test_legal_query_legaltags(legal_api_server, legal_client: LegalClient):
    legal_client.query_legaltags(
        query_list=["text"],
        operator_list=["text"],
        sort_by="text",
        sort_order="text",
        limit=10,
        valid="text",
        data_partition_id="text",

    )

def test_legal_update_legaltag(legal_api_server, legal_client: LegalClient):
    legal_client.update_legaltag(
        name="text",
        contract_id="text",
        description="text",
        expiration_date="2024-01-01T00:00:00+00:00",
        extension_properties={},
        data_partition_id="text",

    )

def test_legal_validate_legaltags(legal_api_server, legal_client: LegalClient):
    legal_client.validate_legaltags(
        names=["text"],
        data_partition_id="text",

    )

