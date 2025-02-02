# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from datetime import datetime

sys.path.insert(1, os.path.abspath("../src"))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "PSNAWP"
copyright = datetime.today().strftime("%Y, Yoshikage Kira")
author = "Yoshikage Kira (@isFakeAccount)"
release = "1.0.0"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = ["sphinx.ext.todo", "sphinx.ext.viewcode", "sphinx.ext.autodoc", 'sphinx.ext.intersphinx']
autodoc_default_options = {
    "members": True,
    "member-order": "bysource",
    "special-members": "__init__",
    "undoc-members": True,
    "exclude-members": "__weakref__",
}
# html_static_path = ["_static"]
# templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]
nitpick_ignore = [
    ("py:class", "Logging"),
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
pygments_style = "perldoc"
html_theme_options = {'collapse_navigation': True, 'analytics_id': 'G-DDW8HTV1D1'}
intersphinx_mapping = {"python": ("https://docs.python.org", None),
                       "requests": ("https://requests.readthedocs.io/en/latest/", None)}
htmlhelp_basename = "PRAW"

source_suffix = ".rst"
