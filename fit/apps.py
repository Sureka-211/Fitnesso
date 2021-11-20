from django.apps import AppConfig


class FitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fit'

class ImageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'image'


