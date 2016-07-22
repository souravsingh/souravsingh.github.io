#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sourav Singh'
SITENAME = u"Sourav's Blog"
SITEURL = ''
SITETITLE = AUTHOR
PATH = 'content'
THEME = "eevee"
TIMEZONE = 'Asia/Kolkata'

THEME_PRIMARY = 'deep_orange'
THEME_ACCENT = 'red'

DISPLAY_PAGES_ON_MENU = True
DEFAULT_LANG = u'en'

DEFAULT_DATE_FORMAT = '%d %b %Y'

DATE_FORMATS = {
    'en': DEFAULT_DATE_FORMAT
}

DISQUS_SITENAME = "systechlog"
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

COMMENTS_ON_PAGES = True

SUMMARY_MAX_LENGTH = 150
