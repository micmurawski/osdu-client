from __future__ import annotations

import os
import shutil
from importlib import import_module

from gen.helpers import put_inits
from osdu_client.client import get_service_client

INDENT = " "*4

TYPE_DEFAULTS = {
    str: '"text"',
    str | None: '"text"',
    'str | None': '"text"',
    'str': '"text"',
    int | None: '10',
    'int | None': '10',
    dict: '{}',
    'dict': '{}',
    bool | None: 'False',
    'list[str]': '["text"]',
    'list[dict]': '[{}]',
    dict | None: '{}',
    'dict | None': '{}',
    'list[str] | None': '["text"]'
}


def create_conftest(module_path: str, name: str):
    module = import_module(f"osdu_client.services.{name.lower()}")
    versions = getattr(module, "VERSIONS", {})

    import_lines = [
        "import pytest",
        "import os",
        "from tests.utils import create_swagger_server",
        "from osdu_client.auth import AuthBackendInterface",
        "from osdu_client.client import OSDUAPI, OSDUAPIClient",
        "import requests_mock",
        "\n",
        "BASE_DIR = os.path.dirname(__file__)",
        "\n"
    ]

    body = [
        '@pytest.fixture(scope="session")',
        "def auth_backend() -> AuthBackendInterface:",
        f"{INDENT}class AuthSession(AuthBackendInterface):",
        f'{INDENT*2}base_url = "https://base.url"',
        f'{INDENT*2}default_data_partition_id = "osdu"',
        f'{INDENT*2}',
        '%sauthorization_header = {"Authorization": "Bearer access_token"}' % (INDENT*2),
        "\n",
        f"{INDENT*2}def get_sd_connection_params(self):",
        "%sreturn {}" % (INDENT*3),
        "\n",
        f"{INDENT}return AuthSession()",
        "\n\n",
        '@pytest.fixture(scope="session")',
        f"def {name.lower()}_api_server():",
        f"{INDENT}with requests_mock.Mocker() as mocker:",
        f'{INDENT*2}create_swagger_server(mocker, os.path.join(BASE_DIR, "swagger.yaml"))',
        f'{INDENT*2}yield mocker',
        "\n\n",
        '@pytest.fixture(scope="session")',
        f"def {name.lower()}_client(auth_backend: AuthBackendInterface) -> OSDUAPIClient:",
        f'{INDENT}return OSDUAPI.client("{name.lower()}", auth_backend=auth_backend)',
    ]
    if versions:
        body = body[:-3]
        for version in versions:
            body += [
                '@pytest.fixture(scope="session")',
                f"def {name.lower()}_client_{version}(auth_backend: AuthBackendInterface) -> OSDUAPIClient:",
                f'{INDENT}return OSDUAPI.client("{name.lower()}", auth_backend=auth_backend, version="{version}")',
                "\n"
            ]

    with open(os.path.join(module_path, "conftest.py"), "w") as file:
        for line in import_lines:
            file.write(line+"\n")
        for line in body:
            file.write(line+"\n")


def create_tests(
    name: str,
    tests_path: str,
):
    module = import_module(f"osdu_client.services.{name.lower()}")
    versions = getattr(module, "VERSIONS", {})
    if versions:
        for version, client_class in versions.items():

            methods = [
                getattr(client_class, method_name)
                for method_name in dir(client_class)
                if callable(getattr(client_class, method_name)) and hasattr(
                    getattr(client_class, method_name), "__annotations__"
                ) and method_name not in ("__init__") and getattr(client_class, method_name).__class__.__name__ == "function"
            ]
            import_template = '\n'.join([
                "from {module_path} import {class_name}",
                "\n",
            ])
            test_template = '\n'.join([
                "def test_{module}_{method_name}({module}_api_server, {module}_client_{version}: {class_name}):",
                "{indent}{module}_client_{version}.{method_name}("
            ])
            versioned_tests_path = tests_path.replace(name.lower()+".py", f"{name.lower()}_{version}.py")
            with open(versioned_tests_path, "w") as f:
                _import = import_template.format(module=name, class_name=client_class.__name__,
                                                 module_path=client_class.__module__)
                f.write(_import)
                for method in methods:
                    test = test_template.format(
                        module=name.lower(),
                        class_name=client_class.__name__,
                        method_name=method.__name__,
                        indent=INDENT,
                        version=version
                    )
                    for k, v in method.__annotations__.items():
                        if k != "return":
                            test += "\n"+(INDENT*2)+f'{k}={TYPE_DEFAULTS[v]},'
                    test += f"\n{INDENT})\n\n"
                    f.write(test)

    else:
        client_class = get_service_client(name.lower())
        methods = [
            getattr(client_class, method_name)
            for method_name in dir(client_class)
            if callable(getattr(client_class, method_name)) and hasattr(
                getattr(client_class, method_name), "__annotations__"
            ) and method_name not in ("__init__") and getattr(client_class, method_name).__class__.__name__ == "function"
        ]

        import_template = '\n'.join([
            "from {module_path} import {class_name}",
            "\n",
        ])
        test_template = '\n'.join([
            "def test_{module}_{method_name}({module}_api_server, {module}_client: {class_name}):",
            "{indent}{module}_client.{method_name}("
        ])

        with open(tests_path, "w") as f:
            _import = import_template.format(module=name, class_name=client_class.__name__,
                                             module_path=client_class.__module__)
            f.write(_import)
            for method in methods:
                test = test_template.format(
                    module=name.lower(),
                    class_name=client_class.__name__,
                    method_name=method.__name__,
                    indent=INDENT,
                )
                for k, v in method.__annotations__.items():
                    if k != "return":
                        test += "\n"+(INDENT*2)+f'{k}={TYPE_DEFAULTS[v]},'
                test += f"\n{INDENT})\n\n"
                f.write(test)


