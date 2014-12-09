from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fuckfinder_backend.views.home', name='home'),
    url(r'^api/', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
