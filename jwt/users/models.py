from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    username = None # overwrite username field of abstract user

    USERNAME_FIELD = 'email' # login with email instead of password
    REQUIRED_FIELDS =  []

