import os
from django.conf import settings
from django import template

register = template.Library()

@register.simple_tag
def include_jquery():
    return "<script type='text/javascript' src='%s'></script>" % os.path.join(getattr(settings, 'STATIC_URL'), 'jquery', 'jquery-1.6.4.min.js')
