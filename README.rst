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

.. image:: https://img.shields.io/travis/SwissDataScienceCenter/renku-sphinx-theme.svg
        :target: https://travis-ci.org/SwissDataScienceCenter/renku-sphinx-theme

.. image:: https://img.shields.io/github/tag/SwissDataScienceCenter/renku-sphinx-theme.svg
        :target: https://github.com/SwissDataScienceCenter/renku-sphinx-theme/releases

.. image:: https://img.shields.io/pypi/dm/renku-sphinx-theme.svg
        :target: https://pypi.python.org/pypi/renku-sphinx-theme

.. image:: https://img.shields.io/github/license/SwissDataScienceCenter/renku-sphinx-theme.svg
        :target: https://github.com/SwissDataScienceCenter/renku-sphinx-theme/blob/master/LICENSE

A Sphinx theme for Renku documentation based on beatiful `Alabaster theme
<http://alabaster.readthedocs.io/en/latest/>`_.

Installation
------------

1. Add ``renku-sphinx-theme`` to ``setup.py`` or ``requirements.txt`` used
   for builing your documentation.
2. Set ``html_theme`` to ``'renku'`` in ``docs/conf.py``.
3. Configure at least ``description`` and ``github_repo`` in
   ``html_theme_options``.

Enjoy your beatiful Renku documentation style.
