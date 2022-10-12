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


class LatestNewsAndUpdates(models.Model):
    newsHeading = models.CharField(blank=False, unique=False, max_length=256)
    imageData = models.ImageField(upload_to='news_heading_images/', default=None)


class CourseDetails(models.Model):
    imageData = models.ImageField(upload_to='course_images/', default=None)
    courseName = models.CharField(blank=False, unique=False, max_length=256)
    duration = models.CharField(blank=False, unique=False, max_length=256)
