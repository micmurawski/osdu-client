from .v2 import WellboreClient as WellboreClientV2  # NOQA
from .v3 import WellboreClient as WellboreClientV3  # NOQA

DEFAULT_VERSION = "v3"
VERSIONS = {
    "v2": WellboreClientV2,
    "v3": WellboreClientV3,
}
