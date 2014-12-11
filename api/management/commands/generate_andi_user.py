from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point

from api.models import FuckFinderUser


class Command(BaseCommand):
    help = 'generate andi user'

    def handle(self, *args, **options):
        FuckFinderUser.objects.create(
            nickname='andi',
            age=26,
            sex='M',
            prefered_sex='F',
            prefered_age_min=21,
            prefered_age_max=29,
            last_location=Point(float(52.228625), float(21.001952)),
            prefered_radius=25
        )
