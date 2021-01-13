"""
Createable pages used in CodeRed CMS.
"""
from django.conf import settings
from django.utils.translation import gettext_lazy as _

from coderedcms.forms import CoderedFormField
from coderedcms.models import (
    CoderedArticlePage,
    CoderedArticleIndexPage,
    CoderedEmail,
    CoderedFormPage,
    CoderedWebPage,
    CoderedPage
)

from wagtail.search import index


from .snippets import *
from .users import *

from streams import blocks
import creator_profile.models


import requests
import polyline
from mysite.settings.base import STRAVA_CLIENT_ID, STRAVA_CLIENT_SECRET,STRAVA_REFRESH_TOKEN

from coderedcms.models.snippet_models import ClassifierTerm








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

    body_content_panels = CoderedWebPage.body_content_panels






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

    index_show_subpages_default = True

    index_order_by_default = '-date_display'
    index_order_by_choices = (('-date_display', 'Display publish date, newest first'),) + \
                             CoderedWebPage.index_order_by_choices

    show_images = models.BooleanField(
        default=True,
        verbose_name=_('Show images'),
    )
    show_captions = models.BooleanField(
        default=True,
    )
    show_meta = models.BooleanField(
        default=True,
        verbose_name=_('Show author and date info'),
    )
    show_preview_text = models.BooleanField(
        default=True,
        verbose_name=_('Show preview text'),
    )

    layout_panels = CoderedWebPage.layout_panels + [
        MultiFieldPanel(
            [
                FieldPanel('show_images'),
                FieldPanel('show_captions'),
                FieldPanel('show_meta'),
                FieldPanel('show_preview_text'),
            ],
            heading=_('Child page display')
        ),
    ]





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


    lat = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_('Latitude'),
        help_text="Latitude of the destination"
    )
    lng = models.FloatField(
        null=True,
        blank=True,
        verbose_name=_('Longitude'),
        help_text="Longitude of the destination"
    )
    strava = models.CharField(max_length=255, null=True, blank=True, verbose_name=_("Strava"), help_text="Strava activity id")

    trip_polyline = models.CharField(max_length=100000, null=True, blank=True)



    def get_polyline(self):
        if self.trip_polyline:
            path = polyline.decode(self.trip_polyline, geojson=True)
            poly = []

            for i in path:
                poly.append([i[0], i[1]])
            return poly
        elif not self.trip_polyline:
            auth_url = "https://www.strava.com/oauth/token"
            # activites_url = "https://www.strava.com/api/v3/athlete/activities/{4056947490}"
            activites_url = "https://www.strava.com/api/v3/activities/" + str(self.strava)

            payload = {
                'client_id': STRAVA_CLIENT_ID,
                'client_secret': STRAVA_CLIENT_SECRET,
                'refresh_token': STRAVA_REFRESH_TOKEN,
                'grant_type': "refresh_token",
                'f': 'json'
            }



            res = requests.post(auth_url, data=payload, verify=False)
            access_token = res.json()["access_token"]

            header = {'Authorization': 'Bearer ' + access_token}
            param = {'per_page': 2, 'page': 1}
            my_dataset = requests.get(activites_url, headers=header, params=param).json()
            strava_tempsave = my_dataset["map"]["polyline"]
            path = polyline.decode(strava_tempsave, geojson=True)

            self.trip_polyline = strava_tempsave
            self.save()

            poly = []
            test = "Test"
            for i in path:
                poly.append([i[0], i[1]])
            return poly

        else:
            self.trip_polyline = "ERROR"
            self.trip_polyline.save()
            return "error"


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


    def get_context(self, request, *args, **kwargs):
        """adding custom stuff to our content"""

        context = super().get_context(request,*args,**kwargs)



        context["profile"] = creator_profile.models.ProfilePage.objects.live().public().specific().filter(owner=self.owner)




        return context

    body = StreamField(blocks.LAYOUT_STREAMBLOCKS, null=True, blank=True)

    search_fields = (
            CoderedPage.search_fields +
            [index.SearchField('body'),
             index.SearchField('caption', boost=2),
             index.FilterField('author'),
             index.FilterField('author_display'),
             index.FilterField('date_display'),
             ]
    )

    # Panels
    body_content_panels = [
        StreamFieldPanel('body'),
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
                FieldPanel('lat'),
                FieldPanel('lng'),
                FieldPanel('strava'),
                FieldPanel('trip_polyline')
            ],
            _('Trip info')
        ),
        MultiFieldPanel(
            [
                InlinePanel("shoe_model", label="Shoe", min_num=0, max_num=4)
            ],
            heading="Shoe(s)"
        )
    ]

"""
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
"""


class MapPage(CoderedWebPage):
    """
    General use page with featureful streamfield and SEO attributes.
    Template renders all Navbar and Footer snippets in existance.
    """





    class Meta:
        verbose_name = 'Map Page'



    template = 'coderedcms/pages/map_page.html'

    body = StreamField(blocks.LAYOUT_STREAMBLOCKS, null=True, blank=True)

    search_fields = (
            CoderedPage.search_fields +
            [index.SearchField('body')]
    )



    # Panels
    body_content_panels = [
        StreamFieldPanel('body'),
    ]

    def get_context(self, request, *args, **kwargs):
        """adding custom stuff to our content"""

        context = super().get_context(request,*args,**kwargs)



        context["posts"] = AdventurePage.objects.live().public().specific()

        if True:
            # Get child pages
            all_children = AdventurePage.objects.live().public().specific()
            # Filter by classifier terms if applicable
            if len(request.GET) > 0 and self.index_classifiers.exists():
                # Look up comma separated ClassifierTerm slugs i.e. `/?c=term1-slug,term2-slug`
                terms = []
                get_c = request.GET.get('c', None)
                if get_c:
                    terms = get_c.split(',')
                # Else look up individual querystrings i.e. `/?classifier-slug=term1-slug`
                else:
                    for classifier in self.index_classifiers.all().only('slug'):
                        get_term = request.GET.get(classifier.slug, None)
                        if get_term:
                            terms.append(get_term)
                if len(terms) > 0:
                    selected_terms = ClassifierTerm.objects.filter(slug__in=terms)
                    context['selected_terms'] = selected_terms
                    if len(selected_terms) > 0:
                        try:
                            for term in selected_terms:
                                all_children = all_children.filter(classifier_terms=term)
                        except AttributeError:
                            print("error")




            context['index_children'] = all_children





        print(context)

        return context




