from django.db import models
class List(models.Model):
    text = models.TextField(default=None, null=True)
    

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List,null=True, default=None, on_delete=models.CASCADE, db_index=True)
