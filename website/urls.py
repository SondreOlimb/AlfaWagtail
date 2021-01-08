from django.conf.urls import url

from wagtail.admin.views import page_privacy, pages

from .users import change_bio
from wagtail.users.models import UserProfile


UserProfile.bio
urlpatterns = [
    url(r'account/change_bio/$', change_bio, name='website_templates_wagtailusers_change_bio.html'),
]

