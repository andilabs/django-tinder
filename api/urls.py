#!/usr/bin/python
# -*- coding: utf-8 -*-
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('',
    url(r'^fuckfindeusers/$', views.FuckFinderList.as_view(), name="fuckfinderuser-list"),
    url(r'^fuckfindeusers/(?P<pk>\d+)/$', views.FuckFinderDetail.as_view(), name="fuckfinderuser-detail"),
    url(r'fetch_fuckfinder_proposals_for/(?P<nick_of_finder>[^/]+)/(?P<current_latitude>-?\d{2,3}.\d{5})/(?P<current_longitiude>-?\d{2,3}.\d{5})/$', views.fetch_fuckfinder_proposals_for, name='fuckfinder_proposals'),
)
urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])