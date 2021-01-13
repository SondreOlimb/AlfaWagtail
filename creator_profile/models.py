from django.db import models

from coderedcms.models import (
    CoderedArticlePage,
    CoderedArticleIndexPage,
    CoderedEmail,
    CoderedFormPage,
    CoderedWebPage
)

import website.models

class ProfilePage(CoderedWebPage):
    class Meta:
        verbose_name = "Profile page"

    # Override to specify custom index ordering choice/default.


    # Only allow CupcakesPages beneath this page.
    parent_page_types = ['creator_profile.ProfileIndexPage']

    template = 'coderedcms/pages/profile_page.html'

    layout_panels = CoderedWebPage.layout_panels

    def get_context(self, request, *args, **kwargs):
        """adding custom stuff to our content"""

        context = super().get_context(request,*args,**kwargs)



        context["posts"] = website.models.AdventurePage.objects.live().public().specific().order_by('-first_published_at').filter(owner=self.owner)

        return context

# Create your models here.
class ProfileIndexPage(CoderedWebPage):

    class Meta:
        verbose_name = "Profile index page"

    # Override to specify custom index ordering choice/default.
    index_query_pagemodel = 'creator_profile.ProfilePage'

    # Only allow CupcakesPages beneath this page.
    subpage_types = ['creator_profile.ProfilePage']

    template = 'coderedcms/pages/profile_index_page.html'

    layout_panels = CoderedWebPage.layout_panels




