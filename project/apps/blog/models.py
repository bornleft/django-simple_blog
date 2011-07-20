# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import ugettext as _
from datetime import datetime
import os


class Group(models.Model):
		name = models.CharField(_(u"Название"), max_length=100, null=False, blank=False )

		class Meta:
				verbose_name = 'группа'
				verbose_name_plural = 'группы'

class Tag(models.Model):
		name = models.CharField(_(u"Название"), max_length = 100, null = False, blank = False)
		entrys = models.ManyToManyField('Entry', verbose_name=_(u"Запись"), blank=True, null=True)

		class Meta:
				verbose_name = 'тэг'
				verbose_name_plural = 'тэги'

class Comment(models.Model):
		entry = models.ForeignKey('Entry', verbose_name = u"", null = False, blank = False)
		comment = models.TextField(_(u"Название"), max_length = 100, null = False, blank = False)
		date_pub = models.DateTimeField(u"Дата опубликования", default=datetime.now())

		class Meta:
				verbose_name = 'коммент'
				verbose_name_plural = 'комменты'

class Entry(models.Model):
		group = models.ForeignKey(Group, verbose_name=_(u""), null=False, blank=False)
		name = models.CharField(_(u"Название"), max_length=100, null=False, blank=False )
		entry = models.TextField(_(u"Текст"), null = False, blank = False)
		author = models.ForeignKey(User, verbose_name=_(u"Автор"), null=False, blank=False)
		date_pub = models.DateTimeField(_(u"Дата опубликования"), auto_now_add=True)
		date_change = models.DateTimeField(_(u"Дата изменения"), auto_now=True)

		class Meta:
				verbose_name = 'запись'
				verbose_name_plural = 'записи'