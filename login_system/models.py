from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

class UserManager(BaseUserManager):

    def create_user(self, username, role= None, password=None):
        if username is None or username == '':
            raise TypeError('Users should have a username')

        user = self.model(username = username, role= role)
        user.set_password(password)
        user.save()

        return user


    def create_superuser(self, username, password=None,role=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username, password = password,role = role)
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.role = 1
        user.save()

        return user

class User(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
        (1, 'Admin'),
        (2, 'Member'),
        (3, 'Expert')
    )

    username = models.CharField(max_length=255, unique=True, db_index=True)
    role = models.PositiveSmallIntegerField(choices = USER_TYPE_CHOICES)# ,blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['role']

    objects = UserManager()

    def __str__(self):
        return self.username