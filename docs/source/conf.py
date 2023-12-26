# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'FRC 3603'
copyright = '3603'
author = 'Wile E. Coyote'

release = '0.2'
version = '0.2.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

html_theme_options = {
    'css_files': [
        'https://new-help-test.readthedocs.io/en/latest/_static/css/custom.css',
    ],
}

html_css_files = [
    'https://new-help-test.readthedocs.io/en/latest/_static/css/custom.css',
]

# -- Options for EPUB output
epub_show_urls = 'footnote'
