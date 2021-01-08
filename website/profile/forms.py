from django import forms
from .models import ExtUserProfile
from django.utils.translation import gettext_lazy as _


class InstagramForm(forms.ModelForm):
    instagram = forms.URLField(required=False, label=_('Your Instagram'))


    class Meta:
        model = ExtUserProfile
        fields = ("instagram",)