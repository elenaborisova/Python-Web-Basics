from django.test import TestCase

from testing.forms.profile import ProfileForm


class ProfileFormTests(TestCase):
    def test_saveProfileForm_whenValidEgn_shouldBeValid(self):
        name = 'Elena'
        age = 24
        egn = '1234567890'
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn,
        })

        self.assertTrue(form.is_valid())

    def test_saveProfileForm_whenEgnContainsLetter_shouldBeInvalid(self):
        name = 'Elena'
        age = 24
        egn = '12345678a0'
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn,
        })

        self.assertFalse(form.is_valid())

    def test_saveProfileForm_whenEgnContainsLessDigits_shouldBeInvalid(self):
        name = 'Elena'
        age = 24
        egn = '123456789'
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn,
        })

        self.assertFalse(form.is_valid())

    def test_saveProfileForm_whenEgnContainsMoreDigits_shouldBeInvalid(self):
        name = 'Elena'
        age = 24
        egn = '12345678900'
        form = ProfileForm(data={
            'name': name,
            'age': age,
            'egn': egn,
        })

        self.assertFalse(form.is_valid())
