
class OSDUClientError(Exception):
    pass


class OSDUAPIError(OSDUClientError):
    pass


class OSDUValidation(OSDUClientError):
    pass