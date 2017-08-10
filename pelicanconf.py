#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sergey Chizhik'
SITENAME = 's.chizhik #site'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Zaporozhye'

DEFAULT_LANG = 'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
    ('You can modify those links in your config file', '#'),
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/s-chizhik'),
    ('stack-overflow', 'https://stackoverflow.com/users/4469537/sergey-chizhik'),
    ('linkedin', 'https://www.linkedin.com/in/sergey-chizhik-848b02141'),
    ('telegram', 'https://t.me/s_chizhik'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
THEME = 'themes/clean-blog'

STATIC_PATHS = ['gpx_tracks', 'img', ]

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = True
HEADER_COLOR = '#008651'
