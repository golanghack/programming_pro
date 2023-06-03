from django.db import models


class Item(models.Model):
    """ELement of list""" 

    text = models.TextField(default='', null=True)

    