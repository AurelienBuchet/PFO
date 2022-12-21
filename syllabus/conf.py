# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Principes de Fonctionnement des Ordinateurs'
copyright = '2020-2022, Olivier Bonaventure'
author = 'Olivier Bonaventure'

# The full version, including alpha/beta/rc tags
release = '2022'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinxcontrib.spelling', 
               'sphinxcontrib.tikz',
               'sphinx.ext.githubpages',
               'sphinx.ext.mathjax',
               #'interactive_syllabus_directives'
]

#               'matplotlib.sphinxext.only_directives',
#               'matplotlib.sphinxext.plot_directive',


# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'fr'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '._*.rst', 'old/*']

master_doc = 'index'

# sphinx

numfig=True  # numérotation des figures

# Spelling checker


#spelling
spelling_lang='fr'
spelling_word_list_filename='dict.txt'
tokenize_lang='fr'
spelling_ignore_acronyms=True
spelling_show_suggestions=True

# latex

latex_elements = {
    'preamble': r'''
\usepackage{bytefield}
\usepackage{circuitikz}
\usepackage{fontawesome}
'''
}
# tikz

tikz_tikzlibraries = "circuits.logic.US,arrows,positioning,calc,quotes,backgrounds,matrix"
tikz_proc_suite = 'ImageMagick'

tikz_latex_preamble='''
%preamble
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{pgfkeys}
\usepackage{bytefield}
\usepackage{circuitikz}
\usepackage{fontawesome}
\\usepackage[normalem]{ulem}
%\pgfplotsset{compat=1.16}
'''

# math


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']


html_theme_options = {
    #'analytics_id': 'G-XXXXXXXXXX',  #  Provided by Google in your dashboard
    #'analytics_anonymize_ip': False,
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': True,
    'sticky_navigation': True,
    'navigation_depth': 4,
    'includehidden': True,
    'titles_only': False
}

html_context = {
  'display_github': True,
  'github_user': 'obonaventure',
  'github_repo': 'PFO',
  'github_version': 'master',
  'conf_py_path': '/'
}
