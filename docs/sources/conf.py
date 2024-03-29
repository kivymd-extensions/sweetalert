# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# Path setup
import os
import sys
from os.path import realpath

sys.path.insert(0, os.path.abspath("_extensions"))
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath("."))))

import autoapi_sweetalert  # NOQA. from _extensions
from sweetalert import __version__  # NOQA

# Project information
project = "Sweet Alert"
copyright = "Copyright (c) 2020 KivyMD Team"
author = "KivyMD Team"
version = __version__
release = __version__

# General configuration
master_doc = "index"
exclude_patterns = []
templates_path = ["_templates"]
locale_dirs = ["_locales"]
language = "Python"

# HTML Theme
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_favicon = "_static/logo-kivymd.png"
html_logo = "_static/logo-kivymd.png"
html_theme_options = {
    "canonical_url": "https://sweetalert.readthedocs.io/en/latest/",
    "navigation_depth": 2,
    "collapse_navigation": False,
}

# Extensions
extensions = [
    "sphinx.ext.autodoc",
    "autoapi_sweetalert",
    "sphinx.ext.intersphinx",
    "kivy_lexer",
    "toctree_with_sort",
]

# AutoAPI configuration
autoapi_dirs = (
    ["../../../sweetalert"]
    if os.path.exists(realpath("../../../sweetalert"))
    else ["../../../../../sweetalert"]
)
autoapi_template_dir = os.path.abspath("_templates")
autoapi_ignore = []
autoapi_type = "python"
autoapi_file_patterns = ["*.py"]
autoapi_generate_api_docs = True
autoapi_options = ["members", "undoc-members"]
autoapi_root = "api"
autoapi_add_toctree_entry = False
autoapi_include_inheritance_graphs = False
show_module_summary = True
autoapi_python_class_content = "class"
autoapi_python_use_implicit_namespaces = False
autoapi_keep_files = False  # True for debugging

# InterSphinx configuration
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "kivy": ("https://kivy.org/doc/stable/", None),
}
