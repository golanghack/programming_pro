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

    
class Course(models.Model):
    """-> model course for education cms platform"""

    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='courses', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField(default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created',]

    def __str__(self):
        return self.title 
