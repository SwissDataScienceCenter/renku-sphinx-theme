# -*- coding: utf-8 -*-
#
# Copyright 2017 Swiss Data Science Center (SDSC)
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

"""A Sphinx theme for Renga documentation."""

import os

from setuptools import setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'check-manifest>=0.25',
    'isort>=4.2.2',
    'pydocstyle>=1.0.0',
]

extras_require = {
    'docs': [
        'Sphinx>=1.6.3',
    ],
    'tests': tests_require,
}

extras_require['all'] = extras_require['docs'] + extras_require['tests']

# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('renga_sphinx_theme', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='renga-sphinx-theme',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='Renga Sphinx theme',
    license='Apache License 2.0',
    author='Swiss Data Science Center (SDSC)',
    author_email='contact@datascience.ch',
    url='https://github.com/SwissDataScienceCenter/renga-sphinx-theme',
    platforms='any',
    packages=['renga_sphinx_theme'],
    include_package_data=True,
    extras_require=extras_require,
    tests_require=tests_require,
    entry_points={
        'sphinx.html_themes': [
            'renga = renga_sphinx_theme',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
