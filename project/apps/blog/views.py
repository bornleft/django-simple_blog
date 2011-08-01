# -*- coding: utf-8 -*-
from django.db.models.query_utils import Q
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponseServerError, HttpResponse, HttpResponseNotFound
from django.template import RequestContext
from django.utils import simplejson as json
from django.core.urlresolvers import reverse
from django.utils.http import urlquote
from project.apps.blog.models import Tag, Group, Entry, Comment
from project.apps.blog.forms import CommentForm, EntryForm, TagForm

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

def add_entry(request):
    #TODO delete it after dev
    print request.user

    if request.method == "POST":
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
        form_entry = EntryForm(initial = {'author': request.user.id}, prefix = "entry")
        form_tag = TagForm(prefix = "tag")
    return render_to_response('blog/add_entry.html', locals(), context_instance=RequestContext(request))

def update_entry(request):
    # not work
    form_entry = EntryForm(request.POST, prefix = "entry")
    if form_entry.is_valid():
        if form_entry.cleaned_data['draft']:
            _draft = True
        else:
            _draft = False

        Entry.objects.filter(pk = 7).update(
            group = form_entry.cleaned_data['group'],
            name = form_entry.cleaned_data['name'],
            entry = form_entry.cleaned_data['entry'],
            author = request.user.id,
            draft = _draft,
        )

    return HttpResponseRedirect("/")


def edit_entry(request, pk):
    try:
        en = Entry.objects.get(pk = pk)
        tg = Tag.objects.filter(entrys = Entry.objects.get(pk = pk))[0]

    except:
        return HttpResponseNotFound
    form_entry = EntryForm(instance = en, prefix = 'entry')
    form_tag = TagForm(instance = tg, prefix = 'tag')
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