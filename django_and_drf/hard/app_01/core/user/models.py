import uuid
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404


class UserManager(BaseUserManager):
    """-> custom managing users""" 

    def get_object_by_public_id(self, public_id: int):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
    
    def create_user(self, username: str, email: str, password: str=None, **kwargs):
        """Create and return a 'User' with email, phone number, username and password""" 

        if username is None:
            raise TypeError('Users must be a username')
        if email is None:
            raise TypeError('Users must be a emaul')
        if password is None:
            raise TypeError('Users must be pass')

        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_superuser(self, username: str, email: str, password: str, **kwargs):
        """Creating and return a 'User' with superuser premis-s"""

        if password is None:
            raise TypeError('Superuser must have a pass-d')
        if email is None:
            raise TypeError('Superuser must have an email')
        if username is None:
            raise TypeError('superuser must have an username')
        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user 




class User(AbstractBaseUser, PermissionsMixin):
    """Model for user"""

    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()
    
    def __str__(self):
        return f'{self.email}'

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
