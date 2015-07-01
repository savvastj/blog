#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

LOAD_CONTENT_CACHE = False

AUTHOR = u'Savvas Tjortjoglou'
SITENAME = u'Savvas Tjortjoglou'
SITEURL = 'http://savvastjortjoglou.com'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# used for ipynb plugin
MARKUP = ('md', 'ipynb')

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
# SOCIAL = (('Twitter', 'http://twitter.com/savvas_91'),
#           ('Github', 'http://github.com/savvastj'),)

DEFAULT_PAGINATION = 5

GOOGLE_ANALYTICS = "UA-50819746-1"

DISPLAY_CATEGORIES_ON_MENU = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = "/home/savvas/PyStuff/blog_env/pelican-themes/pelican-bootstrap3"

# Bootswatch THEME
BOOTSTRAP_THEME = 'yeti'

# Set to blue version of creative which is based on yeti
BOOTSTRAP_NAVBAR_INVERSE = False

# Hide the side bar
HIDE_SIDEBAR = True

#Plugins
PLUGIN_PATHS = ['/home/savvas/PyStuff/blog_env/pelican-plugins']
PLUGINS = ['ipynb', 
            'liquid_tags.img', 
            'liquid_tags.video',
           'liquid_tags.youtube', 
           'liquid_tags.vimeo',
           'liquid_tags.include_code', 
           'summary']

# Pygments 
PYGMENTS_STYLE = 'bw'

# Static paths will be copied without parsing their contents
STATIC_PATHS = ['images', 'code', 'extra/CNAME']

# # Shift the installed location of a file
# Used for custom domain name
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}, }



# DISQUS_SITENAME = "savvasblog"

SHARIFF = True
SHARIFF_LANG = True
