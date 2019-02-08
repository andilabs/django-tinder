from django.core.management.base import BaseCommand
from django.contrib.gis.geos import Point
import random
import uuid
import numpy as np
from api.models import DjTinderUser, hetero_desires


class Command(BaseCommand):
    help = 'generate 1M users for Warsaw with random ' \
           'sex, age, orientation, radius, location'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **options):
        count = options['count']

        warsaw__lat__min = 52.09
        warsaw__lat__max = 52.31
        warsaw__lng__min = 20.87
        warsaw__lng__max = 21.17

        for i in range(count):
            new_random_lat = random.uniform(warsaw__lat__min, warsaw__lat__max)
            new_random_lng = random.uniform(warsaw__lng__min, warsaw__lng__max)
            user_age = random.randrange(18, 55)
            user_delta_plus = random.choice([1, 2, 3, 5, 8, 13])
            user_delta_minus = random.choice([1, 2, 3, 5, 8, 13])
            user_sex = random.choice(['F', 'M'])
            sexual_orientation = ['hetero', 'homo']
            choosen_at_random_sexual_orientation = np.random.choice(
                sexual_orientation, p=[0.95, 0.05])

            if choosen_at_random_sexual_orientation == 'homo':
                user_preferred_sex = user_sex
            else:
                user_preferred_sex = hetero_desires(user_sex)

            DjTinderUser.objects.create(
                nickname=str(uuid.uuid4()),
                age=user_age,
                sex=user_sex,
                preferred_sex=user_preferred_sex,
                preferred_age_min=(user_age-user_delta_minus),
                preferred_age_max=(user_age+user_delta_plus),
                last_location=Point(float(new_random_lng),
                                    float(new_random_lat)),
                preferred_radius=random.choice([5, 10, 15, 20, 25, 30])
            )
