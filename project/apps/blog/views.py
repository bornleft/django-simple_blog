# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404, HttpResponse, HttpResponseNotFound
from django.template import RequestContext
from django.utils import simplejson as json
from django.core.urlresolvers import reverse
from django.utils.http import urlquote
from project.apps.blog.models import Tag, Group, Entry

def first(request):
	entrys = Entry.objects.all().order_by('-date_pub')
	groups = Group.objects.all().order_by('name')

	return render_to_response('blog/main.html', locals(), context_instance=RequestContext(request))


def entry(request, pk):

	try:
		entry = Entry.objects.get(pk = pk)
	except:
		return HttpResponseNotFound


	return render_to_response('blog/entry.html', locals(), context_instance=RequestContext(request))


def search(request, s):
	try:
		entrys = Entry.objects.filter(group__name__icontains = s).order_by('-date_pub')
	except:
		return HttpResponseNotFound
	return render_to_response('blog/search.html', locals(), context_instance=RequestContext(request))