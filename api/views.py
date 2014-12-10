from rest_framework.renderers import JSONRenderer
from rest_framework import generics


from django.shortcuts import get_object_or_404
from django.db.models import F
from django.contrib.gis.measure import D
from django.contrib.gis.geos import (Point, fromstr, fromfile, GEOSGeometry, MultiPolygon, Polygon)
from django.http import JsonResponse

from models import FuckFinderUser
from .serializers import FuckFinderUserListSerializer


class FuckFinderList(generics.ListCreateAPIView):
    serializer_class = FuckFinderUserListSerializer

    def get_queryset(self):
        queryset = FuckFinderUser.objects.all()
        return queryset


class FuckFinderDetail(generics.RetrieveUpdateDestroyAPIView):
    model = FuckFinderUser
    serializer_class = FuckFinderUserListSerializer


def hetero_desires(finder):
    if finder.sex == 'F':
        return 'M'
    else:
        return 'F'


def fetch_fuckfinder_proposals_for(request, nick_of_x, current_latitude, current_longitiude, limit=10):

    finder = get_object_or_404(FuckFinderUser, nickname=nick_of_x)
    finder_location = Point(float(current_longitiude), float(current_latitude))

    # consider by performance benchmarks, either first sex_age queries OR geo

    if finder.prefered_sex == finder.sex:
        # deal with homosexual
        candidates = FuckFinderUser.objects.filter(
            prefered_sex=finder.sex,
            sex=finder.prefered_sex,
            age__range=(finder.prefered_age_min, finder.prefered_age_max),
            prefered_age_min__lte=finder.age,
            prefered_age_max__gte=finder.age,
        ).exclude(nickname=finder.nickname)
    else:
        # deal with heterosexual:
        candidates = FuckFinderUser.objects.filter(
            sex=hetero_desires(finder),
            age__range=(finder.prefered_age_min, finder.prefered_age_max),
            prefered_age_min__lte=finder.age,
            prefered_age_max__gte=finder.age,
        ).exclude(sex=F('prefered_sex')).exclude(nickname=finder.nickname)

    # do geo queries
    candidates_inside_finder_radius_and_vice_versa = candidates.filter(
        last_location__distance_lte=(
            finder_location,
            D(km=min(finder.prefered_radius, F('friendly_rate'))))
        ).distance(finder_location).order_by('distance')[:limit]

    serializer = FuckFinderUserListSerializer(
        candidates_inside_finder_radius_and_vice_versa, many=True)

    return JsonResponse(serializer.data, safe=False)

