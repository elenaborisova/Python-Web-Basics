from unittest import TestCase

from django.core.exceptions import ValidationError

from testing.validators import contains_only_digits_validator


class EgnValidatorTests(TestCase):
    def test_validate_whenOnlyDigits_shouldDoNothing(self):
        contains_only_digits_validator('123')
        # self.assertTrue(True)

    def test_validate_whenEmpty_shouldDoNothing(self):
        contains_only_digits_validator('')

    def test_validate_whenContainsALetter_shouldRaise(self):
        with self.assertRaises(ValidationError) as context:
            contains_only_digits_validator('a')

        self.assertIsNotNone(context.exception)
