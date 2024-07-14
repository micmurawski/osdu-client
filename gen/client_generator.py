import json
import os
import re

import requests

from .helpers import get_path, get_server_url, load_swagger
from .swagger import SwaggerDoc

BASE_DIR = os.path.dirname(__file__)


SERVICES = {
    "Entitlements": "https://community.opengroup.org/osdu/platform/security-and-compliance/entitlements/-/raw/%s/docs/api/entitlements_openapi.yaml?ref_type=heads",
    "SMDS": "https://community.opengroup.org/osdu/platform/domain-data-mgmt-services/seismic/seismic-dms-suite/seismic-store-service/-/raw/%s/app/sdms/docs/api/openapi.osdu.yaml?ref_type=heads",
    "Storage": "https://community.opengroup.org/osdu/platform/system/storage/-/raw/%s/docs/api/storage_openapi.yaml?ref_type=heads",
    "Search": "https://community.opengroup.org/osdu/platform/system/search-service/-/raw/%s/docs/api/search_openapi.yaml?ref_type=heads",
    "Indexer": "https://community.opengroup.org/osdu/platform/system/indexer-service/-/blob/master/docs/api/indexer_openapi.yaml?ref_type=heads",
    "Schema": "https://community.opengroup.org/osdu/platform/system/schema-service/-/raw/master/docs/api/schema_openapi.yaml?ref_type=heads",
    "Register": "https://community.opengroup.org/osdu/platform/system/register/-/blob/master/docs/api/register_openapi.yaml?ref_type=heads",
    "Partition": "https://community.opengroup.org/osdu/platform/system/partition/-/blob/master/docs/api/partition_openapi.yaml?ref_type=heads",
    "PWS": "https://community.opengroup.org/osdu/platform/system/project-and-workflow/-/blob/main/docs/api/openapi.yaml?ref_type=heads",
    "Notification": "https://community.opengroup.org/osdu/platform/system/notification/-/raw/master/docs/api/notification_openapi.yaml?ref_type=heads",
    "File": "https://community.opengroup.org/osdu/platform/system/file/-/raw/master/docs/file-service_openapi.yaml?ref_type=heads",
    "Dataset": "https://community.opengroup.org/osdu/platform/system/dataset/-/raw/master/docs/dataset.swagger.yaml?ref_type=heads",
    "Legal": "https://community.opengroup.org/osdu/platform/security-and-compliance/legal/-/raw/master/docs/api/legal_openapi.yaml?ref_type=heads",
    "Policy": "https://community.opengroup.org/osdu/platform/security-and-compliance/policy/-/raw/master/docs/openapi.yaml?ref_type=heads",
    "Secret": "https://community.opengroup.org/osdu/platform/security-and-compliance/secret/-/raw/main/docs/api/secret_openapi.json?ref_type=heads"
}

INDENT = " "*4

SPECIAL_HEADERS = (
    "data-partition-id",
    "tenant",
)

FORBIDDEN_NAMES = {
    "from": "_form"
}

SIMPLE_TYPES_MAP = {
    'boolean': "bool",
    'string': "str",
    "object": "dict",
    "number": "int",
    "integer": "int",
}

COMPLEX_TYPES = {"array"}
COMPLEX_TYPES_MAP = {
    ("array", "string"): "list[str]",
    ("array", "object"): "list[dict]",
}


