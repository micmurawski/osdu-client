from jsonschema import RefResolver, Draft7Validator, RefResolutionError
from .services.schema_api import SchemaAPIClient, SchemaAPIError


class OSDURefResolver(RefResolver):
    def __init__(self, *args, schema_client: SchemaAPIClient, **kwargs) -> None:
        self.schema_client = schema_client
        super().__init__(*args, **kwargs)

    def resolve_remote(self, uri):
        if uri.startswith('/SOMETHING'):
            try:
                return self.schema_client.get_schema(id=uri)
            except SchemaAPIError as e:
                raise RefResolutionError(str(e)) from e
        else:
            try:
                return super().resolve_remote(uri)
            except RefResolutionError as e:
                _id = uri.rpslit('/', 1)[-1]

def validate(record, schema, schema_client):
    resolver = OSDURefResolver(None, referrer=None, store={}, schema_client=schema_client)
    validator = Draft7Validator(schema, resolver=resolver)
    return validator.iter_errors(record)
