import json
import os
import re
import sys
from subprocess import PIPE, Popen
from typing import Any

import yaml

from .swagger import SwaggerDoc

NOT_SET = object()

UPPER_CASE_SNAKE_CASE_PATTERN = r"[a-zA-Z]+(_[a-zA-Z]+)*"

def ruff_format(path: str):
    popen = Popen(
        [
            sys.executable,
            "-m",
            "ruff",
            "format",
            path
        ],
        stdout=PIPE,
        stderr=PIPE
    )
    popen.wait()
    if popen.returncode != 0:
        msg = popen.stderr.read().decode()
        print(msg)


def generate_models(input: str, output: str, suppress_errors=True):
    cmd = [
        "datamodel-codegen",
        "--input",
        input,
        "--input-file-type",
        "openapi",
        "--output",
        output
    ]
    popen = Popen(
        cmd,
        stdout=PIPE,
        stderr=PIPE
    )
    popen.wait()
    if popen.returncode != 0:
        msg = popen.stderr.read().decode()
        if msg == "Models not found in the input data\n":
            return
        if msg == "Modular references require an output directory, not a file\n":
            cmd[-1] = cmd[-1].replace(".py", "")
            popen = Popen(
                cmd,
                stdout=PIPE,
                stderr=PIPE
            )
            popen.wait()
            if popen.returncode != 0:
                msg = popen.stderr.read().decode()
                print(msg)


def load_swagger(text: str) -> SwaggerDoc:
    try:
        return SwaggerDoc(**json.loads(text))
    except json.decoder.JSONDecodeError:
        return SwaggerDoc(**yaml.safe_load(text))


REPLACE_LIST = [
    "http://localhost:8080",
    "https://evq.csp.osdu.com"
]

def get_server_url(swagger: dict) -> str:
    
    if "basePath" in swagger:
        if re.fullmatch(UPPER_CASE_SNAKE_CASE_PATTERN, swagger["basePath"]):
            return ""
        return swagger["basePath"]

    if "servers" in swagger:
        if swagger["servers"][0]["url"] == '#{SDMS_PREFIX}#':
            return "api/seismic-store/v3"
        url = swagger["servers"][0]["url"]

        match = re.fullmatch(UPPER_CASE_SNAKE_CASE_PATTERN, url)
        if match:
            return ""

        for _str in REPLACE_LIST:
            url = url.replace(_str, "")
        

        return url
    else:
        return ""


def get_path(data: dict, path: str, default: Any = NOT_SET, separator: str = ".", ) -> Any:
    el: str
    result: Any = data
    for el in path.split(separator):
        try:
            if isinstance(result, dict):
                result = result[el]
            else:
                idx = int(el)
                result = result[idx]
        except KeyError as e:
            if default is NOT_SET:
                raise KeyError(f"Path {path} not found") from e
            return default
    return result


def put_inits(path: str):
    _path = path.lstrip("/").split("/")
    while len(_path) > 1:
        open(
            os.path.join(*_path, "__init__.py"), "w"
        ).close()
        _path.pop()
