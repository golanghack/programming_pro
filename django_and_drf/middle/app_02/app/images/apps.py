from django.apps import AppConfig


class ImagesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "images"

    # signals 
    def ready(self):
        import images.signal
