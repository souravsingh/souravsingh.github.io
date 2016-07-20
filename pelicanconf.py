#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sourav Singh'
SITENAME = u"Sourav's Blog"
SITEURL = ''
SITETITLE = AUTHOR
PATH = 'content'
THEME = u"../pelican-themes/Flex"
TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

TWITTER_USERNAME = "MrSouravSingh"
GITHUB_URL = "https://github.com/souravsingh"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# Social widget
SOCIAL = (('Github', 'http://github.com/souravsingh'),
          ('Twitter', 'http://twitter.com/MrSouravSingh'),
	('Reddit','http://reddit.com/user/DanSylverstere'))

DEFAULT_PAGINATION = False

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
