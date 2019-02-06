from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.db.models import F
from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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


# version GEO FIRST with pagination
@api_view(['GET', ])
def fetch_djtinder_proposals_for(request, nick_of_finder, current_latitude, current_longitiude):

    finder = get_object_or_404(DjTinderUser, nickname=nick_of_finder)
    finder_location = Point(float(current_longitiude), float(current_latitude))

    candidates = DjTinderUser.objects.filter(
        last_location__distance_lte=(
            finder_location,
            D(km=min(finder.prefered_radius, F('prefered_radius'))))
        ).distance(finder_location).order_by('distance')

    if finder.prefered_sex == finder.sex:
        # deal with homosexual
        candidates_inside_finder_radius_and_vice_versa = candidates.filter(
            prefered_sex=finder.sex,
            sex=finder.prefered_sex,
            age__range=(finder.prefered_age_min, finder.prefered_age_max),
            prefered_age_min__lte=finder.age,
            prefered_age_max__gte=finder.age,
        ).exclude(nickname=finder.nickname)
    else:
        # deal with heterosexual:
        candidates_inside_finder_radius_and_vice_versa = candidates.filter(
            sex=finder.hetero_desires(),
            age__range=(finder.prefered_age_min, finder.prefered_age_max),
            prefered_age_min__lte=finder.age,
            prefered_age_max__gte=finder.age,
        ).exclude(sex=F('prefered_sex')).exclude(nickname=finder.nickname)

    paginator = Paginator(candidates_inside_finder_radius_and_vice_versa, 20)

    page = request.QUERY_PARAMS.get('page')

    try:
        result = paginator.page(page)
    except PageNotAnInteger:
        result = paginator.page(1)
    except EmptyPage:
        result = paginator.page(paginator.num_pages)

    serializer_context = {'request': request}
    serializer = DjTinderUserListSerializer(
        result, context=serializer_context)
    return Response(serializer.data)
