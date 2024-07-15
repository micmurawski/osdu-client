from osdu_client.services.wellbore.v3 import WellboreClient


def test_wellbore_create_or_update_wellbore_interval_set(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_or_update_wellbore_interval_set(
        data_partition_id="text",

    )


def test_wellbore_create_or_update_wellbore_v3(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_or_update_wellbore_v3(
        data_partition_id="text",

    )


def test_wellbore_create_or_update_wells(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_or_update_wells(
        data_partition_id="text",

    )


def test_wellbore_create_query_wellbore_welllogs(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_query_wellbore_welllogs(
        wellbore_attribute="text",
        data_partition_id="text",

    )


def test_wellbore_create_query_wellbores_wellboremarkersets(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_query_wellbores_wellboremarkersets(
        wellbore_id="text",
        data_partition_id="text",

    )


def test_wellbore_create_query_wellbores_welllogs(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_query_wellbores_welllogs(
        wellbore_id="text",
        data_partition_id="text",

    )


def test_wellbore_create_wellbore_markerset(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_wellbore_markerset(
        data_partition_id="text",

    )


def test_wellbore_create_wellboretrajectories(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_wellboretrajectories(
        data_partition_id="text",

    )


def test_wellbore_create_wellboretrajectories_data(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_wellboretrajectories_data(
        record_id="text",
        data_partition_id="text",

    )


def test_wellbore_create_wellboretrajectories_sessions(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_wellboretrajectories_sessions(
        mode="overwrite",
        from_version=10,
        meta={},
        time_to_live=10,
        record_id="text",
        data_partition_id="text",

    )


def test_wellbore_create_wellboretrajectories_sessions_data(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_wellboretrajectories_sessions_data(
        record_id="text",
        session_id="text",
        data_partition_id="text",

    )


def test_wellbore_create_welllogs(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_welllogs(
        data_partition_id="text",

    )


def test_wellbore_create_welllogs_data(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_welllogs_data(
        record_id="text",
        data_partition_id="text",

    )


def test_wellbore_create_welllogs_sessions(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.create_welllogs_sessions(
        mode="overwrite",
        from_version=10,
        meta={},
        time_to_live=10,
        record_id="text",
        data_partition_id="text",

    )


def test_wellbore_delete_well(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.delete_well(
        wellid="text",
        data_partition_id="text",

    )


def test_wellbore_delete_wellbore(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.delete_wellbore(
        wellboreid="text",
        data_partition_id="text",

    )


def test_wellbore_delete_wellbore_interval_set(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.delete_wellbore_interval_set(
        wellboreintervalsetsid="text",
        data_partition_id="text",

    )


def test_wellbore_delete_wellbore_markerset(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.delete_wellbore_markerset(
        wellboremarkersetid="text",
        data_partition_id="text",

    )


def test_wellbore_delete_wellboretrajectories(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.delete_wellboretrajectories(
        wellboretrajectoryid="text",
        purge="text",
        data_partition_id="text",

    )


def test_wellbore_delete_welllog(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.delete_welllog(
        welllogid="text",
        purge="text",
        data_partition_id="text",

    )


def test_wellbore_get_about(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_about(
        data_partition_id="text",

    )


def test_wellbore_get_record_session_v3(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_record_session_v3(
        record_id="text",
        session_id="text",
        data_partition_id="text",

    )


def test_wellbore_get_returns_data_specified_version(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_returns_data_specified_version(
        record_id="text",
        version="text",
        offset="text",
        limit="text",
        curves="text",
        describe="text",
        filter="text",
        orient="text",
        data_partition_id="text",

    )


def test_wellbore_get_session(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_session(
        record_id="text",
        session_id="text",
        data_partition_id="text",

    )


def test_wellbore_get_version(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_version(
        data_partition_id="text",

    )


def test_wellbore_get_versions_wellbore_interval_set(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_versions_wellbore_interval_set(
        wellboreintervalsetsid="text",
        data_partition_id="text",

    )


def test_wellbore_get_versions_wellboretrajectory(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_versions_wellboretrajectory(
        wellboretrajectoryid="text",
        data_partition_id="text",

    )


def test_wellbore_get_well(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_well(
        wellid="text",
        data_partition_id="text",

    )


def test_wellbore_get_well_version(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_well_version(
        wellid="text",
        version="text",
        data_partition_id="text",

    )


def test_wellbore_get_well_versions(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_well_versions(
        wellid="text",
        data_partition_id="text",

    )


def test_wellbore_get_wellbore(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_wellbore(
        wellboreid="text",
        data_partition_id="text",

    )


def test_wellbore_get_wellbore_interval_set(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_wellbore_interval_set(
        wellboreintervalsetsid="text",
        data_partition_id="text",

    )


def test_wellbore_get_wellbore_interval_sets_versions(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_wellbore_interval_sets_versions(
        wellboreintervalsetsid="text",
        version="text",
        data_partition_id="text",

    )


def test_wellbore_get_wellbore_versions(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_wellbore_versions(
        wellboreid="text",
        data_partition_id="text",

    )


def test_wellbore_get_wellboremarkerset_versions(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_wellboremarkerset_versions(
        wellboremarkersetid="text",
        data_partition_id="text",

    )


def test_wellbore_get_wellboremarkersets(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_wellboremarkersets(
        wellboremarkersetid="text",
        data_partition_id="text",

    )


def test_wellbore_get_wellboremarkersets_versions(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_wellboremarkersets_versions(
        wellboremarkersetid="text",
        version="text",
        data_partition_id="text",

    )


def test_wellbore_get_wellbores_versions(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_wellbores_versions(
        wellboreid="text",
        version="text",
        data_partition_id="text",

    )


def test_wellbore_get_wellboretrajectories(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_wellboretrajectories(
        wellboretrajectoryid="text",
        data_partition_id="text",

    )


def test_wellbore_get_wellboretrajectories_data(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_wellboretrajectories_data(
        record_id="text",
        offset="text",
        limit="text",
        curves="text",
        describe="text",
        filter="text",
        orient="text",
        data_partition_id="text",

    )


def test_wellbore_get_wellboretrajectories_versions(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_wellboretrajectories_versions(
        wellboretrajectoryid="text",
        version="text",
        data_partition_id="text",

    )


def test_wellbore_get_welllog(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_welllog(
        welllogid="text",
        data_partition_id="text",

    )


def test_wellbore_get_welllog_version(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_welllog_version(
        welllogid="text",
        version="text",
        data_partition_id="text",

    )


def test_wellbore_get_welllog_version_data(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_welllog_version_data(
        record_id="text",
        version="text",
        offset="text",
        limit="text",
        curves="text",
        describe="text",
        filter="text",
        orient="text",
        data_partition_id="text",

    )


def test_wellbore_get_welllog_version_data_statistics(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_welllog_version_data_statistics(
        record_id="text",
        version="text",
        curves="text",
        data_partition_id="text",

    )


def test_wellbore_get_welllog_versions(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_welllog_versions(
        welllogid="text",
        data_partition_id="text",

    )


def test_wellbore_get_welllogs_data(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_welllogs_data(
        record_id="text",
        offset="text",
        limit="text",
        curves="text",
        describe="text",
        filter="text",
        orient="text",
        data_partition_id="text",

    )


def test_wellbore_get_welllogs_data_statistics(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.get_welllogs_data_statistics(
        record_id="text",
        curves="text",
        data_partition_id="text",

    )


def test_wellbore_list_records_sessions_v3(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.list_records_sessions_v3(
        record_id="text",
        data_partition_id="text",

    )


def test_wellbore_list_session_given_record(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.list_session_given_record(
        record_id="text",
        data_partition_id="text",

    )


def test_wellbore_patch_wellboretrajectories_sessions(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.patch_wellboretrajectories_sessions(
        state="commit",
        record_id="text",
        session_id="text",
        data_partition_id="text",

    )


def test_wellbore_query_alpha_query_wellbores(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.query_alpha_query_wellbores(
        names="text",
        data_partition_id="text",

    )


def test_wellbore_query_alpha_query_wellbores_wellboretrajectories(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.query_alpha_query_wellbores_wellboretrajectories(
        wellbore_id="text",
        data_partition_id="text",

    )


def test_wellbore_query_alpha_query_welllogs(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.query_alpha_query_welllogs(
        names="text",
        wellbore_id="text",
        mnemonics="text",
        data_partition_id="text",

    )


def test_wellbore_recognize_family(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.recognize_family(
        label="text",
        description="text",
        log_unit="text",
        data_partition_id="text",

    )


def test_wellbore_send_welllog_sessions_data(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.send_welllog_sessions_data(
        record_id="text",
        session_id="text",
        data_partition_id="text",

    )


def test_wellbore_trigger_welllog_version_data_statistics(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.trigger_welllog_version_data_statistics(
        record_id="text",
        version="text",
        data_partition_id="text",

    )


def test_wellbore_update_log_recognition_upload_catalog(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.update_log_recognition_upload_catalog(
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


def test_wellbore_update_welllogs_sessions(wellbore_api_server, wellbore_client_v3: WellboreClient):
    wellbore_client_v3.update_welllogs_sessions(
        state="commit",
        record_id="text",
        session_id="text",
        data_partition_id="text",

    )
