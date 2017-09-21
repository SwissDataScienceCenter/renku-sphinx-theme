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

from __future__ import absolute_import, print_function

import os

from .version import __version__

__all__ = ('__version__', 'get_path', 'setup', 'update_context')


def get_path():
    """Shortcut for users whose theme is next to their conf.py."""
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    """Update template context."""
    context['renga_theme_version'] = __version__

def setup(app):
    """Setup the Sphinx app."""
    theme_path = os.path.abspath(os.path.dirname(__file__))
    app.add_html_theme('renga', theme_path)
    app.connect('html-page-context', update_context)
    return {'version': __version__,
            'parallel_read_safe': True}
