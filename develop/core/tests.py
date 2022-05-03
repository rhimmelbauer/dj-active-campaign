from django.test import TestCase
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.models import Site

from dj_active_campaign.integrations import ActiveCampaignIntegration
from dj_active_campaign.active_campaign.connector import ActiveCampaignConnector
from dj_active_campaign.active_campaign.contact import ContactAPI


class TestActiveCampaignClass(TestCase):

    fixtures = ['site', 'user']

    def setUp(self):
        self.site = Site.objects.get(pk=1)

    def test_active_campaign_setup_success(self):
        active_campaign = ActiveCampaignConnector(self.site)
        self.assertTrue(active_campaign)

    def test_missing_credentials(self):
        with self.assertRaises(ObjectDoesNotExist):

            settings.ACTIVE_CAMPAIGN_KEY = None
            settings.ACTIVE_CAMPAIGN_URL = None
            settings.ACTIVE_CAMPAIGN_VERSION = None

            active_campaign = ActiveCampaignConnector(self.site)
    
    def test_are_credentials_valid_true(self):
        # Before you run this test make sure you have valid credentials
        active_campaign = ActiveCampaignConnector(self.site)

        self.assertTrue(active_campaign.are_credentials_valid())

    def test_are_credentials_valid_false(self):
        active_campaign = ActiveCampaignConnector(self.site)

        active_campaign.headers['Api-Token'] = 'YouShallNotPass'

        self.assertFalse(active_campaign.are_credentials_valid())


class TestContactAPICalls(TestCase):

    fixtures = ['site', 'user']

    def setUp(self):
        self.site = Site.objects.get(pk=1)
        self.contact = {
            'email': "don.ramon@mail.com",
            'first_name': 'Don',
            'last_name': 'Ramon'
        }

    def test_create_contact_success(self):
        contact_api = ContactAPI(self.site)

        contact_api.create(self.contact)

        self.assertTrue(contact_api.response.status_code, 2001)

    def test_create_contact_fail(self):
        contact_api = ContactAPI(self.site)

        del(self.contact['email'])

        with self.assertRaises(HTTPError):
            contact_api.create(self.contact)
