# -*- coding: utf-8 -*-
# ===============LICENSE_START=======================================================
# Acumos Apache-2.0
# ===================================================================================
# Copyright (C) 2017-2018 AT&T Intellectual Property & Tech Mahindra. All rights reserved.
# ===================================================================================
# This Acumos software file is distributed by AT&T and Tech Mahindra
# under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# This file is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============LICENSE_END=========================================================
from setuptools import setup, find_packages


with open("README.md", "r", encoding='utf-8') as file:
    long_description = file.read()


setup(
    name='serviceboot',
    version='0.2.1',
    author='cubeai',
    author_email='cubeai@163.com',
    description='史上最牛的Python微服务框架 —— ServiceBoot',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='Apache License 2.0',
    packages=find_packages(),
    install_requires=[
        'cython==0.29.21',
        'requests==2.24.0',
        'tornado==6.0.4',
        'pyyaml==5.3.1',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: Apache Software License',
    ],
    entry_points="""
    [console_scripts]
    serviceboot=serviceboot.serviceboot:start
    build_docker=serviceboot.build_docker:build_docker
    """,
    keywords='web application micro-service framework 微服务 框架',
    python_requires='>=3.5',
    url='https://github.com/cube-ai/serviceboot.git',
)
