from django.apps import AppConfig


class RealCdConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'real_cd'
    def ready(self):
        import real_cd.signals