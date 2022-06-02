from typing import AnyStr, Dict, Union

from ..exceptions import OSDUClientError


class OSDUAPIError(OSDUClientError):
    def __init__(self, status_code: int, message: Union[Dict, AnyStr] = None) -> None:
        self.status_code = status_code
        self.message = message
        super().__init__(self.message, self.status_code)
