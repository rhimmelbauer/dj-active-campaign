from django.urls import path, re_path
from dj_active_campaign import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='dj_active_campaign-index'),
    path('custom/fields/', views.CustomFieldsListView.as_view(), name='custom-fields'),
    # path('simple/', views.PackageView.as_view(), name='dj_active_campaign-simple'),
    # path('simple/<slug:slug>/', views.VersionView.as_view(), name='dj_active_campaign-simple-version'),
]

