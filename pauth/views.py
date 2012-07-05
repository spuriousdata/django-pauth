from django.views.generic import TemplateView

class Loggin(TemplateView):
    def get(self):
        self.redirect(external_auth_url)

