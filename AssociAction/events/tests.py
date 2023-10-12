from django.test import TestCase, Client
from django.urls import reverse
from datetime import date

from .models import Association, AssociationEvent, Event
from authentication.models import CustomUser


class AssociationEventsViewTest(TestCase):
    def setUp(self):
        self.association = Association.objects.create(
            associationname="Association Test",
            acronym="ATest",
            phone_number="1234567890",
            email="test@example.com",
            description="Description de l'association de test",
        )
        event1_date = date(2023, 10, 10)
        event2_date = date(2028, 11, 10)
        self.event1 = Event.objects.create(
            event_name='event1',
            date=event1_date,
            description='good_event',
        )
        self.event2 = Event.objects.create(
            event_name='event2',
            date=event2_date,
            description='really_good_event',
        )
        AssociationEvent.objects.create(
            association=self.association,
            event=self.event1
        )
        AssociationEvent.objects.create(
            association=self.association,
            event=self.event2
        )
        self.url = reverse('all_asso_event', args=[self.association.id])

    def test_association_events_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['association'].associationname,
            "Association Test",
        )
        sorted_events = sorted(
            response.context['association_events'],
            key=lambda x: x.event.date,
        )

        self.assertQuerysetEqual(
            sorted_events,
            AssociationEvent.objects.all(),
            transform=lambda x: x
        )

    def tearDown(self):
        AssociationEvent.objects.all().delete()
        Event.objects.all().delete()
        Association.objects.all().delete()


class EventDetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = CustomUser.objects.create(
            first_name='EDProfile',
            last_name='Tester',
            username='PTester',
            email='edtest@test.fr',
            password='testpassword123',
        )
        self.association = Association.objects.create(
            associationname="Association Test",
            acronym="ATest",
            phone_number="1234567890",
            email="test@example.com",
            description="Description de l'association de test",
        )

        event_date = date(2023, 11, 11)
        self.event = Event.objects.create(
            event_name="Event Test",
            date=event_date,
            description="Description de l'événement de test",
        )
        AssociationEvent.objects.create(
            event=self.event,
            association=self.association
        )
        self.url = reverse(
            'event_detail',
            args=[self.association.id, self.event.id]
        )
        self.client.force_login(self.user)

    def test_event_detail_view(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(
            response.context['association'].associationname,
            "Association Test",
        )
        self.assertEqual(response.context['event'].event_name, "Event Test")

    def tearDown(self):
        AssociationEvent.objects.all().delete()
        Event.objects.all().delete()
        Association.objects.all().delete()
        CustomUser.objects.all().delete()
