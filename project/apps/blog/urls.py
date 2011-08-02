# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *
#from project.apps.blog.views import RSS

# Global URLConf
from project.apps.blog.views import RssNewsFeed

urlpatterns = patterns('project.apps.blog.views',
    url(r'^entry/(\d+)/$', 'entry', name = "view_entry"),
    url(r'^entry/(\d+)?/edit/$', 'add_modify_entry', name = 'add_modify_entry'),
    url(r'^entry/(\d+)/delete/$', 'delete_entry', name = 'delete_entry'),
    url(r'^section/(\d+)$', 'section', name = "section"),
    url(r'^search/', 'search', name = "search"),
    url(r'^draft/$', 'draft', name = 'draft'),
    url(r'^post-comment/$', 'post_comment', name = "post_comment"),
    url(r'^$', 'first', name="first"),
)

urlpatterns += patterns('',
    url(r'^rss/$', RssNewsFeed(), name = "rss"),
)