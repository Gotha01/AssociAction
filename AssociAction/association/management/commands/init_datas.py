from django.core.management.base import BaseCommand

from association.models import (
    Sector,
    Association,
    AssociationAddress,
    AssociationSector
)
from authentication.models import CustomUser, Address, UserAddress


class Command(BaseCommand):
    help = 'Initialisez des données dans votre application.'

    def handle(self, *args, **kwargs):
        # Retrieve sectors
        sector1 = Sector.objects.get(sectorname='Sports')
        sector2 = Sector.objects.get(sectorname='Agriculture')
        sector3 = Sector.objects.get(sectorname='Culture (Arts)')
        sector4 = Sector.objects.get(sectorname='Aide Sociale')
        sector5 = Sector.objects.get(sectorname='Environnement')

        # Create associations
        association1, _ = Association.objects.get_or_create(
            associationname='Association sportive',
            acronym='A.S.',
            phone_number='1234567890',
            email='as-1@example.com',
            description='Association Sportive de Paris',
            logo='for_test_sport_paris.jpg',
            siret_number=45645645645645,
        )
        association2, _ = Association.objects.get_or_create(
            associationname='Coopérative Agricole',
            acronym='C.A.',
            phone_number='9876543210',
            email='ca-2@example.com',
            description='Coopérative agricole de Dussac'
        )
        association3, _ = Association.objects.get_or_create(
            associationname='Association Culturelle',
            acronym='A.C.',
            phone_number='5555555555',
            email='ac-3@example.com',
            description='Association Culturelle de Lyon'
        )
        association4, _ = Association.objects.get_or_create(
            associationname='Association Humanitaire',
            acronym='A.H.',
            phone_number='4444444444',
            email='ah-4@example.com',
            description='Association Humanitaire de Marseille'
        )
        association5, _ = Association.objects.get_or_create(
            associationname='Association Environnementale',
            acronym='A.E.',
            phone_number='3333333333',
            email='ae-5@example.com',
            description='Association Environnementale de Bordeaux'
        )

        # Create Addresses
        address1, _ = Address.objects.get_or_create(
            postalcode=75001,
            cityname='Paris',
            addresslineone='7 Rue de Rivoli'
        )
        address2, _ = Address.objects.get_or_create(
            postalcode=24270,
            cityname='Dussac',
            addresslineone='4 Route du châtaigner'
        )
        address3, _ = Address.objects.get_or_create(
            postalcode=69000,
            cityname='Lyon',
            addresslineone='10 Place Bellecour'
        )
        address4, _ = Address.objects.get_or_create(
            postalcode=13000,
            cityname='Marseille',
            addresslineone='15 Rue de la République'
        )
        address5, _ = Address.objects.get_or_create(
            postalcode=33000,
            cityname='Bordeaux',
            addresslineone='20 Rue Sainte-Catherine'
        )
        address6, _ = Address.objects.get_or_create(
            postalcode=17000,
            cityname='La Rochelle',
            addresslineone='1 Rue du Collège'
        )
        address7, _ = Address.objects.get_or_create(
            postalcode=24270,
            cityname='Paris',
            addresslineone='10 Rue Gassendi'
        )
        address8, _ = Address.objects.get_or_create(
            postalcode=24270,
            cityname='Bordeaux',
            addresslineone='8 Rue Lebrun'
        )

        # créer des utilisateurs
        lambda_user, created1 = CustomUser.objects.get_or_create(
            first_name='Julien',
            last_name='Deschamps',
            username='Juju',
            email='ju-dech@gmail.com',
            phone_number='0606606066',
        )
        if created1:
            lambda_user.set_password('ReallygoodPassword1')
            lambda_user.save()

        admin_assoc_user, created2 = CustomUser.objects.get_or_create(
            first_name='Jean',
            last_name='Plisson',
            username='JP75',
            email='jean-pli@hotmail.fr',
            phone_number='0789898989',
        )
        if created2:
            admin_assoc_user.set_password('ReallygoodPassword2')
            admin_assoc_user.save()

        director_user, created3 = CustomUser.objects.get_or_create(
            first_name='Chloé',
            last_name='Villena',
            username='Clo33',
            email='cloclo33@orange.fr',
            phone_number='0606606066',
        )
        if created3:
            director_user.set_password('ReallygoodPassword3')
            director_user.save()

        # Create association addresses
        rel_asso1_address1, _ = AssociationAddress.objects.get_or_create(
            association=association1,
            address=address1
        )
        rel_asso2_address2, _ = AssociationAddress.objects.get_or_create(
            association=association2,
            address=address2
        )
        rel_asso3_address3, _ = AssociationAddress.objects.get_or_create(
            association=association3,
            address=address3
        )
        rel_asso4_address4, _ = AssociationAddress.objects.get_or_create(
            association=association4,
            address=address4
        )
        rel_asso5_address5, _ = AssociationAddress.objects.get_or_create(
            association=association5,
            address=address5
        )

        # Create user addresses
        rel_user1_address3, _ = UserAddress.objects.get_or_create(
            user=lambda_user,
            address=address6
        )
        rel_user2_address4, _ = UserAddress.objects.get_or_create(
            user=admin_assoc_user,
            address=address7
        )
        rel_user3_address5, _ = UserAddress.objects.get_or_create(
            user=director_user,
            address=address8
        )

        # Créez des relations entre des associations et des secteurs
        association_sector1, _ = AssociationSector.objects.get_or_create(
            association=association1,
            sector=sector1
        )
        association_sector2, _ = AssociationSector.objects.get_or_create(
            association=association2,
            sector=sector2
        )
        association_sector3, _ = AssociationSector.objects.get_or_create(
            association=association3,
            sector=sector3
        )
        association_sector4, _ = AssociationSector.objects.get_or_create(
            association=association4,
            sector=sector4
        )
        association_sector5, _ = AssociationSector.objects.get_or_create(
            association=association5,
            sector=sector5
        )

        self.stdout.write(self.style.SUCCESS('Data successfully initialized.'))
