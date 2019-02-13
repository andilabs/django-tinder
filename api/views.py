from rest_framework import generics

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point
from django.db.models import F, IntegerField
from django.db.models.functions import Least
from django.shortcuts import get_object_or_404

from api.models import DjTinderUser
from api.serializers import DjTinderUserListSerializer


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

        queryset = queryset.filter(
            sex=finder.sex if finder.homo else finder.get_opposed_sex,
            preferred_sex=finder.sex,
            age__range=(
                finder.preferred_age_min,
                finder.preferred_age_max),
            preferred_age_min__lte=finder.age,
            preferred_age_max__gte=finder.age,
        ).exclude(
            nickname=finder.nickname
        )
        return queryset
