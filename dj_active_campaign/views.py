from dj_active_campaign.models import CustomField
from dj_active_campaign.active_campaign.custom_field import CustomFieldAPI

from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, View


def get_site_from_request(request):
    if hasattr(request, 'site'):
        return request.site
    return get_current_site(request)


class IndexView(TemplateView):
    template_name = "dj_active_campaign/index.html"

class CustomFieldsListView(ListView):
    template_name = "dj_active_campaign/custom_fields.html"
    model = CustomField

    def get_queryset(self):
        return CustomField.on_site.all()


class CreateCustomFieldInActiveCampaign(View):

    def post(self, request, *args, **kwargs):
        custom_field = CustomField.on_site.get(uuid=kwargs.get('uuid'))

        custom_field_api = CustomFieldAPI(get_site_from_request(request))
        custom_field_api.create({'type': custom_field.ac_type, 'title': custom_field.ac_title})

        if not custom_field_api.is_response_valid():
            print(error)
            return redirect('custom-fields')

        custom_field.ac_id = custom_field_api.response.json()['field']['id']
        custom_field.save()
        
        return redirect('custom-fields')