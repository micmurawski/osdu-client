from subprocess import Popen, PIPE
import sys


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
    cmd = " ".join(
        [
            "datamodel-codegen",
            "--input",
            input,
            "--input-file-type",
            "openapi",
            "--output",
            output
        ]
    )
    # print(cmd)
    popen = Popen(
        [
            "datamodel-codegen",
            "--input",
            input,
            "--input-file-type",
            "openapi",
            "--output",
            output
        ],
        stdout=PIPE,
        stderr=PIPE
    )
    popen.wait()
    if popen.returncode != 0:
        msg = popen.stderr.read().decode()
        print(msg)
