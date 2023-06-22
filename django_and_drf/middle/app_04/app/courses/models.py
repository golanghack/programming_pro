from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):
    """-> model Subject for education cms platform""" 

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title',]

    def __str__(self):
        return self.title

    