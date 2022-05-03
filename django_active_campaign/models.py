from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import gettext_lazy as _

class CustomFields(models.Model):
    # site = models.ForeignKey(Site, verbose_name=_("Site"), on_delete=models.CASCADE, default=set_default_site_id, related_name="product_offers")
    ac_id = models.IntegerField(_("Active Campaign ID"))
    ac_title = models.CharField(_("Field Title"), max_length=50)
    ac_value = models.JSONField(_("Field Value"))
    required = models.BooleanField(_("Required"), default=False)

    class Meta:
        verbose_name = "Custom Field"
        verbose_name_plural = "Custom Fields"

    def __str__(self):
        return f"{ac_id} - {self.ac_title}"