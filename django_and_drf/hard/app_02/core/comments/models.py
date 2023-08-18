from django.db import models
from core.abstract.models import AbstractModel, AbstractManager

class CommentManager(AbstractManager):
    pass

class Comment(AbstractModel):
    """Comment model"""

    post = models.ForeignKey('core_post.Post', on_delete=models.PROTECT)
    author = models.ForeignKey('core_user.User', on_delete=models.PROTECT)
    body = models.TextField(default='')
    edited = models.BooleanField(default=False)
    objects = CommentManager()

    def __str__(self):
        return self.author.name 

        
