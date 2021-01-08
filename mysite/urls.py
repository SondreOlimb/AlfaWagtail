from django.conf import settings
from django.conf.urls import url
from django.urls import include, path, re_path
from django.contrib import admin
from wagtail.documents import urls as wagtaildocs_urls
from coderedcms import admin_urls as coderedadmin_urls
from coderedcms import search_urls as coderedsearch_urls
from coderedcms import urls as codered_urls
from website import users
from website.profile import account

urlpatterns = [
    # Admin
    path('django-admin/', admin.site.urls),
    path('admin/', include(coderedadmin_urls)),

    #url for profile bio
    url(r'account/change_bio/$', users.change_bio, name='website_templates_wagtailusers_change_bio'),
    url(r'account/change_instagram/$', account.change_instagram, name='website_templates_wagtailusers_instagram'),
    url(r'account/change_shoes/$', account.change_shoes, name='website_templates_wagtailusers_shoes'),

    # Documents
    path('docs/', include(wagtaildocs_urls)),

    # Search
    path('search/', include(coderedsearch_urls)),

    # For anything not caught by a more specific rule above, hand over to
    # the page serving mechanism. This should be the last pattern in
    # the list:
    re_path(r'', include(codered_urls)),

    # Alternatively, if you want CMS pages to be served from a subpath
    # of your site, rather than the site root:
    #    re_path(r"^pages/", include(codered_urls)),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