def get_type_for_param(param: dict, swagger: dict | None = None) -> str:
    if swagger is None:
        swagger = {}

    if param.get("in") in ("query", "path"):
        return str.__name__

    param_type = param.get("type")
    schema_type = get_path(param, "schema.type", None)
    ref_path = get_path(param, "$ref", get_path(param, "schema.$ref", None))
    all_of = get_path(param, "allOf.0.$ref", None)
    any_of = get_path(param, "anyOf", None)

    
    if any_of:
        types = []
        _list = any_of

        for i in _list:
            obj = get_path(
                swagger,
                i["$ref"][2:],
                None,
                "/"
            )
            _type = obj["type"]
            items_type = get_path(obj, "items.type", "object")

            types.append(
                COMPLEX_TYPES_MAP[(_type, items_type)]
            )
        return "Union[%s]" % ", ".join(types)

    while ref_path or all_of:
        ref_path = ref_path or all_of
        ref = get_path(swagger, ref_path[2:], separator="/", default=None)

        if ref_path.endswith(".json"):
            return dict.__name__

        ref_path = get_path(ref, "$ref", default=None)
        all_of = get_path(ref, "allOf.0.$ref", default=None)
        if not ref_path and not all_of:
            return SIMPLE_TYPES_MAP[ref["type"]]

    if ref_path:
        ref = get_path(swagger, ref_path[2:], separator="/", default=None)
    else:
        ref = None

    if schema_type in SIMPLE_TYPES_MAP:
        return SIMPLE_TYPES_MAP[schema_type]
    elif schema_type in COMPLEX_TYPES:
        items_type_path = get_path(
            param,
            "schema.items.type",
            get_path(
                param,
                "schema.items.$ref",
                None
            )
        )
        while True:
            ref = get_path(swagger, items_type_path[2:], separator="/", default={})

            if isinstance(ref, dict) and "$ref" in ref:
                items_type_path = ref["$ref"]
                continue
            else:
                _type = ref.get("type", items_type_path)
                return COMPLEX_TYPES_MAP[(schema_type, _type)]

    elif param_type in COMPLEX_TYPES:
        items_type = get_path(
            param,
            "schema.items.type",
            default=get_path(
                param,
                "items.type",
                default="object"
            )
        )
        return COMPLEX_TYPES_MAP[(param_type, items_type)]
    elif param_type in SIMPLE_TYPES_MAP:
        return SIMPLE_TYPES_MAP[param_type]
    else:
        raise Exception(param_type, schema_type, ref, param)


no_default = object()


def param_to_function_argument(param: dict, swagger: dict | None = None) -> str:

    if swagger is None:
        swagger = {}

    name = convert_to_snake_case(param["name"])
    _type = get_type_for_param(param, swagger)

    is_required = param.get('required', False)
    _default = param.get('default', None)

    if _default and _default != "null":
        _default = f'"{_default}"'

    if is_required:
        return "%s: %s" % (name, _type)
    return "%s: %s | None = %s" % (name, _type, _default)


def create_headers_block(required_header_params_without_special, optional_header_params_without_special) -> str:
    lines = [
        "headers = self.auth.get_headers()",
        "if data_partition_id:",
        f"{INDENT}headers['data-partition-id'] = data_partition_id",
        "if tenant:",
        f"{INDENT}headers['tenant'] = tenant"
    ]
    if required_header_params_without_special:
        lines.append(
            "headers.update({"
        )
        for header in required_header_params_without_special:
            converted_name = convert_to_snake_case(header['name'])
            lines.append(
                "%s'%s': %s," % (INDENT, header['name'], converted_name)
            )
        lines.append(
            "})"
        )
    for header in optional_header_params_without_special:

        converted_name = convert_to_snake_case(header['name'])
        lines.append(
            "if %s is not None:" % converted_name
        )
        lines.append(
            "%sheaders['%s'] = %s" % (INDENT, header['name'], converted_name)
        )

    return "\n".join(lines)


def create_request_block(
        path: str, method: str, has_params: bool, name: str, has_body: bool
) -> str:
    requests_lines = [
        "url = urljoin(self.base_url, self.service_path, %s)" % path,
        "response = requests.%s(url, headers=headers)" % method,
        "if not response.ok:",
        "%sraise %sAPIError(response.text, response.status_code)" % (INDENT, name),
        "return response.json()"
    ]
    if has_params:
        requests_lines[1] = requests_lines[1][:-1] + ", params=params)"

    if has_body:
        requests_lines[1] = requests_lines[1][:-1] + ", json=request_data)"

    return "\n".join(requests_lines)


