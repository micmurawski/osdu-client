from osdu_client.services import (rafs, wellbore)

SERVICES = {
    "dataset": [],
    "entitlements": [],
    "file": [],
    "indexer": [],
    "legal": [],
    "notification": [],
    "partition": [],
    "policy": [],
    "pws": [],
    "rafs": list(rafs.VERSIONS.keys()),
    "register": [],
    "schema": [],
    "sdms": [],
    "search": [],
    "secret": [],
    "storage": [],
    "wellbore": list(wellbore.VERSIONS.keys()),
    "welldelivery": [],
}
