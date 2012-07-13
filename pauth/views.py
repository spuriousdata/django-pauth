from django.views.generic import TemplateView, RedirectView

from pauth import loaded_providers

class Login(TemplateView):
    def get(self, provider):
        loaded_providers[provider].login()

class Step2(TemplateView):
    def get(self, provider, **kwargs):
        loaded_providers[provider].callback(**kwargs)

