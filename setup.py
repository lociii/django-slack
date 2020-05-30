#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='django-slack',
    url="https://chris-lamb.co.uk/projects/django-slack",
    version='5.14.4',
    description="Provides easy-to-use integration between Django projects and "
    "the Slack group chat and IM tool.",
    author="Chris Lamb",
    author_email="chris@chris-lamb.co.uk",
    license="BSD-3-Clause",
    packages=find_packages(),
    include_package_data=True,
    install_requires=('Django>=2', 'requests', 'six',),
)
