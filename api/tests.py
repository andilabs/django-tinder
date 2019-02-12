from django.core.management import call_command
from django.test import TestCase

from api.models import DjTinderUser


class TestGenerateRandomUsersCommand(TestCase):

    def test_correct_number_of_users_is_generated(self):
        call_command('generate_random_users', '100')
        self.assertEqual(DjTinderUser.objects.count(), 100)
