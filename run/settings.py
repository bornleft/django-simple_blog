# -*- coding: utf-8 -*-
"""
DEBUG=True to run project in development mode.
DEBUG=False to run project in production mode,
"""

DEBUG = True
TEMPLATE_DEBUG = DEBUG
MEDIA_LOCAL_SERVER = DEBUG

if DEBUG:
    from run.development import *
else:
    from run.production import *
