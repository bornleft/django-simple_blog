# -*- coding: utf-8 -*-

from django.conf.urls.defaults import *



# Global URLConf
urlpatterns = patterns('project.apps.blog.views',
	url(r'^entry/(\d+)/$', 'entry', name = "view_entry"),
	url(r'^entry/(\d+)/edit/$', 'edit_entry', name = 'edit_entry'),
	url(r'^entry/(\d+)/delete/$', 'delete_entry', name = 'delete_entry'),
	url(r'^$', 'first', name=u"first"),
	url(r'^search/(.+?)/$', 'search', name = "search"),
	url(r'^add_entry/$', 'add_entry', name = "add_entry"),
	url(r'^draft/$', 'draft', name = 'draft'),
    url(r'^post-comment/$', 'post_comment', name = "post_comment"),
)




