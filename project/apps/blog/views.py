# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext
from django.utils import simplejson as json
from django.core.urlresolvers import reverse
from django.utils.http import urlquote


