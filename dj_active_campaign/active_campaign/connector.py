import requests

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from dj_active_campaign.integrations import ActiveCampaignIntegration


class ActiveCampaignConnector(object):

    def __init__(self, site):
        active_campaign_credentials = ActiveCampaignIntegration(site)

        if active_campaign_credentials.instance:
            self.url = active_campaign_credentials.client_url + active_campaign_credentials.client_id
            self.header = {
                'Api-Token': active_campaign_credentials.private_key
            }
        elif settings.ACTIVE_CAMPAIGN_URL and settings.ACTIVE_CAMPAIGN_KEY and settings.ACTIVE_CAMPAIGN_VERSION:
            self.url = settings.ACTIVE_CAMPAIGN_URL + settings.ACTIVE_CAMPAIGN_VERSION
            self.header = {
                'Api-Token': settings.ACTIVE_CAMPAIGN_KEY
            }
        else:
            raise ObjectDoesNotExist("Active Campaign Credentials are not set")
        

    def are_credentials_valid(self):
        response = requests.get(self.url + 'campaigns', headers=self.header)
        
        if response.status_code == 200:
            return True
        
        return False
