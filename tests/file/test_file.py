from osdu_client.services.file.client import FileClient


def test_file_copy_file_collections(file_api_server, file_client: FileClient):
    file_client.copy_file_collections(
        data_partition_id="text",

    )


def test_file_create_files_metadata(file_api_server, file_client: FileClient):
    file_client.create_files_metadata(
        kind="text",
        acl={
            "viewers": ["example"], "owners": ["example"],
        },
        legal={},
        data={
            "Name": "text",
            "Endian": "BIG",
            "DatasetProperties": {
                "FileSourceInfo": {
                    "FileSource": ""
                }
            }
        },
        id="text",
        ancestry={},
        data_partition_id="text",

    )


def test_file_delete_files_metadata(file_api_server, file_client: FileClient):
    file_client.delete_files_metadata(
        id="text",
        data_partition_id="text",

    )


def test_file_get_file_collections_retrieval_instructions(file_api_server, file_client: FileClient):
    file_client.get_file_collections_retrieval_instructions(
        data_partition_id="text",

    )


def test_file_get_file_collections_storage_instructions(file_api_server, file_client: FileClient):
    file_client.get_file_collections_storage_instructions(
        data_partition_id="text",

    )


def test_file_get_file_list(file_api_server, file_client: FileClient):
    file_client.get_file_list(
        time_from="2024-01-01T00:00:00",
        time_to="2024-01-01T00:00:00",
        page_num=10,
        items=10,
        user_id="text",
        data_partition_id="text",

    )


def test_file_get_file_location(file_api_server, file_client: FileClient):
    file_client.get_file_location(
        file_id="2034ae65-552a-4c04-9e0c-e344ebe40bc7",
        data_partition_id="text",

    )


def test_file_get_file_signed_url(file_api_server, file_client: FileClient):
    file_client.get_file_signed_url(
        srn=["text"],
        data_partition_id="text",

    )


def test_file_get_files_metadata(file_api_server, file_client: FileClient):
    file_client.get_files_metadata(
        id="text",
        data_partition_id="text",

    )


def test_file_get_files_upload_url(file_api_server, file_client: FileClient):
    file_client.get_files_upload_url(
        data_partition_id="text",

    )


def test_file_get_info(file_api_server, file_client: FileClient):
    file_client.get_info(
        data_partition_id="text",

    )


def test_file_get_location(file_api_server, file_client: FileClient):
    file_client.get_location(
        file_id="2034ae65-552a-4c04-9e0c-e344ebe40bc7",
        data_partition_id="text",

    )


def test_file_gets_url_to_download_file(file_api_server, file_client: FileClient):
    file_client.gets_url_to_download_file(
        id="text",
        expiry_time="text",
        data_partition_id="text",

    )
