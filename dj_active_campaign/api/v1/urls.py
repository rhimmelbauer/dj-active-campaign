from django.urls import path

from dj_active_campaign.api import views

app_name = "dj_active_campaign_api"

urlpatterns = [
    path('custom/field/<str:uuid>/create/', views.ActiveCampaignCustomFieldCreate.as_view(), name='ac-custom-field-create'),
    path('contact/<str:uuid>/create/', views.CreateCustomerInActiveCampaign.as_view(), name='ac-custom-field-create'),
]