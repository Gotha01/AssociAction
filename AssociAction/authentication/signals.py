from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Role

@receiver(post_migrate)
def create_initial_roles(sender, **kwargs):
    if sender.name == 'association':
        roles = [
            {"rolename": "Lambda", "rolepermission": 1, "description": "Rôle de base pour les utilisateurs"},
            {"rolename": "Adherent", "rolepermission": 2, "description": "Rôle pour les membres adhérents"},
            {"rolename": "AdminAssociation", "rolepermission": 3, "description": "Rôle administratif pour les associations"},
            {"rolename": "DirecteurAssociation", "rolepermission": 4, "description": "Rôle de directeur pour les associations"},
        ]
        for role_data in roles:
            Role.objects.get_or_create(**role_data)