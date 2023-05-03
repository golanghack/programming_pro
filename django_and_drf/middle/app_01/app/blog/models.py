from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from managers.PublishManager import PublishedManager

class Post(models.Model):

    class Status(models.TextChoices):
        """Class status blog writing.
        
            option status -> Post.Status.choices
            repr -> Post.Status.labels
            row -> Post.Status.values
        """

        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    # VARCHAR in BD
    title: str = models.CharField(max_length=300)
    # VARCHAR in DB
    slug: str = models.SlugField(max_length=300)
    author: str = models.ForeignKey(User, 
                                    on_delete=models.CASCADE, 
                                    related_name='blog_posts')
    # TEXT in DB
    body = models.TextField()
    # DATETIME in DB
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=2, 
                                choices=Status.choices, 
                                default=Status.DRAFT)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [models.Index(fields=['-publish']),]

    def __str__(self) -> str:
        return self.title
