#!/usr/bin/env python
# -*- coding: utf-8 -*-

AUTHOR = 'Edwin Khoo'
SITENAME = 'Edwin Khoo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Links
LINKS = (('Bazant Research Group', 'https://bazantgroup.mit.edu'),)

# Social widget
SOCIAL = (('Email', 'edwinksl@gmail.com'),
          ('Google Scholar', 'https://scholar.google.com/citations?user=y1-vy_0AAAAJ'),
          ('GitHub', 'https://github.com/edwinksl'),
          ('Bitbucket', 'https://bitbucket.org/edwinksl'),
          ('Stack Exchange', 'http://stackexchange.com/users/226073/edwinksl', 'stack-exchange'),
          ('Facebook', 'https://www.facebook.com/edwinksl'),
          ('Twitter', 'https://twitter.com/edwinksl'),
          ('LinkedIn', 'https://www.linkedin.com/in/edwinksl'),
          ('Quora', 'https://www.quora.com/profile/Edwin-Khoo'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme options
THEME = '../pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'

# Custom CSS
CUSTOM_CSS = 'static/custom.css'

# Markdown extensions
MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra']

# Plugins
PLUGIN_PATHS = ['..']
PLUGINS = ['pelican_plugin-render_math']

STATIC_PATHS = ['images', 'extras/CNAME', 'extras/custom.css']
EXTRA_PATH_METADATA = {'extras/CNAME': {'path': 'CNAME'},
                       'extras/custom.css': {'path': 'static/custom.css'}}

ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
INDEX_SAVE_AS = 'blog/index.html'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Blog', '/blog'),
             ('Research', '/pages/research.html'),
             ('Resources', '/pages/resources.html')]
