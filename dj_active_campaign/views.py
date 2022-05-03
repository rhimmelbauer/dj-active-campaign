from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView


class IndexView(TemplateView):
    template_name = "dj_active_campaign/index.html"



    