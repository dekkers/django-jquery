import os
from django.conf import settings
from django import template
from django.utils.html import format_html

register = template.Library()


@register.simple_tag
def include_jquery():
    return format_html("<script type='text/javascript' src='{}'></script>",
                       os.path.join(getattr(settings, 'STATIC_URL'), 'jquery', 'jquery-1.7.2.min.js'))
