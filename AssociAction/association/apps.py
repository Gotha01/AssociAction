from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class AssociationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'association'

    def ready(self):
            from .models import Sector
            from .signals import create_initial_sectors

            post_migrate.connect(create_initial_sectors, sender=self)