from wagtail.contrib.settings.models import BaseSetting, register_setting
from django.db import models
from django.utils.translation import gettext_lazy as _
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel


@register_setting(icon='fa-map')
class MapboxApiApiSettings(BaseSetting):
    """
    Settings for MapBox API services.
    """
    class Meta:
        verbose_name = _('MapBox API')

    mapbox_maps_api_key = models.CharField(
        blank=True,
        max_length=255,
        verbose_name=_('MapBox API Key'),
        help_text=_('The API Key used for Mapbox.')
    )

    panels = [
        MultiFieldPanel([
            FieldPanel("mapbox_maps_api_key"),

        ], heading="MapBox Settings")
    ]