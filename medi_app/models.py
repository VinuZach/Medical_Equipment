from django.db import models

# Create your models here.
# admin@admin.com admin
from django.contrib.auth.models import AbstractUser
from .UserManagers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
