#!/usr/bin/env python3

"""
Setup BONSAI ML python package
"""

from setuptools import setup
from os import path

setup(
    name='loudml',

    version='0.1.0',

    description='BONSAI ML python package',

    py_modules=[
    ],

    packages=[
        'loudml',
        'loudml_new',
    ],

    setup_requires=[
        'jinja2',
    ],

    tests_require=['nose'],
    test_suite='nose.collector',

    install_requires=[
        'dateutils',
        'flask',
        'elasticsearch',
        'tensorflow',
        'h5py',
        'hyperopt',
        'influxdb',
        'Pillow',
        'PyYAML',
        'requests>=2.17.0',
    ],

    extras_require={
    },

    package_data={
    },

    data_files=[
    ],

    include_package_data=True,
    zip_safe=False,

    entry_points={
        'console_scripts': [
            'loudmld=loudml.server:main',
            'loudml_times=loudml.times:main',
            'loudml_ivoip=loudml.ivoip:main',
            'loudml-faker=loudml.faker:main',
            'loudml=loudml.cli:main',
        ],
        'loudml.commands': [
            'create-model=loudml.cli:CreateModelCommand',
            'delete-model=loudml.cli:DeleteModelCommand',
            'list-models=loudml.cli:ListModelsCommand',
            'train=loudml.cli:TrainCommand',
        ],
        'loudml.datasources': [
            'elasticsearch=loudml_new.elastic:ElasticsearchDataSource',
            'influxdb=loudml_new.influx:InfluxDataSource',
        ],
        'loudml.models': [
            'timeseries=loudml_new.times:TimesModel',
        ],
    },
)