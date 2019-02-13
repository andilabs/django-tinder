from django.contrib.gis.geos import Point
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from rest_framework.test import APITestCase

from api.models import DjTinderUser


class TestGenerateRandomUsersCommand(TestCase):

    def test_correct_number_of_users_is_generated(self):
        call_command('generate_random_users', '100')
        self.assertEqual(DjTinderUser.objects.count(), 100)


class TestProposalsApiView(APITestCase):

    @classmethod
    def setUpTestData(cls):
        DjTinderUser.objects.create(
            nickname='test_user',
            age=30,
            sex='M',
            preferred_sex='F',
            preferred_age_min=25,
            preferred_age_max=35,
            last_location=Point(21.012223, 52.230357),
            preferred_radius=1
        )

        DjTinderUser.objects.create(
            nickname='a',
            age=30,
            sex='F',
            preferred_sex='M',
            preferred_age_min=25,
            preferred_age_max=35,
            last_location=Point(21.061133, 52.241402),
            preferred_radius=20
        )
        DjTinderUser.objects.create(
            nickname='b',
            age=32,
            sex='M',
            preferred_sex='M',
            preferred_age_min=25,
            preferred_age_max=35,
            last_location=Point(21.015003, 52.232786),
            preferred_radius=5
        )
        DjTinderUser.objects.create(
            nickname='c',
            age=34,
            sex='F',
            preferred_sex='M',
            preferred_age_min=25,
            preferred_age_max=35,
            last_location=Point(21.015003, 52.232786),
            preferred_radius=4
        )
        DjTinderUser.objects.create(
            nickname='d',
            age=31,
            sex='M',
            preferred_sex='M',
            preferred_age_min=25,
            preferred_age_max=35,
            last_location=Point(21.015003, 52.232786),
            preferred_radius=5
        )

    def test_get_proposals_for_hetero(self):
        response = self.client.get(
            reverse('api:djtinder_proposals', kwargs={
                'user_nick': 'test_user',
                'current_latitude': 52.236479,
                'current_longitude': 21.020547})
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['results']), 1)
        self.assertEqual(response.json()['results'][0]['nickname'], 'c')
        DjTinderUser.objects.filter(nickname='test_user').update(
            preferred_radius=10
        )
        response = self.client.get(
            reverse('api:djtinder_proposals', kwargs={
                'user_nick': 'test_user',
                'current_latitude': 52.236479,
                'current_longitude': 21.020547})
        )
        self.assertEqual(len(response.json()['results']), 2)
