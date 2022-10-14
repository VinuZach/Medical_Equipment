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


class GallerySections(models.Model):
    galleryTitle = models.CharField(blank=False, unique=False, max_length=256)


class GalleryImages(models.Model):
    imageData = models.ImageField(upload_to='gallery_images/', default=None)
    gallery_section = models.ForeignKey(GallerySections, on_delete=models.CASCADE)


class StudentDetails(models.Model):
    joining_date = models.CharField(max_length=20)
    joining_time = models.CharField(max_length=20)
    student_name = models.CharField(max_length=50)
    student_DOB = models.CharField(max_length=20)
    student_mother_name = models.CharField(max_length=50)
    student_mother_occup = models.CharField(max_length=50)
    student_father_name = models.CharField(max_length=50)
    student_father_occup = models.CharField(max_length=50)
    student_gender = models.CharField(max_length=10)
    student_caste_category = models.CharField(max_length=20, default="General")
    presentAddress = models.CharField(max_length=50)
    permanentAddress = models.CharField(max_length=50)
    caste = models.CharField(max_length=20)
    religion = models.CharField(max_length=20)
    mother_tongue = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    mobileNumber = models.CharField(max_length=20)
    emailId = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=20)
    last_attended_school = models.CharField(max_length=30)
    last_attended_school_qual = models.CharField(max_length=30)
    year_of_passing = models.CharField(max_length=10)
    selectedCourse = models.CharField(max_length=20)
    fee_schedule = models.CharField(max_length=10)
    tobe_payed = models.CharField(max_length=50)
    tobe_Qual = models.CharField(max_length=30)
    imageData = models.ImageField(upload_to='students_images/', default=None)
