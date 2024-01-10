from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.api.users'

    """
        The function imports the signals module from the apps.api.users package.
    """
    def ready(self):
        
        import apps.api.users.signals
