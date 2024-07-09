import os
import requests
from gen.generator import generate_clients
from gen.helpers import generate_models, ruff_format
import shutil


WORKDIR = os.getcwd()

SERVICES = {
    "Entitlements": "https://community.opengroup.org/osdu/platform/security-and-compliance/entitlements/-/raw/master/docs/api/entitlements_openapi.yaml?ref_type=heads",
    "SMDS": "https://community.opengroup.org/osdu/platform/domain-data-mgmt-services/seismic/seismic-dms-suite/seismic-store-service/-/raw/master/app/sdms/docs/api/openapi.osdu.yaml?ref_type=heads",
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
    "Secret": "https://community.opengroup.org/osdu/platform/security-and-compliance/secret/-/raw/main/docs/api/secret_openapi.json?ref_type=heads"
}


def put_inits(path: str):
    _path = path.replace(WORKDIR, "")[1:].split("/")
    while len(_path) > 1:
        open(
            os.path.join(*_path, "__init__.py"), "w"
        ).close()
        _path.pop()


def remove_path_if_empty(path: str):
    _path = os.path.join(path, "__init__.py")
    with open(_path, 'r') as fp:
        lines = len(fp.readlines())

    if lines == 0:
        shutil.rmtree(path)


if __name__ == "__main__":

    for name in SERVICES:
        url = SERVICES[name]
        module_path = os.path.join(WORKDIR, "osdu_client", "services", name.lower())
        models_path = os.path.join(module_path, "models")

        os.makedirs(module_path, exist_ok=True)
        put_inits(module_path)

        swagger_path = os.path.join(module_path, "swagger.yaml")

        if not os.path.exists(swagger_path):
            with open(swagger_path, "w") as f:
                response = requests.get(url)

                if not response.ok:
                    raise Exception(f"Could not download {name}")

                f.write(response.text)

        generate_models(
            swagger_path,
            models_path+".py",
        )
        generate_clients(
            swagger_path,
            name,
            dump_file=os.path.join(WORKDIR, "osdu_client", "services", name.lower(), "client.py")
        )
        ruff_format(
            os.path.join(WORKDIR, "osdu_client", "services", name.lower(), "client.py")
        )
        # os.remove(swagger_path)
        # remove_path_if_empty(models_path)
