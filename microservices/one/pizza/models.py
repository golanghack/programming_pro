from django.db import models

class Pizza(models.Model):
    """Pizza model."""
    
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=250)
    
    
