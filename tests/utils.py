import re
from typing import Generator

import requests_mock

from gen.helpers import get_server_url, load_swagger
from gen.swagger import SwaggerDoc
from osdu_client.utils import urljoin


def define_endpoint(mocker: requests_mock.Mocker, path, method, swagger: dict):
    url = get_server_url(swagger)
    path_pattern = re.sub(r'\{[a-zA-Z0-9&_\.-]*\}', ".*", path, flags=re.DOTALL)
    url = urljoin("https://base.url", url, path_pattern)
    matcher = re.compile(url)
    getattr(
        mocker,
        method.lower(),
    )(
        url=matcher,
        json={}
    )


def create_swagger_server(mocker: requests_mock.Mocker, swagger_path: str) -> Generator[None, None, requests_mock.Mocker]:
    data = load_swagger(open(swagger_path).read())
    swagger = SwaggerDoc(data)

    for path in swagger["paths"]:
        for method in swagger["paths"][path]:
            define_endpoint(
                mocker,
                path,
                method,
                swagger
            )
