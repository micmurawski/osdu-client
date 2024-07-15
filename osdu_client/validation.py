from __future__ import annotations

from pydantic import BaseModel, ValidationError

from osdu_client.exceptions import OSDUAPIError
from osdu_client.utils import convert_to_snake_case


def parse_loc(loc: list[str]) -> str:
    _loc = []
    for i, el in enumerate(loc):
        if i == 0:
            _loc.append(convert_to_snake_case(el))
        else:
            _loc.append(str(el))
    return ".".join(_loc)


def validate_data(data: dict, schema: BaseModel, exception: OSDUAPIError = OSDUAPIError):
    try:
        schema(**data)
    except ValidationError as e:
        messages = []
        for error in e.errors(include_url=False):
            _type = error["type"]
            loc = parse_loc(error["loc"])
            msg = error["msg"]
            _input = error["input"]
            messages.append(f"{msg} {_type} in {loc}. Input: {_input}")
        raise exception(messages)
