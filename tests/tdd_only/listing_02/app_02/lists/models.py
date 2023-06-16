from django.db import models
from django.urls import reverse
from django.conf import settings

class List(models.Model):
    """model for list""" 

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

class Item(models.Model):
    """ELement of list""" 

    text = models.TextField(default='', null=True)
    my_list = models.ForeignKey(List, null=True, on_delete=models.CASCADE, default=None)
    item_text = models.BooleanField(default=False)
