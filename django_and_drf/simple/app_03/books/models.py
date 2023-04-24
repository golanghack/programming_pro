from django.db import models

class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Book(models.Model):
    
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(to=Author)

