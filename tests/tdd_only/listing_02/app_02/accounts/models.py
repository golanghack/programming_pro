from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class User(models.Model):
    """User""" 

    email = models.EmailField(primary_key=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True


class Token(models.Model):
    """-> our Token""" 

    email = models.EmailField()
    uid = models.CharField(max_length=255, unique=True)

class ListUserManager(BaseUserManager):
    """-> manage user list"""

    def create_user(self, email):
        """Create user""" 

        ListUser.objects.create(email=email)
    
    def create_superuser(self, email, password):
        """-> create superuser""" 

        self.create_user(email)
        
class ListUser(AbstractBaseUser, PermissionsMixin):
    """-> user for list"""

    email = models.EmailField(primary_key=True)
    USERNAME_FIELD = 'email'

    objects = ListUserManager()

    @property
    def is_staff(self):
        return self.email == 'golanghack@example.com'

    @property
    def is_active(self):
        return True

    class Meta:
        abstract = True