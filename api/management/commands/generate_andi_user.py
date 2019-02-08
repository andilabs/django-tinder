from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point

from api.models import DjTinderUser


class Command(BaseCommand):
    help = 'generate andi user'

    def handle(self, *args, **options):
        DjTinderUser.objects.create(
            nickname='andi',
            age=26,
            sex='M',
            preferred_sex='F',
            preferred_age_min=21,
            preferred_age_max=29,
            last_location=Point(float(52.228625), float(21.001952)),
            preferred_radius=25
        )
