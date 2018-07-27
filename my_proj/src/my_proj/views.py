from django.views import generic


class HomePage(generic.TemplateView):
    template_name = "home.html"


class AboutPage(generic.TemplateView):
    template_name = "about.html"

class PricingPage(generic.TemplateView):
    template_name = "pricing.html"
