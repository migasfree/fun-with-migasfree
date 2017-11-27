#!/usr/bin/env python
# -*- coding: UTF-8 -*-


# ===================================
# code-block font size = footnotesize
# ===================================

from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter

class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\footnotesize"

PygmentsBridge.latex_formatter = CustomLatexFormatter


language = "es"

# Basic project info
project = u'Fun with migasfree'
copyright = u'Alberto Gacías'
version = ''
release = ''
latex_elements = { 'releasename': '' ,  }



# Build options
templates_path = ['_templates']
exclude_patterns = ['_build', 'README.rst']
source_suffix = '.rst'
master_doc = 'index'


# HTML options
html_theme = 'default'
html_theme_path = ['themes']
html_static_path = ['_static']
pygments_style = 'sphinx'
html_use_index = False          # FIXME once proper index directives are added.
html_show_sourcelink = False
html_show_sphinx = False
html_title = "Fun with migasfree"
html_add_permalinks = ''     # FIXME once styles are fixed to get the hover back.
html_logo = 'graphics/portada/migasfree.png'

# LATEX builder
latex_documents = [
  ('index', 'fun-with-migasfree.tex', u'Fun with migasfree',
   u'Alberto Gacías', 'manual'),
]

"""
latex_elements = {
#     'papersize': '',
#     'fontpkg': '',
#     'fncychap': '',
      'maketitle': r'\@title',
#     'pointsize': '',
#     'preamble': '',
#     'releasename': "",
#     'babel': '',
#     'printindex': '',
#     'fontenc': '',
#     'inputenc': '',
#     'classoptions': '',
#     'utf8extra': '',
}
"""

latex_logo = 'graphics/portada/migasfree.png'
latex_use_parts = True

"""
latex_elements = {
                  'preamble': '\\usepackage{amstext}',
                  'releasename': "",
               }
"""

# texinfo builder
texinfo_documents = [
    ('index', 'fun-with-migasfree.tex', u'Fun with migasfree',
     u'Alberto Gacías', 'manual'),
    ]

# ePub builder
epub_title = u'Fun with migasfree'
epub_author = u'Alberto Gacías'
epub_publisher = u'Alberto Gacías'
epub_copyright = u'Alberto Gacías'

