from django.apps import AppConfig
from django.db.models.signals import post_migrate


class AssociationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'association'

    def ready(self):
        from .signals import create_initial_sectors, create_initial_roles

        # Signal to create basic sectors
        post_migrate.connect(create_initial_sectors, sender=self)
        # Signal to create authorization groups
        post_migrate.connect(create_initial_roles, sender=self)
