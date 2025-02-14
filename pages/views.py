from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(TemplateView):
    template_name = "home.html"


class ProfilePageView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
