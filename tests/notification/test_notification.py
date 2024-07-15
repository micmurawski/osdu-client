from osdu_client.services.notification.client import NotificationClient


def test_notification_get_info(notification_api_server, notification_client: NotificationClient):
    notification_client.get_info(
        data_partition_id="text",

    )

def test_notification_record_changed(notification_api_server, notification_client: NotificationClient):
    notification_client.record_changed(
        data_partition_id="text",

    )

