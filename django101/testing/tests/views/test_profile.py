from django.test import TestCase, Client
from django.urls import reverse

from testing.models import Profile


class PersonViewsTests(TestCase):
    def setUp(self):
        self.test_client = Client()

    def test_getIndex_whenNoProfiles_shouldRenderCorrectTemplateWithNoProfiles(self):
        response = self.test_client.get(reverse('profiles'))
        self.assertTemplateUsed(response, 'testing/index.html')

        profiles = response.context['profiles']
        self.assertEqual(0, len(profiles))

        form = response.context['form']
        self.assertIsNotNone(form)

    def test_getIndex_whenTwoProfiles_shouldRenderCorrectTemplateWithTwoProfiles(self):
        profiles = (
            Profile(name='Elena', age=24, egn='1234567890'),
            Profile(name='Maria', age=22, egn='1234567890'),
        )
        [profile.save() for profile in profiles]

        response = self.test_client.get(reverse('profiles'))
        self.assertTemplateUsed(response, 'testing/index.html')

        profiles = response.context['profiles']
        self.assertEqual(2, len(profiles))

        form = response.context['form']
        self.assertIsNotNone(form)

    def test_postIndex_whenValidEgn_shouldRedirectToIndex(self):
        name = 'Elena'
        age = 24
        egn = '1234567890'
        data = {
            'name': name,
            'age': age,
            'egn': egn,
        }

        response = self.test_client.post(reverse('profiles'), data=data)

        self.assertRedirects(response, reverse('profiles'))

    def test_postIndex_whenEgnContainsLetters_shouldRenderIndexAndContainErrors(self):
        name = 'Elena'
        age = 24
        egn = '12345678a0'
        data = {
            'name': name,
            'age': age,
            'egn': egn,
        }

        response = self.test_client.post(reverse('profiles'), data=data)

        self.assertTemplateUsed(response, 'testing/index.html')
        profiles = response.context['profiles']
        self.assertEqual(0, len(profiles))

        form = response.context['form']
        self.assertIsNotNone(form.errors['egn'])
