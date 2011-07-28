# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.utils.translation import ugettext as _
from project.apps.blog.models import Entry

class CommentForm(forms.Form):
	entry_pk = forms.CharField( widget= forms.HiddenInput)
	fname = forms.CharField(label = _(u'Имя'))
	lname = forms.CharField(label = _(u'Фамилия'))
	comment = forms.CharField(label = _(u'Комментарий'), widget = forms.Textarea(attrs={'cols': 60, 'rows': 18}))

class EntryForm(ModelForm):
    class Meta:
		model = Entry