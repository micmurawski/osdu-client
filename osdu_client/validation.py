from pydantic import BaseModel, ValidationError
from osdu_client.exceptions import OSDUAPIError
from osdu_client.utils import convert_to_snake_case


def validate_data(data: dict, schema: BaseModel, exception: OSDUAPIError = OSDUAPIError):
    try:
        schema(**data)
    except ValidationError as e:
        messages = []
        for error in e.errors(include_url=False):
            _type =  error["type"]
            loc = ".".join(i for i in error["loc"])
            msg = error["msg"]
            _input = error["input"]
            messages.append(f"{msg} {_type} in {loc}. Input: {_input}")
        raise exception(messages)
