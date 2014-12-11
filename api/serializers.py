#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from rest_framework.pagination import PaginationSerializer

from django.contrib.gis.geos import fromstr

from models import FuckFinderUser, SEX_CHOICES


class FuckFinderUserListSerializer(serializers.ModelSerializer):
    prefered_sex = serializers.ChoiceField(choices=SEX_CHOICES, default='male')
    sex = serializers.ChoiceField(choices=SEX_CHOICES, default='male')

    class Meta:
        model = FuckFinderUser

    def to_representation(self, instance):
        ret = super(FuckFinderUserListSerializer, self).to_representation(instance)
        pnt = fromstr(ret['last_location'])
        ret['last_location'] = {'longitude': pnt.coords[0], 'latitude': pnt.coords[1]}
        return ret


class PaginatedFuckFinderUserListSerializer(PaginationSerializer):

    class Meta:
        object_serializer_class = FuckFinderUserListSerializer


