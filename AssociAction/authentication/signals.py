from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Role

@receiver(post_migrate)
def create_initial_roles(sender, **kwargs):
    if sender.name == 'association':
        roles = [
            {"rolename": "Lambda", "rolepermission": 1},
            {"rolename": "Adherent", "rolepermission": 2},
            {"rolename": "AdminAssociation", "rolepermission": 3},
            {"rolename": "DirecteurAssociation", "rolepermission": 4},
        ]
        for role_data in roles:
            Role.objects.get_or_create(**role_data)