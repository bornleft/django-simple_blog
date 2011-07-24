# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext
from django.utils import simplejson as json
from django.core.urlresolvers import reverse
from django.utils.http import urlquote
from project.apps.blog.models import Tag, Group, Comment, Entry

def first(request):
	entrys = Entry.objects.all().order_by('-date_pub')
	groups = Group.objects.all().order_by('name')
	return render_to_response('blog/main.html', locals(), context_instance=RequestContext(request))


