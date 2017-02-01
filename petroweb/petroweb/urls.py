"""petroweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from homepage.views import HomePageView, AboutView, HistoryView, ServicesView, OPECView, SovietView, CountryView, ContactView, PostView, PostsView, contact_form_handler
from django.views.decorators.csrf import csrf_exempt
from filebrowser.sites import site
from django.conf import settings

urlpatterns = [
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^about', AboutView.as_view(), name='about'),
    url(r'^history', HistoryView.as_view(), name='history'),
    url(r'^services/opec', OPECView.as_view(), name='opec'),
    url(r'^services/soviet', SovietView.as_view(), name='soviet'),
    url(r'^services/country', CountryView.as_view(), name='countries'),
    url(r'^services', ServicesView.as_view(), name='services'),
    url(r'^contact', ContactView.as_view(), name='contact'),
    url(r'^post/(?P<post_id>\w+)/$', PostView.as_view(), name='post'),
    url(r'^posts', PostsView.as_view(), name='posts'),
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^tinymce/', include('tinymce.urls')),
    # url(r'^mce_filebrowser/', include('mce_filebrowser.urls')),
    url(r'^send_form/', csrf_exempt(contact_form_handler), name='send_form'),
]

if settings.DEBUG :
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'^admin/media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ]