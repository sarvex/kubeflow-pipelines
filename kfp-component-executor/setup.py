# Copyright 2022 The Kubeflow Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import setuptools

NAME = 'kfp-component-executor'
VERSION = '0.0.1'

setuptools.setup(
    name=NAME,
    version=VERSION,
    description='Kubeflow Pipelines component executor package.',
    author='google',
    author_email='kubeflow-pipelines@google.com',
    url='https://github.com/kubeflow/pipelines',
    packages=['kfp_component_executor'],
    python_requires='>=3.7.0',
    install_requires=['kfp>=2.0.0-a3'],
    license='Apache 2.0',
)
