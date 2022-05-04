from django.contrib import admin
from dj_active_campaign.models import CustomField


class CustomFieldAdmin(admin.ModelAdmin):
    list_display = ('pk', 'ac_id', 'ac_title', 'ac_type')
    search_fields = ('ac_id', 'ac_title', )
    list_filter = ('ac_type', )


admin.site.register(CustomField, CustomFieldAdmin)