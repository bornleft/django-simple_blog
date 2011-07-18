# -*- coding: utf-8 -*-
from lib.decorators import *
from django.views.generic.simple import direct_to_template

@render_to('base.html')
def index(request):
    return {}

def extjs(request):
    return direct_to_template(request, 'extjs.html')
