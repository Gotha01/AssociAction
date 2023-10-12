from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth.hashers import make_password

from .forms import (
    RegistrationForm,
    LoginForm,
    UserImageUpdateForm,
    UserProfileUpdateForm,
    AddressUpdateForm,
)
from association.models import UserRoleAssociation, Association, Role


CustomUser = get_user_model()


def superuser_check(user):
    return user.is_superuser


class SuperuserCheckTestCase(TestCase):
    def test_superuser_check_super_user(self):
        # Create a superuser
        superuser = CustomUser.objects.create_superuser(
            first_name='Super',
            last_name='User',
            username='superuser',
            email='superuser@example.com',
            password='superpass',
        )
        self.assertTrue(superuser_check(superuser))

    def test_superuser_check_non_super_user(self):
        # Create an ordinary user
        user = CustomUser.objects.create_user(
            first_name='Ordinary',
            last_name='User',
            username='ordinaryuser',
            email='ordinaryuser@example.com',
            password='userpass',
        )
        # Check whether the function returns False for an ordinary user
        self.assertFalse(superuser_check(user))

    def tearDown(self):
        CustomUser.objects.all().delete


class RegisterViewTest(TestCase):
    def setUp(self):
        self.url = reverse('register')

    def test_register_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('register_form' in response.context)
        register_form = response.context['register_form']
        self.assertIsInstance(register_form, RegistrationForm)

    def test_register_view_post(self):
        post_data = {
            'last_name': 'Lastname',
            'first_name': 'Firstname',
            'username': 'username',
            'email': 'last@name.fr',
            'password': 'Superpassword1',
            'password_confirmation': 'Superpassword1',
        }
        response = self.client.post(self.url, data=post_data)
        self.assertEqual(response.status_code, 302)
        user_created = CustomUser.objects.filter(username='username').exists()
        self.assertTrue(user_created)


class LoginViewTest(TestCase):
    def setUp(self):
        self.url = reverse('login')
        self.user = CustomUser.objects.create_user(
            first_name='User',
            last_name='Test',
            username='testuser1',
            email='mail@mail.test',
            password='Superpassword1',
        )

    def test_login_view_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

        self.assertTrue('login_form' in response.context)
        register_form = response.context['login_form']
        self.assertIsInstance(register_form, LoginForm)

    def test_login_view_post_valid_credentials(self):
        post_data = {
            'username': 'mail@mail.test',
            'password': 'Superpassword1',
        }
        response = self.client.post(self.url, data=post_data)
        self.assertEqual(response.status_code, 302)

    def test_login_view_post_invalid_credentials(self):
        post_false_data = {
            'username': 'testuser@fez.ref',
            'password': 'MotDePasseIncorrect',
        }
        response = self.client.post(self.url, data=post_false_data)
        self.assertEqual(response.status_code, 200)
        message = response.context['message']
        self.assertEqual(message, 'identifiants invalides')

    def tearDown(self):
        CustomUser.objects.all().delete


class ProfileViewTest(TestCase):
    def setUp(self):
        image_data = b'\x89PNG\r\n...your_binary_image_data_here...'
        self.image = SimpleUploadedFile(
            "example.png",
            image_data,
            content_type="image/png"
        )
        self.user1 = CustomUser.objects.create(
            first_name='Tester',
            last_name='Tester',
            username='testuser2',
            email='test1@example.com',
            password='password123!'
        )
        self.user2 = CustomUser.objects.create(
            first_name='Tester',
            last_name='Tester',
            username='testuser3',
            email='test2@example.com',
            password='password123!'
        )
        self.association_for_role = Association.objects.create(
            associationname="Association Test 1",
            acronym="ATest1",
            phone_number="1234567890",
            email="testasso@example.com",
            description="Description de l'association de test 1",
            logo=self.image,
        )
        self.role = Role.objects.get(id=1)
        self.user1_roles = UserRoleAssociation.objects.create(
            user=self.user1,
            association=self.association_for_role,
            role=self.role
        )

    def test_profile_view_authenticated_director_user(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'], self.user1)

    def test_profile_view_authenticated_user(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['user'], self.user2)

    def tearDown(self):
        CustomUser.objects.all().delete()
        Association.objects.all().delete()
        UserRoleAssociation.objects.all().delete()


class UpdateProfileViewTest(TestCase):
    def setUp(self):
        self.url = reverse('update_profile')
        self.user = CustomUser.objects.create(
            first_name='Profile',
            last_name='Tester',
            username='PTester',
            email='ptest@test.fr',
            password=make_password('testpassword123'),
        )
        self.client = Client()

    def test_update_profile_view(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('user_form', response.context)
        self.assertIn('img_form', response.context)
        self.assertIn('address_form', response.context)
        self.assertIsInstance(
            response.context['user_form'],
            UserProfileUpdateForm,
        )
        self.assertIsInstance(
            response.context['img_form'],
            UserImageUpdateForm,
        )
        self.assertIsInstance(
            response.context['address_form'],
            AddressUpdateForm,
        )

    def tearDown(self):
        CustomUser.objects.all().delete()
