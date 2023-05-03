from django.db import models


class PublishedManager(models.Manager):
    """Custom manager."""

    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

