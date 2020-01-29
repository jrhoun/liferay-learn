import os
from sphinx.builders.html import StandaloneHTMLBuilder

import recommonmark
from recommonmark.transform import AutoStructify

#
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#

author = "Liferay"
copyright = "2019, Liferay"
extensions = ["notfound.extension", "recommonmark", "sphinx_markdown_tables"]
html_css_files = ["main.css"]
html_favicon = "_static/img/favicon.ico"
#html_js_files = ["main.js"]
html_logo = "_static/img/liferay-waffle.svg"
html_short_title = "Documentation"
html_show_copyright = False
html_show_sphinx = False
html_static_path = ["_static"]
html_theme = "basic"
html_title = "Liferay Learn"
language = "en"
locale_dirs = ["_locale"]
master_doc = "contents"
notfound_template = "404.html"
project = "Liferay Learn"
release = "1.0"
source_suffix = [".md", ".rst"]
templates_path = ["_templates"]
version = "1.0"

class WithRootSiteHTMLBuilder(StandaloneHTMLBuilder):
	def get_doc_context(self, docname, body, metatags):
		doc_context = super().get_doc_context(docname, body, metatags)

		if docname != 'README':
			# Set the README.md on the root level as the "fake" parent
			# ie: docs/commerce/README.md
			site_parent = self.get_relative_uri(docname, 'README')

			# Set the document title as site title
			# ie: Commerce or DXP Cloud, etc
			site_title = self.render_partial(self.env.titles['README'])['title']

			# Add the "fake" parent to the parents object, so that "DXP", "Commerce", etc.
			# is visible in the breadcrumbs
			doc_context['parents'].insert(
				0,
				{
					'link': site_parent,
					'title': site_title
				}
			)

		return doc_context

# def setup(app):
# 	app.add_builder(WithRootSiteHTMLBuilder, True)

# 	app.add_config_value('recommonmark_config', {
# 		'enable_auto_toc_tree': False,
# 		'enable_math': False,
# 		'enable_inline_math': False
# 	}, True)

# 	app.add_transform(AutoStructify)

# for MarkdownParser
from sphinx_markdown_parser.parser import MarkdownParser
from sphinx_markdown_parser.transform import AutoStructify

def setup(app):
    app.add_source_suffix('.md', 'markdown')
    app.add_source_parser(MarkdownParser)
    app.add_config_value('markdown_parser_config', {
        'auto_toc_tree_section': 'Content',
        'enable_auto_doc_ref': False,
        'enable_auto_toc_tree': False,
        'enable_eval_rst': True,
        'extensions': [
            'extra',
            'nl2br',
            'sane_lists',
            'smarty',
            'toc',
            'wikilinks',
            'pymdownx.arithmatex',
        ],
    }, True)

# for CommonMarkParser
from recommonmark.parser import CommonMarkParser

def setup(app):
    app.add_source_suffix('.md', 'markdown')
    app.add_source_parser(CommonMarkParser)
    app.add_config_value('markdown_parser_config', {
        'auto_toc_tree_section': 'Content',
        'enable_auto_doc_ref': False,
        'enable_auto_toc_tree': False,
        'enable_eval_rst': True,
        'enable_inline_math': True,
        'enable_math': True,
    }, True)

def setup(app):
    app.add_config_value('markdown_parser_config', {
            'url_resolver': lambda url: github_doc_root + url,
            'auto_toc_tree_section': 'Contents',
            }, True)
    app.add_transform(AutoStructify)
