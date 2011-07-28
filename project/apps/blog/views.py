# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponseServerError, HttpResponse, HttpResponseNotFound
from django.template import RequestContext
from django.utils import simplejson as json
from django.core.urlresolvers import reverse
from django.utils.http import urlquote
from project.apps.blog.models import Tag, Group, Entry, Comment
from project.apps.blog.forms import CommentForm, EntryForm, TagForm

def first(request):
	entrys = Entry.objects.all().order_by('-date_pub')
	groups = Group.objects.all().order_by('name')

	return render_to_response('blog/main.html', locals(), context_instance=RequestContext(request))


def entry(request, pk):

	try:
		entry = Entry.objects.get(pk = pk)
	except:
		return HttpResponseNotFound


	form = CommentForm()

	return render_to_response('blog/entry.html', locals(), context_instance=RequestContext(request))

def add_entry(request):
	print request.POST
	if request.method == "POST":
		form_entry = EntryForm(request.POST, prefix = "entry")
		form_tag = TagForm(request.POST, prefix = "tag")
		if form_entry.is_valid() and form_tag.is_valid():
			en = Entry(
				group = form_entry.cleaned_data['group'],
				name = form_entry.cleaned_data['name'],
				entry = form_entry.cleaned_data['entry'],
				author = form_entry.cleaned_data['author']
			).save()
			tg = Tag(
				name = form_tag.cleaned_data['name'],
			)
			tg.entrys.add(en.pk).save()
			return HttpResponseRedirect("/")
	form_entry = EntryForm(prefix = "entry")
	form_tag = TagForm( prefix = "tag")
	return render_to_response('blog/add_entry.html', locals(), context_instance=RequestContext(request))

def entry(request, pk):
	try:
		e = Entry.objects.get(pk = pk)
	except:
		return HttpResponseNotFound


	form = CommentForm(initial = {"entry_pk": e.pk})

	return render_to_response('blog/entry.html', locals(), context_instance=RequestContext(request))

def post_comment(request):

	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			if request.user.is_anonymous():
				user = None
			else:
				user = request.user

			cmnt = Comment(
				comment = form.cleaned_data["comment"],
				author = user,
			    entry = Entry.objects.get(pk = form.cleaned_data["entry_pk"])
			)

			cmnt.save()
			return HttpResponseRedirect( request.META["HTTP_REFERER"] + "#cmnt%s" % cmnt.pk)
		else: #is not valid
			return HttpResponseRedirect( request.META["HTTP_REFERER"])

	else: #not POST
		return HttpResponseServerError

def search(request, s):

	entrys = Entry.objects.filter(group__name__icontains = s).order_by('-date_pub')

	return render_to_response('blog/search.html', locals(), context_instance=RequestContext(request))