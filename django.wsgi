import sys
import os
import os.path

sys.path.insert(0, os.path.dirname(__file__))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
