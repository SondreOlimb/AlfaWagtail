from . forms import *
from .models import ExtUserProfile

from django.contrib import messages
from django.template.response import TemplateResponse
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


def change_instagram(request):
    if request.method == 'POST':
        form = InstagramForm(request.POST, instance=ExtUserProfile.get_for_user(request.user))

        if form.is_valid():
            form.save()


            messages.success(request, _("Your Instagram has been changed successfully!"))
            return redirect('wagtailadmin_account')
    else:
        form = InstagramForm(instance=ExtUserProfile.get_for_user(request.user))

    return TemplateResponse(request, 'coderedcms/wagtailusers/instagram.html', {
        'form': form,
    })