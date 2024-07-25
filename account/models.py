from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from .managers import UserManager

class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=200)
    email = models.EmailField(('email address'), unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()

# Create your models here.
