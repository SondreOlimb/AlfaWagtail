from django.urls import reverse
from wagtail.users.models import UserProfile
from wagtail.users.forms import UserEditForm, UserCreationForm
from wagtail.core import hooks


from django import forms
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.template.response import TemplateResponse
from django.shortcuts import redirect

from django.utils.translation import gettext_lazy as _

@hooks.register('register_account_menu_item')
def register_account_set_profile_bio(request):
    return {
        'url': reverse('website_templates_wagtailusers_change_bio'),
        'label': _('Change your bio'),
        'help_text': _("Change your bio.")
    }



@hooks.register('register_account_menu_item')
def register_account_set_instagram(request):
    return {
        'url': reverse('website_templates_wagtailusers_instagram'),
        'label': _('Change/Add your Instagram'),
        'help_text': _("Change/Add your Instagram")
    }