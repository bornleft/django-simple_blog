# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

# Global URLConf
urlpatterns = patterns('project.views',
	url(r'^index$', 'index', name = "index"),
)

# Include applications URLConf
urlpatterns += patterns('',

    (r'^', include('project.apps.blog.urls')),
                        
    ######----------------------------------
    ######     for admin
    ######----------------------------------
    (r'^admin/', include(admin.site.urls)),
)

if settings.MEDIA_LOCAL_SERVER:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': 'project/static/' }),
    )
