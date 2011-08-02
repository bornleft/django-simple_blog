# -*- coding: utf-8 -*-
from django.db.models.query_utils import Q
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseServerError, HttpResponse, HttpResponseNotFound
from django.template import RequestContext
from django.utils import simplejson as json
from django.core.urlresolvers import reverse
from django.utils.http import urlquote
from project.apps.blog.models import Tag, Group, Entry, Comment
from project.apps.blog.forms import CommentForm, EntryForm, TagForm
from django.contrib.syndication.views import Feed

def first(request):
    entrys = Entry.objects.filter(draft = False).order_by('-date_pub')
    groups = Group.objects.all().order_by('name')
    return render_to_response('blog/entrys.html', locals(), context_instance=RequestContext(request))


def entry(request, pk):

    try:
        entry = Entry.objects.get(pk = pk)
    except:
        return HttpResponseNotFound


    form = CommentForm()

    return render_to_response('blog/entry.html', locals(), context_instance=RequestContext(request))

def add_modify_entry(request, pk = None):
    #TODO delete it after dev
    print request.user

    if request.method == "POST":
        if pk:
            #пк указан, в ссылке, это редактирование
            _entry = Entry.objects.get(pk = pk)


            form_entry = EntryForm(request.POST, instance = _entry, prefix = "entry")
            if _entry.get_tags() :
                form_tag = TagForm(request.POST, prefix = "tag", instance = _entry.get_tags()[0] )
            else:
                form_tag = TagForm(request.POST, prefix = "tag")
        else:
            form_entry = EntryForm(request.POST, prefix = "entry")
            form_tag = TagForm(request.POST, prefix = "tag")

        if form_entry.is_valid() and form_tag.is_valid():

            en = form_entry.save()
            tg = Tag.objects.filter(name = form_tag.cleaned_data['name'])
            if tg:
                #exist
                tg = tg[0]
                tg.entrys.add(en.pk)
                tg.save()
            else:
                #not exist
                tg = form_tag.save()
                tg.entrys.add(en)
                tg.save()
            return HttpResponseRedirect("/")
    else:
        if pk:
            #пк указан, в ссылке, это редактирование
            _entry = Entry.objects.get(pk = pk)


            form_entry = EntryForm(instance = _entry, prefix = "entry")
            if _entry.get_tags() :
                form_tag = TagForm(prefix = "tag", instance = _entry.get_tags()[0] )
            else:
                form_tag = TagForm(prefix = "tag")

        else:
            form_entry = EntryForm(initial = {'author': request.user.id}, prefix = "entry")
            form_tag = TagForm(prefix = "tag")
        
    return render_to_response('blog/add_entry.html', locals(), context_instance=RequestContext(request))


def delete_entry(request, pk):
    if request.GET:
        try:
            en = Entry.objects.get(pk = pk).delete()
        except:
            return HttpResponseNotFound
        return HttpResponseRedirect('/')
    else:
        entry = Entry.objects.get(pk = pk)
        return render_to_response('blog/delete_entry.html', locals(), context_instance=RequestContext(request))

def entry(request, pk):
    try:
        entry = Entry.objects.get(pk = pk)
    except:
        return HttpResponseNotFound
    form = CommentForm(initial = {"entry_pk": entry.pk})

    return render_to_response('blog/entry.html', locals(), context_instance=RequestContext(request))

def draft(request):
    entrys = Entry.objects.filter(draft = True).order_by('-date_pub')
    if not entrys:
        return HttpResponseRedirect('/')
    return render_to_response('blog/entrys.html', locals(), context_instance=RequestContext(request))

def section(request, section_pk):

    entrys = Entry.objects.filter( group__pk = section_pk, draft = False ).order_by('-date_pub')

    return render_to_response('blog/entrys.html', locals(), context_instance=RequestContext(request))


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

def search(request):
    if request.GET:
        q = request.GET["q"]
        entrys = Entry.objects.filter(
            Q(name__contains = q) | Q(group__name__contains = q)
            , Q(draft = False) ).order_by('-date_pub')
    else: #not POST
        return HttpResponseServerError

    return render_to_response('blog/entrys.html', locals(), context_instance=RequestContext(request))

class RssNewsFeed(Feed):
    title = "Django-simple_blog rss"
    description = "Updates on changes and additions to django-simple_blog."

    def get_object(self, request, group_id):
        return get_object_or_404(Entry, group__pk=group_id)

    def items(self, obj):
        return Entry.objects.filter(draft=False).order_by('-date_pub')
    def item_title(item, obj):
        return obj
    def item_description(item, obj):
        return obj
    def item_link(item, obj):
        return obj
    def link(self, obj):
        return obj
