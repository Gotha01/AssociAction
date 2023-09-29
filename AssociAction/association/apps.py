from django.apps import AppConfig
from django.db.models.signals import post_migrate, post_save


class AssociationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'association'

    def ready(self):
        from .models import Association
        from .signals import create_initial_sectors, create_initial_roles

        # Signal to create basic sectors
        post_migrate.connect(create_initial_sectors, sender=self)
        # Signal to create authorization groups
        post_migrate.connect(create_initial_roles, sender=Association)