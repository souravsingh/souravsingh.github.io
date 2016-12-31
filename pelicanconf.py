#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sourav Singh'
SITENAME = u"Purkyně's Cell"
SITEURL = 'https://souravsingh.github.io/'
SITETITLE = AUTHOR
PATH = 'content'
STATIC_PATHS = ['Images']

THEME = "pelican-blue"
TIMEZONE = 'Asia/Kolkata'

TWITTER_USERNAME="MrSouravSingh"

SIDEBAR_DIGEST = 'Programmer and an aspiring Bioinformatician'


BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

#DISPLAY_PAGES_ON_MENU = True
DEFAULT_LANG = u'en'

DEFAULT_DATE_FORMAT = '%d %b %Y'

DATE_FORMATS = {
    'en': DEFAULT_DATE_FORMAT
}

DISQUS_SITENAME = "systechlog"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll

# Social widget
SOCIAL = (('github', 'https://github.com/souravsingh'),
          ('twitter', 'https://twitter.com/MrSouravSingh'),
          )

DEFAULT_PAGINATION = False

COMMENTS_ON_PAGES = True

SUMMARY_MAX_LENGTH = 150
