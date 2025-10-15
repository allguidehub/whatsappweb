# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path if your modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'WhatsApp Web Usage Guide'
author = 'WhatsApp Web Support Team'
copyright = '2025'
# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Sphinx extensions (add if needed, e.g., 'sphinx_rtd_theme')
extensions = []

# Allow reStructuredText raw HTML content
raw_enabled = True

# Template paths
templates_path = ['_templates']

# Exclude build directories and system files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# (Optional) Enable a theme such as sphinx_rtd_theme
# html_theme = 'sphinx_rtd_theme'

# Page title that appears in the browser tab
html_title = "How to Use WhatsApp Web – Complete Desktop Guide"
html_short_title = "WhatsApp Web Guide"

# Favicon (optional – place favicon.ico in root or _static folder)
html_favicon = 'favicon.ico'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Static files such as custom CSS or images (uncomment if used)
# html_static_path = ['_static']
