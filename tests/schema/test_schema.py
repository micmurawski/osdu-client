from osdu_client.services.schema.client import SchemaClient


def test_schema_create_schema(schema_api_server, schema_client: SchemaClient):
    schema_client.create_schema(
        schema_info={
            "schemaIdentity": {
                "source": "source",
                "entityType": "entityType",
                "authority": "authority",
                "schemaVersionMajor": 1,
                "schemaVersionMinor": 1,
                "schemaVersionPatch": 1
            },
            "status": "PUBLISHED"
        },
        schema={},
        data_partition_id="text",
        tenant="text",
    )


def test_schema_get_info(schema_api_server, schema_client: SchemaClient):
    schema_client.get_info(
        data_partition_id="text",
        tenant="text",
    )


def test_schema_get_liveness_check(schema_api_server, schema_client: SchemaClient):
    schema_client.get_liveness_check(
        data_partition_id="text",
        tenant="text",
    )


def test_schema_get_schema(schema_api_server, schema_client: SchemaClient):
    schema_client.get_schema(
        id="text",
        data_partition_id="text",
        tenant="text",
    )


def test_schema_search_schemas(schema_api_server, schema_client: SchemaClient):
    schema_client.search_schemas(
        authority="text",
        source="text",
        entity_type="text",
        schema_version_major="text",
        schema_version_minor="text",
        schema_version_patch="text",
        status="text",
        scope="text",
        latest_version="text",
        limit="text",
        offset="text",
        data_partition_id="text",
        tenant="text",
    )


def test_schema_update_schema(schema_api_server, schema_client: SchemaClient):
    schema_client.update_schema(
        schema_info={
            "schemaIdentity": {
                "source": "source",
                "entityType": "entityType",
                "authority": "authority",
                "schemaVersionMajor": 1,
                "schemaVersionMinor": 1,
                "schemaVersionPatch": 1
            },
            "status": "PUBLISHED"
        },
        schema={},
        data_partition_id="text",
        tenant="text",
    )


def test_schema_update_schemas_system(schema_api_server, schema_client: SchemaClient):
    schema_client.update_schemas_system(
        schema_info={
            "schemaIdentity": {
                "source": "source",
                "entityType": "entityType",
                "authority": "authority",
                "schemaVersionMajor": 1,
                "schemaVersionMinor": 1,
                "schemaVersionPatch": 1
            },
            "status": "PUBLISHED"
        },
        schema={},
        data_partition_id="text",
        tenant="text",
    )
