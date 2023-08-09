
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, 
    PermissionsMixin
)
from django.db import models 

from core_app.abstract import AbstractModel, AbstractManager

class UserManager(BaseUserManager, AbstractManager):
    """User manager -> managing for users from model AbstractBaseUser"""" 

    def create_user(
        self, username: str,
        phone: str, 
        email: str, 
        password: str=None, 
        **kwargs):
        """Create a User with email, phone number, username, password and return"""

        # exceptions
        if username is None:
            raise TypeError('Пользователь должен иметь имя')
        if email is None:
            raise TypeError('У Пользователя должен быть email')
        if password is None:
            raise TypeError('У Пользователя должен быть пароль')
        if phone is None:
            raise TypeError('У Пользователя должен быть номер телефона')
        # create user
        user = self.model(
            username=username, 
            email=self.normalize_email(email), **kwargs
        )
        # setting password for user
        user.set_password(password)
        # saving user in db 
        user.save(using=self._db)
        return user 
