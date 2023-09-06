from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.dispatch import receiver


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'authentication'

    def ready(self):
            from .models import Role
            from .signals import create_initial_roles

            post_migrate.connect(create_initial_roles, sender=self)