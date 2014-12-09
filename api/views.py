from rest_framework.renderers import JSONRenderer
from rest_framework import generics


from django.shortcuts import get_object_or_404
from django.db.models import F
from django.contrib.gis.measure import D
from django.contrib.gis.geos import (Point, fromstr, fromfile, GEOSGeometry, MultiPolygon, Polygon)
from django.http import JsonResponse
from django.http import HttpResponse

from models import FuckFinderUser
from .serializers import FuckFinderUserListSerializer


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


class FuckFinderList(generics.ListCreateAPIView):
    serializer_class = FuckFinderUserListSerializer

    def get_queryset(self):
        queryset = FuckFinderUser.objects.all()
        return queryset


class FuckFinderDetail(generics.RetrieveUpdateDestroyAPIView):
    model = FuckFinderUser
    serializer_class = FuckFinderUserListSerializer


def fetch_fuckfinder_proposals_for(request, nick_of_x, current_latitude, current_longitiude, limit=10):

    finder = get_object_or_404(FuckFinderUser, nickname=nick_of_x)

    finder_location = Point(float(current_longitiude), float(current_latitude))

    candidates = FuckFinderUser.objects.filter(
        sex=finder.prefered_sex,
        age__range=(finder.prefered_age_min, finder.prefered_age_max),
        prefered_age_min__lte=finder.age,
        prefered_age_max__gte=finder.age
    )

    candidates_inside_finder_radius_and_vice_versa = candidates.filter(
        last_location__distance_lte=(
            finder_location,
            D(km=min(finder.prefered_radius, F('friendly_rate'))))
        ).distance(finder_location).order_by('distance')[:limit]

    serializer = FuckFinderUserListSerializer(candidates_inside_finder_radius_and_vice_versa, many=True)

    return JSONResponse(serializer.data)