PARTS_TO_REPLACE = [
    (" an ", " "),
    (" a ", " "),
    (" the ", " "),
    (" of ", " "),
    ("-", "_"),
    (" ", "_"),
    ("'", ""),
    (".", ""),
    ("/", "_"),
    ("retrieve", "get"),
    (":", "_"),
    ("(", ""),
    (")", ""),
    ("references", "refs"),
    ("reference", "ref"),
    ("application", "app"),
    ("authorization", "auth"),
    ("dms", ""),
    ("all", ""),
    ("get list", "list"),
    ("get_list", "list"),
    ("re_index", "reindex"),
    ("__", "_")
]

STARTS_WITH_PREFERENCES = [
    "reply",
    "soft_delete",
    "create_or_update",
    "refresh",
    "get_latest",
    "get_specific_record",
    "list_registered_apps",
    "acquire",
    "remove",
    "add_user_to_seismic_store_subproject_auth_group",
    "list_users_in_subprojects_role_based_auth_groups",
    "reindex",
    "get_searches_schemainfo_repository",
    "delete_groups_members",
]


def create_method_name_from_summary(
        method: str, summary: str | None, parts_to_replace: list[str] = PARTS_TO_REPLACE
) -> str:
    if summary is not None:
        if " " not in summary:
            summary = convert_to_snake_case(summary)
        else:
            summary = summary.lower()

        for a, b in parts_to_replace:
            summary = summary.replace(a, b)

        summary = summary.rsplit("_and", 1)[0]

        summary = summary.split(" (", 1)[0]
        summary = convert_to_snake_case(summary)

        if method.lower() == "get" and not summary.startswith("get") and not summary.startswith("list"):
            summary = f"get_{summary}"

        return summary
    return ""


def create_method_name_from_path(method: str, name_parts: list[str], parts_to_replace: list[str] = PARTS_TO_REPLACE) -> str:
    if not name_parts:
        return ""
    if name_parts[0].startswith("query") or name_parts[0].startswith("list"):
        result = "_".join(name_parts)

        for a, b in parts_to_replace:
            result = result.replace(a, b)
        return result

    if method == "get":
        result = "get_"+"_".join(name_parts)
    elif method == "post":
        result = "create_"+"_".join(name_parts)
    elif method in ("put", "update"):
        result = "update_"+"_".join(name_parts)
    else:
        result = method+"_"+"_".join(name_parts)

    for a, b in parts_to_replace:
        result = result.replace(a, b)

    return result


def update_method_name_map(method: str, path: str, name: str, summary: str, method_names_file: str, description: str = "") -> str:
    data = json.load(open(method_names_file, "r"))
    data[f"{method.lower()}:{path}"] = [name, summary, description]
    json.dump(data, open(method_names_file, "w"))


def get_name_from_name_map(method: str, path: str, method_names_file: str):
    data = json.load(open(method_names_file, "r"))
    result = data.get(f"{method.lower()}:{path}")
    if result is None:
        return result
    return result[0]


def create_method_name(method: str, path: str, name_parts: list[str], swagger: dict, method_names_file: str) -> str:
    # try:
    summary = swagger["paths"][path][method].get("summary")
    description = swagger["paths"][path][method].get("description", "")
    # except TypeError as e:
    #    print(name_parts, path)
    #    raise e
    name = get_name_from_name_map(method, path, method_names_file)

    if name:
        return name

    from_summary = create_method_name_from_summary(method, summary)
    from_path = create_method_name_from_path(method, name_parts)

    for pref in STARTS_WITH_PREFERENCES:
        if from_summary.startswith(pref):
            result = from_summary
            break
        if from_path.startswith(pref):
            result = from_path
            break

    if from_summary != "" and len(from_summary) < len(from_path):
        result = from_summary
    else:
        result = from_path

    update_method_name_map(method, path, result, summary, method_names_file, description)
    return result


