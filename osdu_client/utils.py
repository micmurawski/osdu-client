from __future__ import annotations

import re

FORBIDDEN_NAMES = {
    "from": "_form"
}


def urljoin(*args) -> str:
    return "/".join(map(lambda x: str(x).rstrip('/').lstrip('/'), [arg for arg in args if arg]))


def convert_to_snake_case(name: str) -> str:
    result = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower().replace("-", "_")
    if result in FORBIDDEN_NAMES:
        return FORBIDDEN_NAMES[result]
    return result
