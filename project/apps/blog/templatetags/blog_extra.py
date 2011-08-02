from django import template
from re import compile
register = template.Library()

@register.filter
@stringfilter
def cut_entry(value):
    p = compile('(\[cut\].*?)$', re.DOTALL)
    return sub(p, '', value)