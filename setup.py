import codecs
import os.path
from signal import raise_signal

from setuptools import find_packages, setup

HERE = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    return codecs.open(os.path.join(HERE, *parts), 'r').read()


def get_dependencies():
    with open("requirements.txt", encoding="utf-8") as fh:
        return fh.read().splitlines()


setup(
    name='osdu_client',
    version='0.3.2',
    author="Michal Murawski",
    author_email="mmurawski777@gmail.com",
    description="OSDU API Client",
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    url="https://github.com/micmurawski/osdu-client/",
    package_dir={"": "src"},
    packages=find_packages(
        where="./src",
        exclude=(
            'build',
            'tests',
        )),
    install_requires=get_dependencies(),
    include_package_data=True,
    python_requires=">=3.7,<4.0",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8"
    ],
)
