from auth import AuthInterface

from osdu_client.services import get_service_client


class OSDUAPI:
    @staticmethod
    def client(service_name, auth_backend: AuthInterface = None):
        return get_service_client(service_name)(auth_backend)
