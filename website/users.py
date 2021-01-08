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

@hooks.register('register_account_menu_item')
def register_account_set_instagram(request):
    return {
        'url': reverse('website_templates_wagtailusers_shoes'),
        'label': _('Add your shoes'),
        'help_text': _("Add your shoes")
    }









class BioForm(forms.ModelForm):
    bio = forms.CharField(required=False, label=_('Your bio'))


    class Meta:
        model = UserProfile
        fields = ("bio",)


def change_bio(request):
    if request.method == 'POST':
        form = BioForm(request.POST, instance=UserProfile.get_for_user(request.user))

        if form.is_valid():
            form.save()


            messages.success(request, _("Your bio has been changed successfully!"))
            return redirect('wagtailadmin_account')
    else:
        form = BioForm(instance=UserProfile.get_for_user(request.user))

    return TemplateResponse(request, 'coderedcms/wagtailusers/change_bio.html', {
        'form': form,
    })
