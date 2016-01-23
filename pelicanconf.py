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

# Blogroll
LINKS = (('Bazant Research Group', 'https://bazantgroup.mit.edu'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/edwinksl'),
          ('Bitbucket', 'https://bitbucket.org/edwinksl'),
          ('Facebook', 'https://www.facebook.com/edwinksl'),
          ('Twitter', 'https://twitter.com/edwinksl'),
          ('LinkedIn', 'https://www.linkedin.com/in/edwinksl'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = '/home/edwinksl/Git/pelican-bootstrap3'
BOOTSTRAP_NAVBAR_INVERSE = True

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
