from pydantic import BaseModel, ValidationError
from osdu_client.exceptions import OSDUAPIError
from osdu_client.utils import convert_to_snake_case


def validate_data(data: dict, schema: BaseModel, exception: OSDUAPIError = OSDUAPIError):
    try:
        schema(**data)
    except ValidationError as e:
        for error in e.errors(include_url=False):
            _type =  error["type"]
            loc = ".".join(convert_to_snake_case(str(i)) for i in error["loc"])
            msg = error["msg"]
            _input = error["input"]
            message = f"{msg} {_type} in {loc}. Input: {_input}"
            raise exception(message)
