#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

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
SOCIAL = (('GitHub', 'https://github.com/edwinksl'),
          ('Bitbucket', 'https://bitbucket.org/edwinksl'),
          ('Facebook', 'https://www.facebook.com/edwinksl'),
          ('Twitter', 'https://twitter.com/edwinksl'),
          ('LinkedIn', 'https://www.linkedin.com/in/edwinksl'),
          ('Quora', 'https://www.quora.com/profile/Edwin-Khoo'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = '/home/edwinksl/Git/pelican-bootstrap3'
BOOTSTRAP_NAVBAR_INVERSE = True

CUSTOM_CSS = 'static/custom.css'

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
