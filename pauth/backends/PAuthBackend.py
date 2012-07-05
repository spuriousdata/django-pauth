from django.util.importlib import import_module as im

class PAuthBackend(object):
    supports_anonymous_user = False

    def authenticate(self, username=None, password=None):
        pass
