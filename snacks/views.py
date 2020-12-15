from django.views.generic import TemplateView

#link to urls
class HomeView(TemplateView):
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"