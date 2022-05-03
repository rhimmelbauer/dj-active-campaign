import requests

from django.core.exceptions import ObjectDoesNotExist
from dj_active_campaign.active_campaign.connector import ActiveCampaignConnector


class CustomFieldAPI(ActiveCampaignConnector):
    RELATIVE_URL = 'fields'

    def query(self, params=None):
        self.get(self.RELATIVE_URL, params)

    def create(self, data):
        self.validate_call(data)

        self.post(self.RELATIVE_URL, {'contact': data})

    def update(self, data):
        self.validate_call(data)

        contact_id = self.get_user_id(data['email'])

        self.put(self.RELATIVE_URL + f'/{contact_id}', data={'contact': data})

    def remove(self, id):
        self.delete(self.RELATIVE_URL + f'/{id}')