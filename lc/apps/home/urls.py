from django.conf.urls import *


urlpatterns = patterns('lc.apps.home.views',

 url(r'^$', 'index', name="index"),
 url(r'^calendar/$', 'calendar', name="calendar"),
url(r'^calendar/inner/(\d{4})/$', 'calendar_inner', name="calendar_inner"),
 url(r'^community/$', 'community', name="community"),

)

