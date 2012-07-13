from django.conf.urls import patterns, url, include
from pauth import loaded_providers
from pauth.views import *

urlpatterns = patterns('',
    (r'^login/(?P<provider>\w/$', Login.as_view()),
    (r'^loggout/$', Logout.as_view()),
)

for lp in loaded_providers.values():
    urlpatterns += lp.url()
