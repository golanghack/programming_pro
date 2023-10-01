from django.db import models

class Todo(models.Model):
    title = models.CharField(max_length=400)
    body = models.TextField(default='')

    def __str__(self):
        return self.title

        
