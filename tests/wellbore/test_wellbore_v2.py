from osdu_client.services.wellbore.v2 import WellboreClient


def test_wellbore_create_alpha_logs_sessions(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.create_alpha_logs_sessions(
        mode="overwrite",
        from_version=10,
        meta={},
        time_to_live=10,
        record_id="text",
        data_partition_id="text",
    )

def test_wellbore_create_or_update_dipset(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.create_or_update_dipset(
        data_partition_id="text",
    )

def test_wellbore_create_or_update_logs(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.create_or_update_logs(
        data_partition_id="text",
    )

def test_wellbore_create_or_update_logsets(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.create_or_update_logsets(
        data_partition_id="text",
    )

def test_wellbore_create_or_update_marker(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.create_or_update_marker(
        data_partition_id="text",
    )

def test_wellbore_create_or_update_trajectories(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.create_or_update_trajectories(
        data_partition_id="text",
    )

def test_wellbore_create_or_update_well(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.create_or_update_well(
        data_partition_id="text",
    )

def test_wellbore_create_or_update_wellbore_v2(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.create_or_update_wellbore_v2(
        data_partition_id="text",
    )

def test_wellbore_create_trajectory_data(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.create_trajectory_data(
        trajectoryid="text",
        orient="text",
        data_partition_id="text",
    )

def test_wellbore_define_dips_dipset(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.define_dips_dipset(
        dipsetid="text",
        data_partition_id="text",
    )

def test_wellbore_delete_dip(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.delete_dip(
        dipsetid="text",
        index="text",
        data_partition_id="text",
    )

def test_wellbore_delete_dipset(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.delete_dipset(
        dipsetid="text",
        recursive=False,
        data_partition_id="text",
    )

def test_wellbore_delete_log(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.delete_log(
        logid="text",
        data_partition_id="text",
    )

def test_wellbore_delete_logset(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.delete_logset(
        logsetid="text",
        recursive=False,
        data_partition_id="text",
    )

def test_wellbore_delete_marker(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.delete_marker(
        markerid="text",
        data_partition_id="text",
    )

def test_wellbore_delete_trajectory(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.delete_trajectory(
        trajectoryid="text",
        data_partition_id="text",
    )

def test_wellbore_delete_well(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.delete_well(
        wellid="text",
        recursive=False,
        data_partition_id="text",
    )

def test_wellbore_delete_wellbores(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.delete_wellbores(
        wellboreid="text",
        recursive=False,
        data_partition_id="text",
    )

def test_wellbore_get_about(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_about(
        data_partition_id="text",
    )

def test_wellbore_get_alpha_logs_data(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_alpha_logs_data(
        record_id="text",
        offset=10,
        limit=10,
        curves="text",
        describe=False,
        filter=["text"],
        orient="text",
        data_partition_id="text",
    )

def test_wellbore_get_alpha_logs_versions_data(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_alpha_logs_versions_data(
        record_id="text",
        version="text",
        offset=10,
        limit=10,
        curves="text",
        describe=False,
        filter=["text"],
        orient="text",
        data_partition_id="text",
    )

def test_wellbore_get_decimated_log(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_decimated_log(
        logid="text",
        quantiles=10,
        start=10,
        stop=10,
        orient="text",
        bulk_path="text",
        data_partition_id="text",
    )

def test_wellbore_get_dip(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_dip(
        dipsetid="text",
        index=10,
        limit=10,
        data_partition_id="text",
    )

def test_wellbore_get_dip_at_index(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_dip_at_index(
        dipsetid="text",
        index="text",
        data_partition_id="text",
    )

def test_wellbore_get_dipset(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_dipset(
        dipsetid="text",
        data_partition_id="text",
    )

def test_wellbore_get_dipsets_versions(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_dipsets_versions(
        dipsetid="text",
        version="text",
        data_partition_id="text",
    )

def test_wellbore_get_log(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_log(
        logid="text",
        data_partition_id="text",
    )

def test_wellbore_get_log_data(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_log_data(
        logid="text",
        orient="text",
        bulk_path="text",
        data_partition_id="text",
    )

def test_wellbore_get_log_statistics(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_log_statistics(
        logid="text",
        bulk_path="text",
        data_partition_id="text",
    )

def test_wellbore_get_log_version(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_log_version(
        logid="text",
        version="text",
        data_partition_id="text",
    )

def test_wellbore_get_log_version_data(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_log_version_data(
        logid="text",
        version="text",
        orient="text",
        bulk_path="text",
        data_partition_id="text",
    )

def test_wellbore_get_log_versions(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_log_versions(
        logid="text",
        data_partition_id="text",
    )

def test_wellbore_get_logset(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_logset(
        logsetid="text",
        data_partition_id="text",
    )

def test_wellbore_get_logset_version(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_logset_version(
        logsetid="text",
        version="text",
        data_partition_id="text",
    )

def test_wellbore_get_logset_versions(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_logset_versions(
        logsetid="text",
        data_partition_id="text",
    )

def test_wellbore_get_marker(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_marker(
        markerid="text",
        data_partition_id="text",
    )

def test_wellbore_get_marker_version(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_marker_version(
        markerid="text",
        version="text",
        data_partition_id="text",
    )

def test_wellbore_get_marker_versions(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_marker_versions(
        markerid="text",
        data_partition_id="text",
    )

def test_wellbore_get_record_session_v2(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_record_session_v2(
        record_id="text",
        session_id="text",
        data_partition_id="text",
    )

def test_wellbore_get_trajectory(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_trajectory(
        trajectoryid="text",
        data_partition_id="text",
    )

def test_wellbore_get_trajectory_data(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_trajectory_data(
        trajectoryid="text",
        channels=["text"],
        orient="text",
        data_partition_id="text",
    )

def test_wellbore_get_trajectory_version(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_trajectory_version(
        trajectoryid="text",
        version="text",
        data_partition_id="text",
    )

def test_wellbore_get_trajectory_version_data(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_trajectory_version_data(
        trajectoryid="text",
        version="text",
        channels=["text"],
        orient="text",
        data_partition_id="text",
    )

def test_wellbore_get_trajectory_versions(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_trajectory_versions(
        trajectoryid="text",
        data_partition_id="text",
    )

def test_wellbore_get_version(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_version(
        data_partition_id="text",
    )

def test_wellbore_get_versions_dipset(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_versions_dipset(
        dipsetid="text",
        data_partition_id="text",
    )

def test_wellbore_get_versions_wellbore(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_versions_wellbore(
        wellboreid="text",
        data_partition_id="text",
    )

def test_wellbore_get_well_v2(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_well_v2(
        wellid="text",
        data_partition_id="text",
    )

def test_wellbore_get_well_version(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_well_version(
        wellid="text",
        version="text",
        data_partition_id="text",
    )

def test_wellbore_get_well_versions_v2(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_well_versions_v2(
        wellid="text",
        data_partition_id="text",
    )

def test_wellbore_get_wellbores(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_wellbores(
        wellboreid="text",
        data_partition_id="text",
    )

def test_wellbore_get_wellbores_versions(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.get_wellbores_versions(
        wellboreid="text",
        version="text",
        data_partition_id="text",
    )

def test_wellbore_insert_dip_in_dipset(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.insert_dip_in_dipset(
        dipsetid="text",
        data_partition_id="text",
    )

def test_wellbore_list_records_sessions_v2(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.list_records_sessions_v2(
        record_id="text",
        data_partition_id="text",
    )

def test_wellbore_patch_alpha_logs_sessions(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.patch_alpha_logs_sessions(
        state="commit",
        record_id="text",
        session_id="text",
        data_partition_id="text",
    )

def test_wellbore_query_dip_from_dipset(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.query_dip_from_dipset(
        dipsetid="text",
        min_reference=10,
        max_reference=10,
        classification="text",
        data_partition_id="text",
    )

def test_wellbore_recognize_family(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.recognize_family(
        label="text",
        description="text",
        log_unit="text",
        data_partition_id="text",
    )

def test_wellbore_send_alpha_logs_sessions_data(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.send_alpha_logs_sessions_data(
        record_id="text",
        session_id="text",
        data_partition_id="text",
    )

def test_wellbore_update_dip(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.update_dip(
        azimuth={
            "value": 10.0,
            "unitKey": "unitKey"
        },
        inclination={
            "value": 10.0,
            "unitKey": "unitKey"
        },
        reference={
            "value": 10.0,
            "unitKey": "unitKey"
        },
        classification="text",
        quality={
            "value": 10.0,
            "unitKey": "unitKey"
        },
        x_coordinate={
            "value": 10.0,
            "unitKey": "unitKey"
        },
        y_coordinate={
            "value": 10.0,
            "unitKey": "unitKey"
        },
        z_coordinate={
            "value": 10.0,
            "unitKey": "unitKey"
        },
        dipsetid="text",
        index="text",
        data_partition_id="text",
    )

def test_wellbore_update_log_recognition_upload_catalog(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.update_log_recognition_upload_catalog(
        acl={
            "owners": [],
            "viewers": []
        },
        data={
            "family_catalog": []
        },
        legal={},
        data_partition_id="text",
    )

def test_wellbore_upload_log_data(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.upload_log_data(
        logid="text",
        orient="text",
        bulk_path="text",
        data_partition_id="text",
    )

def test_wellbore_write_alpha_logs_data(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.write_alpha_logs_data(
        record_id="text",
        data_partition_id="text",
    )

def test_wellbore_write_log_data(wellbore_api_server, wellbore_client_v2: WellboreClient):
    wellbore_client_v2.write_log_data(
        logid="text",
        orient="text",
        bulk_path="text",
        data_partition_id="text",
    )

