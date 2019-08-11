#! /usr/bin/env python
import os

from setuptools import setup

PROJECT_ROOT, _ = os.path.split(__file__)
with open("version.txt") as vf:
    REVISION = vf.read().strip()

print(f"**** BUILDING {REVISION} .")

PROJECT_NAME = "uk_improv_guide"
PROJECT_AUTHORS = "Salim Fadhley"
PROJECT_EMAILS = "salimfadhley@gmail.com"
PROJECT_URL = "https://github.com/salimfadhley/uk_improv_guide"
SHORT_DESCRIPTION = "Demonstration"

try:
    DESCRIPTION = open(os.path.join(PROJECT_ROOT, "readme.md")).read()
except IOError:
    DESCRIPTION = SHORT_DESCRIPTION

try:
    REQUIREMENTS = list(open("requirements.txt").read().splitlines())
except IOError:
    REQUIREMENTS = []

setup(
    name=PROJECT_NAME.lower(),
    version=REVISION,
    author=PROJECT_AUTHORS,
    author_email=PROJECT_EMAILS,
    package_dir={"": "uk_improv_guide"},
    packages=["uk_improv_guide"],
    zip_safe=True,
    include_package_data=False,
    install_requires=REQUIREMENTS,
    url=PROJECT_URL,
    description=SHORT_DESCRIPTION,
    long_description=DESCRIPTION,
    license="MIT",
    entry_points={"console_scripts": ["manage = uk_improv_guide.manage:main"]},
)
