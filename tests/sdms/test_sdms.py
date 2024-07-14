from osdu_client.services.sdms.client import SDMSClient


def test_sdms_acquire_lock_for_dataset(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.acquire_lock_for_dataset(
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        path="text",
        datasetid="text",
        openmode="text",
        wid="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_check_datasets_list(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.check_datasets_list(
        datasets=["text"],
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_compute_and_get_size_dataset(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.compute_and_get_size_dataset(
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        datasetid="text",
        path="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_copy_dataset(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.copy_dataset(
        impersonation_token_context="text",
        sdpath_from="text",
        sdpath_to="text",
        lock="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_create_impersonation_token(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.create_impersonation_token(
        resources=[dict(resource="example-resource")],
        metadata={},
        user_token="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_create_imptoken(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.create_imptoken(
        token="text",
        resources=[dict(resource="example-resource")],
        refresh_url="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_create_new_subproject(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.create_new_subproject(
        admin="text",
        storage_class="text",
        storage_location="text",
        access_policy="uniform",
        acls={},
        ltag="text",
        subprojectid="text",
        tenantid="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_delete_all_datasets_in_subproject(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.delete_all_datasets_in_subproject(
        filter={},
        path="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_delete_dataset(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.delete_dataset(
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        path="text",
        datasetid="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_delete_subproject(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.delete_subproject(
        subprojectid="text",
        tenantid="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_delete_user(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.delete_user(
        email="text",
        path="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_app(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_app(
        sdpath="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_app_trusted(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_app_trusted(
        sdpath="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_content_list(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_content_list(
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        path="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_dataset(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_dataset(
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        path="text",
        datasetid="text",
        seismicmeta="text",
        translate_user_info="text",
        record_version="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_dataset_access_permissions(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_dataset_access_permissions(
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        path="text",
        datasetid="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_datasets_sizes(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_datasets_sizes(
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        datasetid="text",
        path="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_download_connection_credentials_string(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_download_connection_credentials_string(
        impersonation_token_context="text",
        sdpath="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_gcs_access_token(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_gcs_access_token(
        impersonation_token_context="text",
        sdpath="text",
        readonly="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_info(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_info(
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_operation_bulk_delete_status(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_operation_bulk_delete_status(
        operation_id="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_subproject_metadata(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_subproject_metadata(
        subprojectid="text",
        tenantid="text",
        translate_user_info="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_svcstatus(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_svcstatus(
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_svcstatus_access(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_svcstatus_access(
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_tenant(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_tenant(
        tenantid="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_tenant_sdpath(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_tenant_sdpath(
        datapartition="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_upload_connection_credential_string(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_upload_connection_credential_string(
        impersonation_token_context="text",
        sdpath="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_user(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_user(
        sdpath="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_get_user_roles(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.get_user_roles(
        sdpath="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_list_datasets_in_subproject(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.list_datasets_in_subproject(
        type="text",
        gtags=["text"],
        search="text",
        filter={},
        limit=10,
        cursor="text",
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        translate_user_info="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_list_datasets_sizes(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.list_datasets_sizes(
        datasets=["text"],
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_list_storage_tiers(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.list_storage_tiers(
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_list_subprojects_in_tenant(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.list_subprojects_in_tenant(
        tenantid="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_ls(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.ls(
        impersonation_token_context="text",
        sdpath="text",
        wmode="text",
        limit="text",
        cursor="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_ls_post(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.ls_post(
        sdpath="text",
        wmode="text",
        limit=10,
        cursor="text",
        impersonation_token_context="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_patch_dataset_metadata(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.patch_dataset_metadata(
        dataset_new_name="text",
        metadata={},
        filemetadata={},
        last_modified_date="text",
        gtags=["text"],
        ltag="text",
        readonly=False,
        status="text",
        seismicmeta={},
        openzgy_v1={},
        segy_v1={},
        acls={},
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        path="text",
        datasetid="text",
        close="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_patch_imptoken(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.patch_imptoken(
        token="text",
        refresh_url="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_patch_subprojects_metadata(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.patch_subprojects_metadata(
        access_policy="text",
        acls={},
        ltag="text",
        tenantid="text",
        subprojectid="text",
        recursive="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_refresh_impersonation_token(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.refresh_impersonation_token(
        impersonation_token="text",
        impersonation_token_context="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_refresh_imptoken(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.refresh_imptoken(
        token="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_register_app(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.register_app(
        email="text",
        sdpath="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_register_new_dataset(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.register_new_dataset(
        type="text",
        gtags=["text"],
        seismicmeta={},
        openzgy_v1={},
        segy_v1={},
        acls={},
        impersonation_token_context="text",
        ltag="text",
        tenantid="text",
        subprojectid="text",
        path="text",
        datasetid="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_register_tenant(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.register_tenant(
        gcpid="text",
        esd="text",
        default_acls="text",
        tenantid="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_remove_lock_associated_with_dataset(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.remove_lock_associated_with_dataset(
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        path="text",
        datasetid="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_set_app_trusted(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.set_app_trusted(
        email="text",
        sdpath="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_update_user(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.update_user(
        email="text",
        path="text",
        group="viewer",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_upsert_tags_to_dataset(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.upsert_tags_to_dataset(
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        path="text",
        datasetid="text",
        gtag="text",
        data_partition_id="text",
        tenant="text",
    )


def test_sdms_validate_ctag(sdms_api_server, sdms_client: SDMSClient):
    sdms_client.validate_ctag(
        impersonation_token_context="text",
        tenantid="text",
        subprojectid="text",
        path="text",
        datasetid="text",
        ctag="text",
        data_partition_id="text",
        tenant="text",
    )
