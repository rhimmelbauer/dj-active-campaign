from django.shortcuts import redirect
from django.views.generic import View
from django.urls import reverse_lazy

from dj_active_campaign.models import CustomField, CustomFieldTypes
from dj_active_campaign.active_campaign import ContactAPI, CustomFieldAPI


class ActiveCampaignCustomFieldCreate(View):
    success_url = reverse_lazy('custom-fileds')

    def post(self, request, *args, **kwargs):
        custom_field = CustomField.on_site.get(uuid=kwargs.get('uuid'))

        custom_field_api = CustomFieldAPI(get_site_from_request(request))
        custom_field_api.create({'type': custom_field.ac_type, 'title': custom_field.ac_title})

        if not custom_field_api.is_response_valid():
            logger.error(custom_field_api.errors)

            return redirect('custom-fields')

        custom_field.ac_id = custom_field_api.response.json()['field']['id']
        custom_field.save()
        
        return redirect(request.META.get('HTTP_REFERER', self.success_url))


class CreateCustomerInActiveCampaign(View):
    success_url = reverse_lazy('dj-active-campaign-index')

    def post(self, request, *args, **kwargs):
        site = get_site_from_request(request)
        contact_api = ContactAPI(site)

        contact_api.create(request.POST)

        return redirect(request.META.get('HTTP_REFERER', self.success_url))
