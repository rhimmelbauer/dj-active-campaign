from dj_active_campaign.models import CustomField

from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, View

class IndexView(TemplateView):
    template_name = "dj_active_campaign/index.html"

class CustomFieldsListView(ListView):
    template_name = "dj_active_campaign/custom_fields.html"
    model = CustomField

    def get_queryset(self):
        return CustomField.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context['custom_fields'] = self.get_queryset()

        return context

class CreateCustomFieldInActiveCampaign(View):

    def post(self, request, *args, **kwargs):

        return redirect('custom-fields')