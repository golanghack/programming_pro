from django.db import models

class Token(models.Model):
    """-> our Token""" 

    email = models.EmailField()
    uid = models.CharField(max_length=255)