def generate_tests(
    name: str,
    tests_dir: str,
    code_path: str
):
    module_path = os.path.join(tests_dir, name.lower())
    test_path = os.path.join(tests_dir, name.lower(), f"test_{name.lower()}.py")
    os.makedirs(module_path, exist_ok=True)
    put_inits(module_path)
    shutil.copy(os.path.join(code_path, "swagger.yaml"), os.path.join(module_path, "swagger.yaml"))
    create_conftest(module_path, name)
    create_tests(name, test_path)


if __name__ == "__main__":

    tests_path = "./tests"
    SERVICES = {
        "Entitlements": "https://community.opengroup.org/osdu/platform/security-and-compliance/entitlements/-/raw/master/docs/api/entitlements_openapi.yaml?ref_type=heads",
        "SDMS": "https://community.opengroup.org/osdu/platform/domain-data-mgmt-services/seismic/seismic-dms-suite/seismic-store-service/-/raw/master/app/sdms/docs/api/openapi.osdu.yaml?ref_type=heads",
        "Storage": "https://community.opengroup.org/osdu/platform/system/storage/-/raw/master/docs/api/storage_openapi.yaml?ref_type=heads",
        "Search": "https://community.opengroup.org/osdu/platform/system/search-service/-/raw/master/docs/api/search_openapi.yaml?ref_type=heads",
        "Indexer": "https://community.opengroup.org/osdu/platform/system/indexer-service/-/raw/master/docs/api/indexer_openapi.yaml?ref_type=heads",
        "Schema": "https://community.opengroup.org/osdu/platform/system/schema-service/-/raw/master/docs/api/schema_openapi.yaml?ref_type=heads",
        "Register": "https://community.opengroup.org/osdu/platform/system/register/-/raw/master/docs/api/register_openapi.yaml?ref_type=heads",
        "Partition": "https://community.opengroup.org/osdu/platform/system/partition/-/raw/master/docs/api/partition_openapi.yaml?ref_type=heads",
        "PWS": "https://community.opengroup.org/osdu/platform/system/project-and-workflow/-/raw/main/docs/api/openapi.yaml?ref_type=heads",
        "Notification": "https://community.opengroup.org/osdu/platform/system/notification/-/raw/master/docs/api/notification_openapi.yaml?ref_type=heads",
        "File": "https://community.opengroup.org/osdu/platform/system/file/-/raw/master/docs/file-service_openapi.yaml?ref_type=heads",
        "Dataset": "https://community.opengroup.org/osdu/platform/system/dataset/-/raw/master/docs/dataset.swagger.yaml?ref_type=heads",
        "Legal": "https://community.opengroup.org/osdu/platform/security-and-compliance/legal/-/raw/master/docs/api/legal_openapi.yaml?ref_type=heads",
        "Policy": "https://community.opengroup.org/osdu/platform/security-and-compliance/policy/-/raw/master/docs/openapi.yaml?ref_type=heads",
        "Secret": "https://community.opengroup.org/osdu/platform/security-and-compliance/secret/-/raw/main/docs/api/secret_openapi.json?ref_type=heads",
        "Wellbore": "https://community.opengroup.org/osdu/platform/domain-data-mgmt-services/wellbore/wellbore-domain-services/-/raw/master/spec/generated/openapi.json?ref_type=heads",
        "WellDelivery": "https://community.opengroup.org/osdu/platform/domain-data-mgmt-services/well-delivery/well-delivery/-/raw/master/docs/api/swagger.yaml?ref_type=heads",
        "RAFS": "https://community.opengroup.org/osdu/platform/domain-data-mgmt-services/rock-and-fluid-sample/rafs-ddms-services/-/raw/main/docs/spec/openapi.json?ref_type=heads"
    }

    for service in SERVICES:
        test_module = os.path.join(tests_path, service.lower(), f"test_{service.lower()}.py")
        if not os.path.exists(test_module):
            generate_tests(
                service.lower(),
                tests_path,
                os.path.join("./osdu_client/services", service.lower())
            )
