from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
import random
import uuid
import numpy as np
from api.models import FuckFinderUser, hetero_desires


class Command(BaseCommand):
    help = 'generate 1M users for Warsaw with random sex, age, orientation, radius, location'

    def handle(self, *args, **options):
        warsaw__lat__min = 52.09
        warsaw__lat__max = 52.31
        warsaw__lng__min = 20.87
        warsaw__lng__max = 21.17

        for i in xrange(10**6):
            new_random_lat = random.uniform(warsaw__lat__min, warsaw__lat__max)
            new_random_lng = random.uniform(warsaw__lng__min, warsaw__lng__max)
            user_age = random.randrange(18, 55)
            user_delta_plus = random.choice([1, 2, 3, 5, 8, 13])
            user_delta_minus = random.choice([1, 2, 3, 5, 8, 13])
            user_sex = random.choice(['F', 'M'])
            sexual_orientation = ['hetero', 'homo']
            choosen_at_random_sexual_orientation = np.random.choice(sexual_orientation, p=[0.95, 0.05])

            if choosen_at_random_sexual_orientation == 'homo':
                user_prefered_sex = user_sex
            else:
                user_prefered_sex = hetero_desires(user_sex)

            FuckFinderUser.objects.create(
                nickname=str(uuid.uuid4()),
                age=user_age,
                sex=user_sex,
                prefered_sex=user_prefered_sex,
                prefered_age_min=(user_age-user_delta_minus),
                prefered_age_max=(user_age+user_delta_plus),
                last_location=Point(float(new_random_lng), float(new_random_lat)),
                prefered_radius=random.choice([5, 10, 15, 20, 25, 30])
            )