from django.db import models
from django.utils import timezone

class Post(models.Model):
    # VARCHAR in BD
    title: str = models.CharField(max_length=300)
    # VARCHAR in DB
    slug: str = models.SlugField(max_length=300)
    # TEXT in DB
    body = models.TextField()
    # DATETIME in DB
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']),]

    def __str__(self) -> str:
        return self.title
