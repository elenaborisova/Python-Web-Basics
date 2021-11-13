from django.core.exceptions import ValidationError
from django.test import TestCase

from testing.models import Profile


class ProfileModelTests(TestCase):
    def test_createProfile_whenValidEgn_shouldCreate(self):
        name = 'Elena'
        age = 24
        egn = '1234567890'
        profile = Profile(name=name, age=age, egn=egn)

        profile.full_clean()
        profile.save()

    def test_createProfile_whenInvalidEgn_shouldRaise(self):
        name = 'Elena'
        age = 24
        egn = '12345678a0'

        with self.assertRaises(ValidationError) as context:
            profile = Profile(name=name, age=age, egn=egn)
            profile.full_clean()
            profile.save()

        self.assertIsNotNone(context.exception)

