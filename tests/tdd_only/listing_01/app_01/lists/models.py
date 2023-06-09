from django.db import models

class List(models.Model):
    """model for list""" 

    pass

class Item(models.Model):
    """ELement of list""" 

    text = models.TextField(default='', null=True)
    my_list = models.ForeignKey(List, null=True, on_delete=models.CASCADE,)

