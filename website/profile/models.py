from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db import models

from wagtail.users.models import UserProfile


from modelcluster.fields import ParentalKey
from coderedcms.forms import CoderedFormField
from coderedcms.models import (
    CoderedArticlePage,
    CoderedArticleIndexPage,
    CoderedEmail,
    CoderedFormPage,
    CoderedWebPage
)

from ..snippets import *


class ExtUserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='wagtail_extended_userprofile'
    )

    instagram = models.URLField(
        verbose_name=_('Instagram url'),
        max_length=255,
        help_text=_("Add your instagram"),
        default=''
    )

    shoes = models.ManyToManyField(Shoes)

    @classmethod
    def get_for_user(cls, user):
        return cls.objects.get_or_create(user=user)[0]
