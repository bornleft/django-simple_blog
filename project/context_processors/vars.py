# -*- coding: utf-8 -*-
import project.settings
from project.apps.blog.models import Group, Entry

def setting_vars(request):


    return {
            'PROJECT_NAME' : project.settings.PROJECT_NAME,

    }

def menu_vars(request):
    groups = Group.objects.all().order_by('name')

    return {
        'menu': groups,
    }

def draft_count_vars(request):

    return {
        'draft_count': Entry.objects.filter(draft = True).order_by('-date_pub').count(),
    }