# -*- coding: utf-8 -*-
import logging
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime
import os


class Group(models.Model):
		name = models.CharField(_(u"Название"), max_length=100, null=False, blank=False )

		def __unicode__(self):
			return u'%s' % (self.name)

		class Meta:
				verbose_name = _(u'группу')
				verbose_name_plural = _(u'группы')


class Tag(models.Model):
		name = models.CharField(_(u"Название"), max_length = 100, null = False, blank = False)
		entrys = models.ManyToManyField('Entry', verbose_name=_(u"Запись"), blank=True, null=True)

		def __unicode__(self):
			return u'%s' % (self.name)

		class Meta:
				verbose_name = _(u'тэг')
				verbose_name_plural = _(u'тэги')

class Entry(models.Model):
		group = models.ForeignKey(Group, verbose_name=_(u"группа"), null=False, blank=False)
		name = models.CharField(_(u"Название"), max_length=100, null=False, blank=False )
		entry = models.TextField(_(u"Текст"), null = False, blank = False)
		author = models.ForeignKey(User, verbose_name=_(u"Автор"), null=False, blank=False)
		date_pub = models.DateTimeField(_(u"Дата опубликования"), auto_now_add=True)
		date_change = models.DateTimeField(_(u"Дата изменения"), auto_now=True)

		def get_tags(self):
			tags = Tag.objects.filter(entrys__in = [self])
			return tags



		def __unicode__(self):
			return u'%s' % (self.name)

		class Meta:
				verbose_name = _(u'запись')
				verbose_name_plural = _(u'записи')