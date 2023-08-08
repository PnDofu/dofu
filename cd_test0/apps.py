from django.apps import AppConfig

class CdTest0Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cd_test0'
    def ready(self):
        import cd_test0.signals