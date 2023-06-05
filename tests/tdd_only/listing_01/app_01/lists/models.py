from django.db import models


class Item(models.Model):
    """ELement of list""" 

    text = models.TextField(default='', null=True)
    my_list = models.TextField(default='')

class List(models.Model):
    """model for list""" 

    pass