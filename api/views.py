from rest_framework import generics

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.db.models import F, IntegerField
from django.db.models.functions import Least
from django.shortcuts import get_object_or_404

from api.models import DjTinderUser
from api.serializers import DjTinderUserListSerializer


class DjTinderList(generics.ListCreateAPIView):
    serializer_class = DjTinderUserListSerializer

    def get_queryset(self):
        queryset = DjTinderUser.objects.all()
        return queryset


class DjTinderDetail(generics.RetrieveUpdateDestroyAPIView):
    model = DjTinderUser
    serializer_class = DjTinderUserListSerializer


class ProposalsApiView(generics.ListAPIView):

    serializer_class = DjTinderUserListSerializer
    queryset = DjTinderUser.objects.all()

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        finder = get_object_or_404(
            DjTinderUser,
            nickname=self.kwargs.get('user_nick')
        )
        current_user_location = Point(
            float(self.kwargs.get('current_longitude')),
            float(self.kwargs.get('current_latitude')),
            srid=4326
        )
        # we annotate each object with smaller of two radius:
        # - requesting user
        # - and each user preferred_radius
        # we annotate queryset with distance between given in params location
        # (current_user_location) and each user location
        queryset = queryset.annotate(
            smaller_radius=Least(
                finder.preferred_radius,
                F('preferred_radius'),
                output_field=IntegerField()
            ),
            distance=Distance('last_location', current_user_location)
        ).filter(
            distance__lte=F('smaller_radius') * 1000
        ).order_by(
            'distance'
        )

        if finder.preferred_sex == finder.sex:
            # deal with homosexual
            queryset = queryset.filter(
                preferred_sex=finder.sex,
                sex=finder.preferred_sex,
                age__range=(
                    finder.preferred_age_min,
                    finder.preferred_age_max),
                preferred_age_min__lte=finder.age,
                preferred_age_max__gte=finder.age,
            ).exclude(
                nickname=finder.nickname
            )
        else:
            # deal with heterosexual:
            queryset = queryset.filter(
                sex=finder.hetero_desires(),
                age__range=(
                    finder.preferred_age_min,
                    finder.preferred_age_max),
                preferred_age_min__lte=finder.age,
                preferred_age_max__gte=finder.age,
            ).exclude(
                sex=F('preferred_sex'),
                nickname=finder.nickname
            )
        return queryset
