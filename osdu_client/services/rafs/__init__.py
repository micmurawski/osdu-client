from .v1 import RAFSClient as RAFSClientV1  # NOQA
from .v2 import RAFSClient as RAFSClientV2  # NOQA

DEFAULT_VERSION = "v2"
VERSIONS = {
    "v1": RAFSClientV1,
    "v2": RAFSClientV2,
}
