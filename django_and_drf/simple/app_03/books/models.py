from django.db import models

class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(to=Author)

    def __str__(self):
        return self.title


class Event(models.Model):

    title = models.CharField(max_length=60)
    seo_title = models.CharField(max_length=59)
    seo_description = models.CharField(max_length=160)
    abstract = models.CharField(max_length=160)
    body = models.TextField(default='')
    duration = models.IntegerField(default=0)
    slug = models.SlugField(max_length=20)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.IntegerField()
    location = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'
