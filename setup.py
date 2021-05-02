#!/usr/bin/env python

from setuptools import setup


setup(
    name='make-deb-py3',
    version='0.0.6',
    include_package_data=True,
    packages=['make_deb_py3'],
    author="Rob McQueen",
    author_email="rob@nylas.com",
    maintainer="delta",
    maintainer_email="danielcabrales523@gmail.com",
    description="Generates Debian configuration based on your setup.py",
    package_data={
        "make_deb_py3": [
            "resources/debian/control.j2",
            "resources/debian/rules.j2",
            "resources/debian/triggers.j2",
            "resources/debian/changelog.j2",
            "resources/debian/compat.j2"
            ]
        },
    scripts=['bin/make-deb-py3'],
    install_requires=['future', 'Jinja2'],
    zip_safe=False
)
