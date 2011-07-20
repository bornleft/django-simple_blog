# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
import os


class Group(models.Model):
    name = models.CharField(_(u"Название"), max_length=100, null=False, blank=False )


class Entry(models.Model):

    group = models.ForeignKey(Group, verbose_name=u"", null=False, blank=False)
    name = models.CharField(_(u"Название"), max_length=100, null=False, blank=False )
