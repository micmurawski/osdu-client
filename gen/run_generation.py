import os
import shutil

import requests

from gen.client_generator import generate_clients
from gen.helpers import generate_models, ruff_format

WORKDIR = os.getcwd()

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


def remove_path_if_empty(path: str):
    _path = os.path.join(path, "__init__.py")
    if os.path.exists(_path):
        with open(_path, 'r') as fp:
            lines = len(fp.readlines())

        if lines == 0:
            shutil.rmtree(path)


if __name__ == "__main__":

    for name in SERVICES:
        url = SERVICES[name]
        module_path = os.path.join(WORKDIR, "osdu_client", "services", name.lower())
        models_path = os.path.join(module_path, "models")
        rel_module_path = module_path.replace(WORKDIR, ".")
        os.makedirs(rel_module_path, exist_ok=True)

        swagger_path = os.path.join(module_path, "swagger.yaml")

        if not os.path.exists(swagger_path):
            with open(swagger_path, "w") as f:
                response = requests.get(url)

                if not response.ok:
                    raise Exception(f"Could not download {name}")

                f.write(response.text)

        if not (os.path.exists(models_path) or os.path.exists(models_path+".py")):
            generate_models(
                swagger_path,
                models_path+".py",
            )
        if not os.path.exists(os.path.join(module_path, "client.py")):
            generate_clients(
                swagger_path,
                name,
                dump_file_path=os.path.join(module_path, "client.py")
            )

        ruff_format(module_path)
        # os.remove(swagger_path)
        remove_path_if_empty(models_path)
