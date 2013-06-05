from django.conf.urls import *


urlpatterns = patterns('lc.apps.home.views',

 url(r'^$', 'index', name="index"),
 url(r'^calendar/$', 'calendar', name="calendar"),
 url(r'^community/$', 'community', name="community"),

)

