import os

from django.test import TestCase
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.sites.models import Site

from dj_active_campaign.integrations import ActiveCampaignIntegration
from dj_active_campaign.active_campaign.connector import ActiveCampaignConnector
from dj_active_campaign.active_campaign.contact import ContactAPI
from requests import HTTPError

class TestActiveCampaignClass(TestCase):

    fixtures = ['site', 'user']

    def setUp(self):
        self.site = Site.objects.get(pk=1)

    def test_active_campaign_setup_success(self):
        active_campaign = ActiveCampaignConnector(self.site)
        self.assertTrue(active_campaign)

    def test_missing_credentials(self):
        with self.assertRaises(ObjectDoesNotExist):

            settings.ACTIVE_CAMPAIGN_VERSION = None

            active_campaign = ActiveCampaignConnector(self.site)
        
        settings.ACTIVE_CAMPAIGN_VERSION = os.getenv("ACTIVE_CAMPAIGN_VERSION", None)
    
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
        self.contact_api = ContactAPI(self.site)
        self.contact = {
            'email': "don.ramon@mail.com",
            'firstName': 'Don',
            'lastName': 'Ramon'
        }

    def test_create_contact_success(self):
        self.contact_api.create(self.contact)

        self.assertEquals(self.contact_api.response.status_code, 201)

    def test_create_contact_fail(self):
        del(self.contact['email'])

        with self.assertRaises(KeyError):
            self.contact_api.create(self.contact)

    def test_query_contact(self):
        self.contact_api.query({'email': self.contact['email']})

        self.assertEqual(self.contact_api.response.status_code, 200)
    
    def test_update_contact(self):
        self.contact_api.update({'email': self.contact['email'], 'lastName': 'Jamon'})

        self.assertEqual(self.contact_api.response.status_code, 200)

    def test_remove_contact(self):
        self.contact_api.query()

        contacts = self.contact_api.response.json().get('contacts', [])

        if contacts:
            self.contact_api.remove(contacts[0]['id'])

            self.assertEqual(self.contact_api.response.status_code, 200)