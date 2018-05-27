#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read()

requirements = [
    'Keras>=2.1.5',
    'numpy>=1.14.0',
    'opencv-python>=3.4.0.12',
    'scikit-image>=0.13.1',
    'scikit-learn>=0.19.1',
    'tensorflow>=1.7.0',
    'pandas>=0.22.0',
    'featuretools==0.1.17'
]

setup_requirements = ['pytest-runner', ]

test_requirements = ['pytest', ]

setup(
    author='MIT Data To AI Lab',
    author_email='dailabmit@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="Pipelines and primitives for machine learning and data science.",
    include_package_data=True,
    install_requires=requirements,
    keywords='machine learning classification',
    license="MIT license",
    long_description=readme + '\n\n' + history,
    long_description_content_type='text/markdown',
    name='mlblocks',
    packages=find_packages(include=['mlblocks']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/HDI-Project/MLBlocks',
    version='0.1.0',
    zip_safe=False,
)
