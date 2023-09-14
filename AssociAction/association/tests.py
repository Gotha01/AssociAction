from django.test import TestCase
from django.urls import reverse
from .models import Association
from django.core.files.uploadedfile import SimpleUploadedFile

class AssociationViewsTestCase(TestCase):
    
    def setUp(self):
        # Create a fictitious image file for testing
        image_data = b'\x89PNG\r\n...your_binary_image_data_here...'
        self.image = SimpleUploadedFile("example.png", image_data, content_type="image/png")

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
    
    def test_association_detail_view(self):
        associations = Association.objects.all()

        for association in associations:
            url = reverse('association_detail', args=[association.id])
            
            response = self.client.get(url)
            
            self.assertEqual(response.status_code, 200)

            self.assertTemplateUsed(response, 'association/association_detail.html')
            
            self.assertEqual(response.context['association'], association)