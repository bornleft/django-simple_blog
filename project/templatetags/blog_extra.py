from django import template
from re import compile, sub, DOTALL
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def cut_entry(value):
    p = compile('(\[cut\].*?)$', DOTALL)
    return sub(p, '', value)

@register.filter
@stringfilter
def all_entry(value):
    #p = compile('(\[cut\])', DOTALL)
    #return sub(p, '', value)
    return value.replace('[cut]', '')