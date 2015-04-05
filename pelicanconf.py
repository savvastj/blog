#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Savvas Tjortjoglou'
SITENAME = u'Savvas Tjortjoglou'
SITEURL = ''

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
# LINKS =  (('Pelican', 'http://getpelican.com/'),
#           ('Python.org', 'http://python.org/'),
#           ('DataTau', 'http://www.datatau.com/'),
#           ('Pythonic Perambulations', 'http://jakevdp.github.io/'),
#           ('Greg Rada', 'http://www.gregreda.com/'),
#           ('The Spread', 'http://thespread.us/'),)
          # ('538', 'http://fivethirtyeight.com/'),
          # ('Wonkblog', 'http://www.washingtonpost.com/blogs/wonkblog/'),
          # ('Vox', 'http://www.vox.com/'),
          # ('The Upshot', 'http://www.nytimes.com/upshot/'),
          # ('Grantland', 'http://grantland.com/'),)

# Social widget
SOCIAL = (('Twitter', 'http://twitter.com/savvas_91'),
          ('Github', 'http://github.com/savvastj'),)

DEFAULT_PAGINATION = 5

DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "/home/savvas-mint/pelican-themes/pelican-bootstrap3"

# Disqus and Google Analytics

# DISQUS_SITENAME = "savvasblog"
# DISQUS_NO_ID = True

GOOGLE_ANALYTICS = "UA-50819746-1"


#Plugins
PLUGIN_PATHS = ['/home/savvas-mint/pelican-plugins']
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook', 
           'summary']


# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'code', 'extra/CNAME']

# # Shift the installed location of a file
# Used for custom domain name
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }

# Pygments 
PYGMENTS_STYLE = 'monokai'

# Bootswatch THEME
BOOTSTRAP_THEME = 'creative'

# Recent Posts
# DISPLAY_RECENT_POSTS_ON_SIDEBAR = 'True'

# Set to blue version of creative which is based on yeti
BOOTSTRAP_NAVBAR_INVERSE = True

# Hide the side bare
# HIDE_SIDEBAR = True

DISPLAY_TAGS_ON_SIDEBAR = False


