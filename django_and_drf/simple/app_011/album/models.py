from django.db import models

class Singer(models.Model):
    name = models.CharField(max_length=200, help_text='Singer')

class Album(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    start = models.DateField(blank=True)
    