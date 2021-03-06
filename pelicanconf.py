#!/usr/bin/env python

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
LINKS = [('Bazant Research Group', 'https://bazantgroup.mit.edu/')]

# Social widget
SOCIAL = [('Email', 'mailto:edwinksl@gmail.com', 'envelope'),
          ('Google Scholar', 'https://scholar.google.com/citations?user=y1-vy_0AAAAJ'),
          ('GitHub', 'https://github.com/edwinksl'),
          ('Bitbucket', 'https://bitbucket.org/edwinksl/'),
          ('Stack Exchange', 'https://stackexchange.com/users/226073/edwinksl'),
          ('Facebook', 'https://www.facebook.com/edwinksl'),
          ('Twitter', 'https://twitter.com/edwinksl'),
          ('LinkedIn', 'https://www.linkedin.com/in/edwinksl/'),
          ('Quora', 'https://www.quora.com/profile/Edwin-Khoo'),
          ('Reddit', 'https://www.reddit.com/user/edwinksl')]

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Theme options
THEME = 'pelican-themes/pelican-bootstrap3'
BOOTSTRAP_THEME = 'flatly'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Custom CSS
CUSTOM_CSS = 'static/custom.css'

# Plugins
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['render_math', 'i18n_subsites']

STATIC_PATHS = ['images', 'extras/custom.css', '../CNAME', '../README.md', '../LICENSE.md', '../_headers', '../keybase.txt']
EXTRA_PATH_METADATA = {'extras/custom.css': {'path': 'static/custom.css'},
                       '../CNAME': {'path': 'CNAME'},
                       '../README.md': {'path': 'README.md'},
                       '../LICENSE.md': {'path': 'LICENSE.md'},
                       '../_headers': {'path': '_headers'},
                       '../keybase.txt': {'path': 'keybase.txt'}}

ARTICLE_PATHS = ['blog']
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
INDEX_SAVE_AS = 'blog/index.html'
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = [('Blog', '/blog'),
             ('Research', '/pages/research.html'),
             ('Resources', '/pages/resources.html')]

DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
