from django.db import models

class Book(models):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title