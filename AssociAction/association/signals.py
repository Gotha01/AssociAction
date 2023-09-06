from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Sector

@receiver(post_migrate)
def create_initial_sectors(sender, **kwargs):
    if sender.name == 'association':
        sectors = [
        {"sectorname": "Culture (Arts)", "description": "Promotion des arts visuels, de la musique, de la danse, etc."},
        {"sectorname": "Sciences et technologie", "description": "Innovations, recherches scientifiques, etc."},
        {"sectorname": "Éducation", "description": "Éducation générale, éducation aux médias, etc."},
        {"sectorname": "Santé", "description": "Vaccinations, accès aux soins médicaux, santé publique, prévention des maladies"},
        {"sectorname": "Sports", "description": "Tennis, football, basket, handball, rugby, etc."},
        {"sectorname": "Environnement", "description": "Développement durable, protection de l'environnement, etc."},
        {"sectorname": "Vie sociale", "description": "Personnes âgées, jeunesse et loisirs, découverte sociale"},
        {"sectorname": "Aide Sociale", "description": "Habitat, Alimentation, Handicap, Humanitaire"},
        {"sectorname": "Patrimoine", "description": "Préservation du patrimoine culturel, historique et architectural."},
        {"sectorname": "Animaux", "description": "Protection et bien-être des animaux."},
        {"sectorname": "Relation internationale", "description": "Jumelage, diplomatie, coopération internationale"},
        {"sectorname": "Religions", "description": "Activités religieuses et interreligieuses"},
        {"sectorname": "Politique", "description": "Engagement civique, sensibilisation politique"},
        {"sectorname": "Économique", "description": "Activités économiques, développement économique"},
        {"sectorname": "Droit", "description": "Droits des consommateurs, protection de l'enfance, etc."},
        {"sectorname": "Énergie", "description": "Énergie renouvelable, gestion de l'énergie, etc."},
        {"sectorname": "Transport", "description": "Mobilité urbaine, transport public, etc."},
        {"sectorname": "Agriculture", "description": "Agriculture durable, coopératives, sécurité alimentaire, etc."},
        {"sectorname": "Tourisme", "description": "Promotion du tourisme local, tourisme durable, etc."},
        {"sectorname": "Média", "description": "Médias numériques, journalisme indépendant, etc."},
    ]
        for sector_data in sectors:
            Sector.objects.get_or_create(**sector_data)