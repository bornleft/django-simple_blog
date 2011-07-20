# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime
import os


class Group(models.Model):
    name = models.CharField(_(u"Название"), max_length=100, null=False, blank=False )

class Tag(models.Model):
	name = models.CharField(_(u"Название"), max_length = 100, null = False, blank = False)

class Comment(models.Model):
	entry = models.ForeignKey(Entry, verbose_name = u"", null = False, blank = False)
	comment = models.TextField(_(u"Название"), max_length = 100, null = False, blank = False)
	date_pub = models.DateTimeField(u"Дата опубликования", default=datetime.now())

class Entry(models.Model):
    group = models.ForeignKey(Group, verbose_name=u"", null=False, blank=False)
    name = models.CharField(_(u"Название"), max_length=100, null=False, blank=False )
	entry = models.TextField(_(u"Запись"), null = False, blank = False)
	date_pub = models.DateTimeField(u"Дата опубликования", default=datetime.now())
	date_change = models.DateTimeField(u"Дата изменения", default=datetime.now())