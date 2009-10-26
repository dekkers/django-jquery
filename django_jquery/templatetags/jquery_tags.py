import os
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_noop, ugettext
from django.conf import settings
from django import template

register = template.Library()

APP_NAME = "jquery"
THEME_NAME = "flick"
FILES = {
    'js':('jquery-1.3.2.min.js', 'jquery-ui-1.7.2.custom.min.js'),
    'css':('%s/jquery-ui-1.7.2.custom.css' % THEME_NAME,),
}

@register.simple_tag
def jquery_requirements():
    print "jquery_requirements"
    url = "%s/%s" % (getattr(settings, "APPS_MEDIA_URL", {}), APP_NAME)
    print "url: ", url
    L = []
    for css in FILES['css']:
        path = os.path.normpath("%s/css/%s" % (url, css))
        L.append('<link type="text/css" href="%s" rel="Stylesheet" />' % path)
    for js in FILES['js']:
        path = os.path.normpath("%s/%s" % (url, js))
        L.append('<script type="text/javascript" src="%s"></script>' % path)
 
    print L


    return "\n".join(L)
