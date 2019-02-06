#!/usr/bin/python
# -*- coding: utf-8 -*-

from rest_framework import serializers

from django.contrib.gis.geos import fromstr

from api.models import DjTinderUser, SEX_CHOICES


class DjTinderUserListSerializer(serializers.ModelSerializer):
    prefered_sex = serializers.ChoiceField(choices=SEX_CHOICES, default='male')
    sex = serializers.ChoiceField(choices=SEX_CHOICES, default='male')

    class Meta:
        model = DjTinderUser
        fields = "__all__"

    def to_representation(self, instance):
        ret = super(DjTinderUserListSerializer, self).to_representation(instance)
        pnt = fromstr(ret['last_location'])
        ret['last_location'] = {'longitude': pnt.coords[0], 'latitude': pnt.coords[1]}
        return ret