def create_params_block(
    required_query_params,
    optional_query_params
) -> str:
    lines = []
    if not optional_query_params and not required_query_params:
        return ""
    elif not required_query_params:
        lines.append("params = {}")
    else:
        lines.append(
            "params = {"
        )
        for qp in required_query_params:
            converted_name = convert_to_snake_case(qp['name'])
            lines.append(
                "%s'%s': %s," % (INDENT, qp['name'], converted_name)
            )
        lines.append("}")

    for qp in optional_query_params:
        converted_name = convert_to_snake_case(qp['name'])
        lines.append(
            "if %s is not None:" % converted_name
        )
        lines.append(
            "%sparams['%s'] = %s" % (INDENT, qp['name'], converted_name)
        )
    return "\n".join(lines)


def get_body_params(swagger, params: list[dict], request_body: dict | None = None) -> tuple[list[dict], list[dict]]:

    if request_body is None:
        request_body = {}

    required = []
    not_required = []
    for p in params:
        if p.get("required", False) and p['in'] == 'body':
            required.append(p)
        elif p["in"] == "body":
            not_required.append(p)

    schema_path = get_path(
        request_body,
        "content.application/json.schema.$ref",
        get_path(
            request_body,
            "$ref",
            None
        )
    )

    if schema_path is None:
        return required, not_required

    schema = get_path(swagger, schema_path[2:], separator="/")

    if "properties" not in schema:
        schema_path = get_path(
            schema,
            "content.application/json.schema.$ref"
        )
        schema = get_path(swagger, schema_path[2:], separator="/")

    for k, v in schema["properties"].items():
        if k in schema.get("required", []):
            required.append(
                dict(**v, name=k, required=True)
            )
        else:
            not_required.append(
                dict(**v, name=k, required=False)
            )

    return required, not_required


def create_validation_block(path: str, method: str, swagger: dict, name: str) -> str:

    request_body = swagger["paths"][path][method].get("requestBody", None)
    if request_body is None:
        return ""

    schema_path = get_path(request_body, "content.application/json.schema.$ref", get_path(request_body, "$ref", None))
    if schema_path:
        model_class = schema_path.rsplit("/", 1)[-1]
        lines = [
            "if self.validation:",
            "%svalidate_data(request_data, %s, %sAPIError)" % (INDENT, model_class, name),
        ]
        return "\n".join(lines)
    return ""


def create_body_block(required: list[dict], not_required: list[dict]) -> str:
    lines = []

    if not required and not not_required:
        return ""

    if not required:
        lines.append("request_data = {}")
    else:
        lines.append(
            "request_data = {"
        )
        for p in required:
            converted_name = convert_to_snake_case(p['name'])
            lines.append(
                "%s'%s': %s," % (INDENT, p['name'], converted_name)
            )

        lines.append("}")

    for p in not_required:
        converted_name = convert_to_snake_case(p['name'])

        lines.append(
            "if %s is not None:" % converted_name
        )

        lines.append(
            "%srequest_data['%s'] = %s" % (INDENT, p['name'], converted_name)
        )

    return "\n".join(lines)


def create_method(swagger: dict, name: str, method: str, path: str, path_template: str, class_name: str) -> str:
    params = swagger["paths"][path][method].get("parameters", [])
    request_body = swagger["paths"][path][method].get("requestBody", None)

    body_required, body_not_required = get_body_params(swagger, params, request_body)

    sig = create_method_sig(swagger, name, params, body_required, body_not_required) + "\n"

    body = create_method_body(path, method, params, body_required,
                              body_not_required, path_template, class_name, swagger)
    result = sig
    for line in body.split("\n"):
        result += INDENT+line + "\n"

    return result


def parse_request_body(swagger: dict, props: list[dict]) -> list[str]:
    result = []
    for prop in props:
        result.append(
            param_to_function_argument(prop, swagger)
        )
    return result


