from django.conf.urls import patterns
from django.core.exceptions import ImproperlyConfigured

from pauth.providers import PAuthProvider
from pauth.views import Step2

class GoogleProvider(PAuthProvider):
    def __init__(self):
        self.scope = ['https://www.googleapis.com/auth/userinfo#email']

    def configure(self, conf):
        c = conf.get(self.name)
        if not c:
            raise ImproperlyConfigured("GoogleProvider requires configuration")
        self.client_id      = c['client_id']
        self.client_secret  = c['client_secret']
        self.access_type    = c.get('client_secret', 'offline')
        self.scope          += c.get('scope', [])

    def urls(self):
        return patterns('',
            (r'^google/$', Step2.as_view(), {'provider':'GoogleProvider'}),
        )

provider = GoogleProvider()
