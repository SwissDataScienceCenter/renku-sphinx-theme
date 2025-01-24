..
    Copyright 2017 Swiss Data Science Center (SDSC)
    A partnership between École Polytechnique Fédérale de Lausanne (EPFL) and
    Eidgenössische Technische Hochschule Zürich (ETHZ).

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

=================================
 Sphinx Theme for Renku Projects
=================================

.. image:: https://github.com/SwissDataScienceCenter/renku-sphinx-theme/actions/workflows/test.yml/badge.svg
        :target: https://github.com/SwissDataScienceCenter/renku-sphinx-theme/actions?query=branch%3Amaster

.. image:: https://img.shields.io/github/tag/SwissDataScienceCenter/renku-sphinx-theme.svg
        :target: https://github.com/SwissDataScienceCenter/renku-sphinx-theme/releases

.. image:: https://img.shields.io/pypi/dm/renku-sphinx-theme.svg
        :target: https://pypi.python.org/pypi/renku-sphinx-theme

.. image:: https://img.shields.io/github/license/SwissDataScienceCenter/renku-sphinx-theme.svg
        :target: https://github.com/SwissDataScienceCenter/renku-sphinx-theme/blob/master/LICENSE

A Sphinx theme for Renku documentation based on RTD theme.

https://renku-sphinx-theme.readthedocs.io/en/latest/

Installation
------------

1. Add ``renku-sphinx-theme`` to ``setup.py`` or ``requirements.txt`` used
   for building your documentation.
2. Set ``html_theme`` to ``'renku'`` in ``docs/conf.py``.
3. Configure at least ``description`` and ``github_repo`` in
   ``html_theme_options``.

Enjoy your beautiful Renku documentation style.


Style (css)
-----------

This repo contains a ``scss`` file that generates a ``css`` file.
The ``css`` file shouldn't be manually modified since it's generated with the ``scss``.
Instructions to change and run the ``scss`` file are inside it ``./renku_sphinx_theme/static/custom.scss``.

Renku repo is a better repository for testing style changes.

The easy way of doing this is to go to the renku repo, add a temporary css (custom.css)
in the ``docs/conf.py`` file and follow this steps:

https://renku.readthedocs.io/en/latest/how-to-guides/contributing/documentation.html

After doing the changes in the temporary css add this to custom.scss in this repository, build this into
a css file using the instructions and commit the css and scss files.


Building
--------

To build docs after doing changes, and test things inside this repository

1. From the base folder... ``pip install -r docs/requirements.txt``
2. This should be done in case there where changes in fonts or new css files added ``pip install --editable .``
3. There is no Makefile here but in order to do the "make html" action you should do

    ``cd docs``
    ``sphinx-build -b html -d _build/doctrees . _build/html``

Docs will be built into ``_build/html...`` open this files with chrome to see the changes.


Releasing
---------

1. Create a pull request updating ``renku_sphinx_theme/version.py`` to the new version number
   and ``CHANGES.rst`` to list the new changes.
2. Once the pull request is merged, `create a new release <https://github.com/SwissDataScienceCenter/renku-sphinx-theme/releases/new>`__.
3. The release will be automatically be pushed to `PyPI <https://pypi.org/project/renku-sphinx-theme/>`__.