def create_method_sig(swagger: dict, name: str, params: list[str], body_required: list[str], body_not_required: list[str]) -> str:
    path_params = [
        p for p in params if p['name'] not in SPECIAL_HEADERS and p["in"] != "body"
    ]
    elements = [name, ]

    sig = ""
    _input_parameters_strings = []

    if body_required:
        _input_parameters_strings += parse_request_body(swagger, body_required)

    if body_not_required:
        _input_parameters_strings += parse_request_body(swagger, body_not_required)

    _input_parameters_strings += [param_to_function_argument(p) for p in path_params]

    if _input_parameters_strings:
        sig += ", ".join(_input_parameters_strings)

    if sig:
        elements.append(sig)

    try:
        if len(elements) > 1:
            sig = "def %s(self, *, %s, data_partition_id: str | None = None, tenant: str | None = None) -> dict:" % tuple(elements)
        else:
            sig = "def %s(self, data_partition_id: str | None = None, tenant: str | None = None) -> dict:" % tuple(elements)
        return sig
    except Exception as e:
        raise Exception(elements, len(elements)) from e


def create_method_body(path: str, method: str, params: dict,  body_required: list[dict], body_not_required: list[dict], path_template: str, name: str, swagger: dict = None) -> str:
    if swagger is None:
        swagger = {}

    path_params_names = [convert_to_snake_case(p['name']) for p in params if p['in'] == 'path']

    path_template = path_template[1:]

    if len(path_params_names) == 0:
        path_template = f'"{path_template}"'
    elif len(path_params_names) == 1:
        path_template = f'"{path_template}" % {path_params_names[0]}'
    else:
        path_template = f'"{path_template}" % ({", ".join(path_params_names)})'

    required_query_params = [p for p in params if p['in'] == 'query' and p.get('required', False)]
    optional_query_params = [p for p in params if p['in'] == 'query' and not p.get('required', False)]
    required_header_params_without_special = [p for p in params if p['in'] ==
                                              'header' and p['name'] not in SPECIAL_HEADERS and p.get('required', False)]
    optional_header_params_without_special = [p for p in params if p['in'] ==
                                              'header' and p['name'] not in SPECIAL_HEADERS and not p.get('required', False)]

    has_body = body_required or body_not_required
    has_params = required_query_params or optional_query_params
    lines = filter(lambda x: x != "", [
        create_headers_block(required_header_params_without_special, optional_header_params_without_special),
        create_params_block(required_query_params, optional_query_params),
        create_body_block(body_required, body_not_required),
        create_validation_block(path, method, swagger, name),
        create_request_block(path_template, method, has_params, name, has_body)
    ])

    return "\n\n".join(lines)


def convert_to_snake_case(name):
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower().replace("-", "_")
    if result in FORBIDDEN_NAMES:
        return FORBIDDEN_NAMES[result]
    return result


def create_imports(swagger: SwaggerDoc, name: str, version: str, num_of_versions: int) -> str:
    imported_models = []
    for path in swagger.paths[version]:
        for method in swagger["paths"][path]:
            try:
                request_body = swagger["paths"][path][method].get("requestBody", None)
            except AttributeError as e:
                raise e
            if request_body is None:
                continue

            schema_path = get_path(request_body, "content.application/json.schema.$ref", None)
            if schema_path:
                model_class = schema_path.rsplit("/", 1)[-1]
                imported_models.append(model_class)

            schema_path = get_path(request_body, "$ref", None)
            if schema_path:
                model_class = schema_path.rsplit("/", 1)[-1]
                imported_models.append(model_class)

    lines = [
        "from __future__ import annotations\n",
        "import requests\n",
        "from osdu_client.utils import urljoin",
        "from osdu_client.services.base import OSDUAPIClient",
        "from osdu_client.exceptions import OSDUAPIError",
    ]

    if version != "common" and num_of_versions > 1:
        lines.pop(3)
        lines.append(
            f"from osdu_client.services.{name.lower()}.common import {name}CommonClient",
        )

    if imported_models:
        lines.append(
            "from osdu_client.validation import validate_data"
        )
        lines.append(
            "\nfrom .models import ("
        )
        lines += [INDENT+i+"," for i in imported_models]
        lines.append(")")

    return "\n".join(lines)


