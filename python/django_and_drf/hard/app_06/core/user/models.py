import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models 
from django.http import Http404


class UserManager(BaseUserManager):
    """User manager""" 

    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
    
class User(AbstractBaseUser, PermissionsMixin):
    """User class""" 

    public_id = models.UUIDField(db_index=True, 
                                default=uuid.uuid4, 
                                editable=False,
                                unique=True
                                )
    username = models.CharField(db_index=True, 
                                max_length=200,
                                unique=True)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(db_index=True, 
                                unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = ['email']
    REQUIRED_FIELDS = ['username']

    objects = UserManager()
    def __str__(self):
        return f'{self.email}'

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
    
    