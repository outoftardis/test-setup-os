# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------

project = 'OS Test'
copyright = '2021, Katya'
author = 'Katya'

# The full version, including alpha/beta/rc tags
release = '2021'

# substitutions

rst_prolog = """
.. |short_name| replace:: Lib Name
.. |full_name| replace:: Open Source Library Name
"""

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

html_static_path = ['_static']

html_theme = 'sphinx_book_theme'
html_logo = '_static/main.png'
html_favicon = '_static/favicons.png'

# html theme options
html_theme_options = {
    'repository_url': 'https://github.com/outoftardis/test-setup-os',
    'path_to_docs': 'docs/source',
    'use_issues_button': True,
    'use_edit_page_button': True,
    'repository_branch': 'main'
}