def create_definition(name: str, swagger: dict, version: str, num_of_versions: int) -> str:

    url = get_server_url(swagger)
    lines = [
        "class %sAPIError(OSDUAPIError):" % name,
        "%spass" % INDENT,
        "class %sClient(OSDUAPIClient):" % name,
        '%sservice_path = "%s"' % (INDENT, url)
    ]
    if version == "common" and num_of_versions > 1:
        lines[-2] = "class %sCommonClient(OSDUAPIClient):" % name
    elif version != "common" and num_of_versions > 1:
        lines[-2] = "class %sClient(%sCommonClient):" % (name, name)
    return "\n".join(lines)


def create__init__(name: str, versions: list[str], module_path: str):

    versions = [v for v in versions if v != "common"]

    if len(versions) < 2:
        with open(os.path.join(module_path, "__init__.py"), "w") as f:
            f.write(f"from .client import {name}Client #NOQA\n")
        return

    default_version = max(versions, key=lambda x: int(x[1:]))
    with open(os.path.join(module_path, "__init__.py"), "w") as f:
        for version in versions:

            if version == "common":
                continue

            f.write(f"from .{version} import {name}Client as {name}Client{version.upper()} #NOQA\n")

        f.write(f'DEFAULT_VERSION="{default_version}"\n')
        f.write("VERSIONS={\n")

        for version in versions:
            f.write('%s"%s": %sClient%s,\n' % (INDENT, version, name, version.upper()))

        f.write("}\n")


def generate_clients(url: str, name: str, branch: str = "master", dump_file_path: str = "dump.py"):
    module_path = os.path.dirname(dump_file_path)

    class_name = name
    if url.startswith("http"):

        url = url % branch
        response = requests.get(url)

        if not response.ok:
            raise Exception(response.text)
        swagger = load_swagger(response.text)
    else:
        swagger = load_swagger(open(url).read())

    swagger = SwaggerDoc(swagger)
    # generating methods
    create__init__(class_name, swagger.versions, module_path)
    for version in swagger.versions:

        if len(swagger.versions) == 1:
            method_names_file = os.path.join(module_path, "method_names.json")
            if not os.path.exists(method_names_file):
                json.dump({}, open(method_names_file, "w"))

        else:
            dump_file_path = os.path.join(module_path, version + ".py")
            method_names_file = os.path.join(module_path, f"method_names_{version}.json")
            if not os.path.exists(method_names_file):
                json.dump({}, open(method_names_file, "w"))

        with open(dump_file_path, "w") as f:
            f.write(create_imports(swagger, class_name, version, len(swagger.versions))+"\n\n")
            f.write(
                create_definition(class_name, swagger, version, len(swagger.versions)),
            )
            f.write("\n")
            method_names = set()
            for path in swagger.paths[version]:
                path_template = re.sub(r'\{[a-zA-Z0-9&_\.-]*\}', "%s", path, flags=re.DOTALL)
                name_parts = []
                for element in filter(lambda x: x not in ("", "_ah"), path.replace(":", "/").split("/")):

                    if not (element.startswith("{") and element.endswith("}")):
                        name_parts.append(convert_to_snake_case(element))

                for method in swagger["paths"][path]:

                    method_name = create_method_name(method, path, name_parts, swagger, method_names_file)

                    if method_name in method_names:
                        raise Exception(
                            f"method name duplicate: {method_name} {method} {path}. Check {method_names_file}")

                    method_names.add(method_name)
                    method_body = create_method(
                        swagger,
                        method_name,
                        method,
                        path,
                        path_template,
                        class_name

                    )
                    for line in method_body.splitlines():
                        f.write(INDENT+line+"\n")
                    f.write("\n")
