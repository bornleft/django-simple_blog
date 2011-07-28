from django.contrib.admin import site, ModelAdmin, TabularInline, StackedInline
from django import forms
#import widgets
from project.apps.blog import models

class BlogGroup(ModelAdmin):
		list_display = ('name', )

class BlogEntry(ModelAdmin):
		list_display = ('name', 'entry', 'author', 'date_pub', 'date_change')

class BlogTag(ModelAdmin):
		list_display = ('name', )

class BlogComment(ModelAdmin):
		list_display = ('comment', 'entry', 'author', 'date_pub', 'date_change')

site.register(models.Group, BlogGroup)
site.register(models.Entry, BlogEntry)
site.register(models.Tag, BlogTag)
site.register(models.Comment, BlogComment)