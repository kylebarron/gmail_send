#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'google-api-python-client >= 1.7.3',
    'httplib2 >= 0.11.3',
    'oauth2client >= 4.1.2',
]

setup_requirements = [
    'setuptools >= 38.6.0',
    'twine >= 1.11.0'
]

test_requirements = []

setup(
    author="Kyle Barron",
    author_email='barronk@mit.edu',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    description="Simple wrapper to send emails through Gmail",
    install_requires=requirements,
    entry_points={
        'console_scripts': ['gmail_send_auth=gmail_send.send:authenticate_cli']
    },
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='gmail_send',
    name='gmail_send',
    packages=find_packages(include=['gmail_send']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/kylebarron/gmail_send',
    version='0.1.0',
    zip_safe=False,
)
