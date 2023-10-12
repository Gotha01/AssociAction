from django.test import TestCase
from django.urls import reverse
from django.http import HttpRequest
from django.core.files.uploadedfile import SimpleUploadedFile

from association.models import Association, UserRoleAssociation, Role
from authentication.models import CustomUser


class OtherViewTests(TestCase):
    def test_help_center_view(self):
        # Test the help center view
        response = self.client.get(reverse('help'))
        self.assertEqual(response.status_code, 200)

    def test_legals_view(self):
        # Test the legals view
        response = self.client.get(reverse('legals'))
        self.assertEqual(response.status_code, 200)


class HomeViewTest(TestCase):
    def setUp(self):
        self.url = reverse('home')

    def test_home_view_post(self):
        request = HttpRequest()
        request.method = 'POST'

        datas = [
            {
                'quoi': 'Sports',
                'ou': '',
            },
            {
                'quoi': '',
                'ou': 'Marseille',
            },
            {
                'quoi': '',
                'ou': '',
            }
        ]
        for data in datas:
            request.POST = data
            response = self.client.post(self.url, data)

            self.assertEqual(response.status_code, 200)
            self.assertTrue('associations' in response.context)
            associations = response.context['associations']
            self.assertTrue(
                all(isinstance(assoc, Association) for assoc in associations)
            )

    def test_home_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


class ContactViewTest(TestCase):
    def setUp(self):
        self.url = reverse('contact')
        self.user = CustomUser.objects.create_user(
            first_name='Testy',
            last_name='User',
            username='testyuser',
            email='testyuser@example.com',
            password='userpass',
        )
        self.role = Role.objects.get(id=1)
        image_data = b'\x89PNG\r\n...your_binary_image_data_here...'
        self.image = SimpleUploadedFile(
            "example.png",
            image_data,
            content_type="image/png"
        )
        self.association = Association.objects.create(
            associationname="Association Test 1",
            acronym="ATest1",
            phone_number="1234567890",
            email="test1@example.com",
            description="Description de l'association de test 1",
            logo=self.image,
        )
        self.user_role = UserRoleAssociation.objects.create(
            user=self.user, role=self.role, association=self.association
        )

    def test_contact_view(self):
        # Test the contact view
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_contact_director_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
