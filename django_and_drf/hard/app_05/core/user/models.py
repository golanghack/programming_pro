from django.db import models 
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from core.abstract.models import AbstractManager, AbstractModel


def user_directory_path(instance: str, filename: str) -> str:
    """-> upload file in MEDIA_ROOT/user_<id>/<filename>""" 

    return f'user_{instance.public_id}/{filename}'

class UserManager(BaseUserManager, AbstractManager):
    """User manager universaly"""

    def create_user(self, 
                    username: str, 
                    email: str, 
                    password: str=None, 
                    **kwargs):
        """Create User with this parameters:
        :username -> string
        :email    -> string
        :password -> string -> default -> None
        **kwargs  -> any parameters
        """ 

        if username is None:
            raise TypeError('Users must have a username')
        if email is None:
            raise TypeError('Users must be email')
        if password is None:
            raise TypeError('User must be password')
        
        # create user 
        user = self.model(
            username=username, 
            email=self.normalize_email(email),
            **kwargs
        )
        user.set_password(password)
        user.save(using=self._db)
        return user 

    def create_superuser(self, 
                        username: str, 
                        email: str, 
                        password: str=None, 
                        **kwargs):
        """Create superuser with this parameters and superuser permissions 
        :username   -> string 
        :email      -> string
        :password   -> string -> default -> None 
        **kwargs
        """ 

        if password is None:
            raise TypeError('Superuser must have a password')
        if email is None:
            raise TypeError('Superuser must have an email')
        if username is None:
            raise TypeError('Superuser must have an username')

        user = self.create_user(username, email, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user 

class User(AbstractModel, AbstractBaseUser, PermissionsMixin):
    """User model""" 

    username: str=models.CharField(db_index=True, 
                                    max_length=255, 
                                    unique=True)
    first_name: str=models.CharField(max_length=255)
    last_name: str=models.CharField(max_length=255)
    email: str=models.EmailField(db_index=True, 
                                    unique=True)
    is_active: bool=models.BooleanField(default=True)
    is_superuser: bool=models.BooleanField(default=False)
    bio: str=models.TextField(null=True)
    avatar = models.ImageField(null=True, 
                                blank=True, 
                                upload_to=user_directory_path)
    posts_liked = models.ManyToManyField('core_post.Post', 
                                related_name='liked_by')
    comments_liked = models.ManyToManyField('core_comment.Comment', 
                                related_name='commented_by')
    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    objects = UserManager()

    def __str__(self):
        return f'{self.email}'

    @property
    def name(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
    def like_post(self, post):
        """Like post""" 

        return self.posts_liked.add(post)
    
    def remove_like_post(self, post):
        """Remove like""" 

        return self.posts_liked.remove(post)

    def has_liked_post(self, post) -> bool:
        """Return True if likes have or False""" 

        return self.posts_liked.filter(pk=post.pk).exists()

    def like_comment(self, comment: str):
        """Like comment""" 

        return self.comments_liked.add(comment)

    def remove_like_comment(self, comment: str):
        """Remove like comment""" 

        return self.comments_liked.remove(comment)

    def has_liked_comment(self, comment: str) -> bool:
        """Return True is have comment like or False""" 

        return self.comments_liked.filter(pk=comment.pk).exists()