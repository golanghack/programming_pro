from django.db import models

class Post(models.Model):
    # VARCHAR in BD
    title: str = models.CharField(max_length=300)
    # VARCHAR in DB
    slug: str = models.SlugField(max_length=300)
    # TEXT in DB
    body = models.TextField()

    def __str__(self):
        return self.title
