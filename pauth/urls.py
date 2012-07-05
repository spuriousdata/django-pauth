from django.conf.urls import patterns, url, include
from pauth.views import *

urlpatterns = patterns('',
    (r'^login/(?P<provider>\w/$', Login.as_view()),
    (r'^loggout/$', Logout.as_view()),
)
