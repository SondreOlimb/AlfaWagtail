"""
Createable pages used in CodeRed CMS.
"""
from django.conf import settings
from django.utils.translation import gettext_lazy as _


from modelcluster.fields import ParentalKey
from coderedcms.forms import CoderedFormField
from coderedcms.models import (
    CoderedArticlePage,
    CoderedArticleIndexPage,
    CoderedEmail,
    CoderedFormPage,
    CoderedWebPage
)

from django.db import models
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


from .snippets import *







class ArticlePage(CoderedArticlePage):
    """
    Article, suitable for news or blog content.
    """
    class Meta:
        verbose_name = 'Article'
        ordering = ['-first_published_at']

    # Only allow this page to be created beneath an ArticleIndexPage.
    parent_page_types = ['website.ArticleIndexPage']

    template = 'coderedcms/pages/article_page.html'
    amp_template = 'coderedcms/pages/article_page.amp.html'
    search_template = 'coderedcms/pages/article_page.search.html'


class ArticleIndexPage(CoderedArticleIndexPage):
    """
    Shows a list of article sub-pages.
    """
    class Meta:
        verbose_name = 'Article Landing Page'

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = 'website.ArticlePage'

    # Only allow ArticlePages beneath this page.
    subpage_types = ['website.ArticlePage']

    template = 'coderedcms/pages/article_index_page.html'


class FormPage(CoderedFormPage):
    """
    A page with an html <form>.
    """
    class Meta:
        verbose_name = 'Form'

    template = 'coderedcms/pages/form_page.html'


class FormPageField(CoderedFormField):
    """
    A field that links to a FormPage.
    """
    class Meta:
        ordering = ['sort_order']

    page = ParentalKey('FormPage', related_name='form_fields')


class FormConfirmEmail(CoderedEmail):
    """
    Sends a confirmation email after submitting a FormPage.
    """
    page = ParentalKey('FormPage', related_name='confirmation_emails')


class WebPage(CoderedWebPage):
    """
    General use page with featureful streamfield and SEO attributes.
    Template renders all Navbar and Footer snippets in existance.
    """
    class Meta:
        verbose_name = 'Web Page'

    template = 'coderedcms/pages/web_page.html'


class AdventureIndexPage(CoderedWebPage):
    """
    Landing page for Adventures
    """
    class Meta:
        verbose_name = "Adventure Landing Page"

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = 'website.AdventurePage'

    # Only allow CupcakesPages beneath this page.
    subpage_types = ['website.AdventurePage']

    template = 'coderedcms/pages/adventure_index_page.html'

    layout_panels = CoderedWebPage.layout_panels




class AdventurePage(CoderedWebPage):
    """
    Custom page for individual Adventure blogs
    """

    class Meta:
        verbose_name = "Adventure Page"

    # Only allow this page to be created beneath an CupcakesIndexPage.
    parent_page_types = ['website.AdventureIndexPage']

    template = "coderedcms/pages/adventure_page.html"

    #layout_panels = CoderedWebPage.layout_panels

    banner_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name='Adventure Photo',
    )

    caption = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Caption'),
    )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Author'),
    )
    author_display = models.CharField(
        max_length=255,
        blank=True,
        verbose_name=_('Display author as'),
        help_text=_('Override how the author’s name displays on this article.'),
    )
    date_display = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Display publish date'),
    )

    def get_author_name(self):
        """
        Gets author name using a fallback.
        """
        if self.author_display:
            return self.author_display
        if self.author:
            return self.author.get_full_name()
        return ''

    def get_pub_date(self):
        """
        Gets published date.
        """
        if self.date_display:
            return self.date_display
        return ''

    def get_description(self):
        """
        Gets the description using a fallback.
        """
        if self.search_description:
            return self.search_description
        if self.caption:
            return self.caption
        if self.body_preview:
            return self.body_preview
        return ''

    search_fields = (
            CoderedWebPage.search_fields +
            [
                index.SearchField('caption', boost=2),
                index.FilterField('author'),
                index.FilterField('author_display'),
                index.FilterField('date_display'),
            ]
    )

    # Add custom fields to the body
    body_content_panels = CoderedWebPage.body_content_panels + [

        ImageChooserPanel("banner_image"),
        FieldPanel('caption'),
        MultiFieldPanel(
            [
                FieldPanel('author'),
                FieldPanel('author_display'),
                FieldPanel('date_display'),
            ],
            _('Publication Info')
        ),
        MultiFieldPanel(
            [
                InlinePanel("shoe_model", label="Shoe", min_num=0, max_num=4)
            ],
            heading="Shoe(s)"
        )
    ]




