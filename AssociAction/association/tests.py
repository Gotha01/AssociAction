from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.core.files.uploadedfile import SimpleUploadedFile

from authentication.models import CustomUser
from .models import Association, Sector
from authentication.forms import AddressUpdateForm
from association import views as vw


class AssociationViewsTestCase(TestCase):

    def setUp(self):
        # Create a fictitious image file for testing
        image_data = b'\x89PNG\r\n...your_binary_image_data_here...'
        self.image = SimpleUploadedFile(
            "example.png",
            image_data,
            content_type="image/png"
        )

        # Create fictitious associations for tests
        test_associations = [
            {
                'associationname': "Association Test 1",
                'acronym': "ATest1",
                'phone_number': "1234567890",
                'email': "test1@example.com",
                'description': "Description de l'association de test 1",
                'logo': self.image,
            },
            {
                'associationname': "Association Test 2",
                'acronym': "ATest2",
                'phone_number': "1234567890",
                'email': "test2@example.com",
                'description': "Description de l'association de test 2",
                'logo': self.image,
            },
            {
                'associationname': "Association Test 3",
                'acronym': "ATest3",
                'phone_number': "1234567890",
                'email': "test3@example.com",
                'description': "Description de l'association de test 3",
                'logo': self.image,
            },
            {
                'associationname': "Association Test 4",
                'acronym': "ATest4",
                'phone_number': "1234567890",
                'email': "test4@example.com",
                'description': "Description de l'association de test 4",
                'logo': self.image,
            },
        ]
        for association_data in test_associations:
            Association.objects.create(**association_data)

    def test_association_detail_view_not_found(self):
        url = reverse('association_detail', args=[999])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 404)

    def test_association_detail_view(self):
        associations = Association.objects.all()

        for association in associations:
            url = reverse('association_detail', args=[association.id])

            response = self.client.get(url)

            self.assertEqual(response.status_code, 200)

            self.assertTemplateUsed(
                response,
                'association/association_detail.html'
            )

            self.assertEqual(response.context['association'], association)

    def tearDown(self):
        Association.objects.all().delete()


class TestUrls(TestCase):
    def test_association_detail_is_resolved(self):
        url = reverse('association_detail', args=[1])
        self.assertEquals(resolve(url).func, vw.association_detail)

    def test_association_list_is_resolved(self):
        url = reverse('association_list')
        self.assertEquals(resolve(url).func, vw.association_list)

    def test_create_association_is_resolved(self):
        url = reverse('create_association')
        self.assertEquals(resolve(url).func, vw.create_association)

    def test_update_association_is_resolved(self):
        association_id = 1
        url = reverse('update_association', args=[association_id])
        self.assertEquals(resolve(url).func, vw.update_association)

    def test_association_address_is_resolved(self):
        association_id = 1
        url = reverse('association_address', args=[association_id])
        self.assertEquals(resolve(url).func, vw.association_address)


class CreateAssociationViewTest(TestCase):
    def setUp(self):
        self.url = reverse('create_association')
        self.superuser = CustomUser.objects.create_superuser(
            first_name='Super',
            last_name='USer',
            username='SuperUser',
            email='super@user.su',
            password='PerfectPassword123',
        )
        self.client = Client()
        self.sector = Sector.objects.create(sectorname='Example Sector')

    def test_create_association_page(self):
        self.client.force_login(self.superuser)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context)

    def test_create_association_page_post(self):
        self.client.force_login(self.superuser)
        form_data = {
            'associationname': 'New Association',
            'sector': self.sector.id,
            'email': 'newassociation@example.com',
            'acronym': 'NA',
            'phone_number': '1234567890',
            'description': 'A new association',
            'logo': 'path/to/logo.png',
        }
        response = self.client.post(
            self.url,
            data=form_data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(
            Association.objects.filter(
                associationname='New Association'
            ).exists()
        )

    def tearDown(self):
        CustomUser.objects.all().delete()
        Sector.objects.all().delete()


class AssociationAddressViewTest(TestCase):
    def setUp(self):
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
        self.url = reverse('association_address', args=[self.association.id])
        self.client = Client()

    def test_create_address_association_page(self):
        response = self.client.get(self.url, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_create_address_association_page_post(self):
        form_data = {
            'postalcode': 12345,
            'cityname': 'Example City',
            'addresslineone': '123 Main St',
            'addresslinetwo': 'Apt 4B',
        }
        response = self.client.post(self.url, data=form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        form = AddressUpdateForm(form_data)
        self.assertTrue(form.is_valid())

        self.assertEqual(form.cleaned_data['postalcode'], 12345)
        self.assertEqual(form.cleaned_data['cityname'], 'Example City')

    def tearDown(self):
        Association.objects.all().delete()


class updateAssociationViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create(
            first_name='Upasvi',
            last_name='Iewtest',
            username="Uavt",
            email='uavt@test.com',
            password='1passwordReallyStrong',
        )
        self.client.force_login(self.user)
        self.association = Association.objects.create(
            associationname="Association Test",
            acronym="ATest",
            phone_number="1234567890",
            email="test@example.com",
            description="Description de l'association de test",
        )
        self.url = reverse('update_association', args=[self.association.id])

    def test_get_update_association_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        labels_to_check = [
            "Nom de l&#x27;association",
            "Acronyme",
            "Numéro de téléphone",
            "Adresse e-mail",
            "Description",
            "Numéro de SIRET",
        ]

        for label in labels_to_check:
            self.assertContains(response, label)

    def test_update_association_valid_data(self):
        data = {
            'associationna': 'Nouveau nom',
            'Acronyme': 'NewAcronym',
        }
        response = self.client.post(self.url, data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nom de l&#x27;association')

    def test_delete_logo(self):
        data = {'delete_logo': 'delete_logo'}
        response = self.client.post(self.url, data, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_submit_logo_valid_data(self):
        data = {'submit_logo': 'submit_logo'}
        response = self.client.post(self.url, data, follow=True)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        CustomUser.objects.all().delete()
        Association.objects.all().delete()
