import os
from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def include_jquery():
    url = getattr(settings, 'MEDIA_URL')
    if hasattr(settings, 'STATIC_URL'):
        url = getattr(settings, 'STATIC_URL')
    return "<script type='text/javascript' src='%s'></script>" % os.path.join(url, 'jquery', 'jquery-1.4.2.min.js')
