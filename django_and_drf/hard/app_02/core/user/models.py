from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from core.abstract.models import AbstractManager, AbstractModel
import uuid


class UserManager(BaseUserManager):
    """Custom user manager""" 

    def get_object_by_public_id(self, public_id):
        """Get object and return""" 

        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404
    
    def create_user(self, username, email, password=None, **kwargs):
        """Create and return `user ` with an enmail, phone, number, username and pass"""

        if username is None:
            raise TypeError('Users must have a username')
        if email is None:
            raise TypeError('Users must have an email')
        if password is None:
            raise TypeError('Users must have a password')
        
        user = self.model(username=username, email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_superuser(self, username, email, password, **kwargs):
        """Create and return a `User`1 with superuser (admin) permissions"""

        if password is None:
            raise TypeError('Superusers must have a password')
        if username is None:
            raise TypeError('Superusers must have an username')
        if email is None:
            raise TypeError('Suprusers must have an email')

        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user 
class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    """Create user model""" 

    public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, blank=True, upload_to='images/')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    objects = UserManager()
    post_liked = models.ManyToManyField('core_post.Post', related_name='liked_by')

    def __str__(self):
        return f'{self.email}'

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'