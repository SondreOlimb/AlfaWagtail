from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    MultiFieldPanel,
    StreamFieldPanel)
from wagtail.core.fields import StreamField
from wagtail.core.models import Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet
from wagtail.images import get_image_model_string
from wagtail.snippets.edit_handlers import SnippetChooserPanel


from coderedcms.blocks import HTML_STREAMBLOCKS, LAYOUT_STREAMBLOCKS, NAVIGATION_STREAMBLOCKS
from coderedcms.settings import cr_settings


class ShoeOrderable(Orderable):
    """This allows us to select one or more blog authors from Snippets."""

    page = ParentalKey("website.AdventurePage", related_name="shoe_model")
    shoe = models.ForeignKey(
        "website.Shoes",
        on_delete=models.CASCADE,
    )

    panels = [
    	# Use a SnippetChooserPanel because shoes is registered as a snippet
        SnippetChooserPanel("shoe"),
    ]

@register_snippet
class Shoes(ClusterableModel):
    """
    Simple and generic model to add shoe models
    """
    class Meta:
        verbose_name = _('Shoes')
        verbose_name_plural = _('Shoes')
        ordering = ['shoe_name']


    shoe_name = models.CharField(
        max_length=255,
        verbose_name=_('Name'),
    )

    shoe_photo = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Cupcake Photo',
    )

    shoe_URL = models.URLField(
        blank=True,
        verbose_name=_('AlfaModel'),
        help_text=_('Link to the model on alfa.no'),
    )

    panels = [
        FieldPanel('shoe_name'),
        ImageChooserPanel("shoe_photo"),
        FieldPanel('shoe_URL'),
    ]

    def __str__(self):
        """string representation of this class"""
        return self.shoe_name




