# -*- coding: utf-8 -*-
#
# Copyright 2017-2018 Swiss Data Science Center (SDSC)
# A partnership between École Polytechnique Fédérale de Lausanne (EPFL) and
# Eidgenössische Technische Hochschule Zürich (ETHZ).
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A Sphinx theme for Renku documentation."""

import os

from setuptools import setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'check-manifest>=0.25',
    'isort>=4.2.2',
    'pydocstyle>=1.0.0',
    'twine>=4.0,<7.0',
    'pkginfo<1.13',
    'setuptools',
    'wheel',
]

extras_require = {
    'docs': [
        'Sphinx>=1.6.3,<10.0.0',
        'sphinx-rtd-theme>=0.5.0,<3.2',
    ],
    'dev': [ 
        'libsass~=0.23.0'
    ],
    'tests': tests_require,
}

extras_require['all'] = extras_require['docs'] + extras_require['dev'] + extras_require['tests']

install_requires = [
    'Sphinx>=1.6.3,<10.0.0',
    'sphinx-rtd-theme>=0.5.0,<3.2',
]

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('renku_sphinx_theme', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='renku-sphinx-theme',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    keywords='Renku Sphinx theme',
    license='Apache License 2.0',
    author='Swiss Data Science Center (SDSC)',
    author_email='contact@datascience.ch',
    url='https://github.com/SwissDataScienceCenter/renku-sphinx-theme',
    platforms='any',
    packages=['renku_sphinx_theme'],
    include_package_data=True,
    extras_require=extras_require,
    install_requires=install_requires,
    tests_require=tests_require,
    entry_points={
        'sphinx.html_themes': [
            'renku = renku_sphinx_theme',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
)
