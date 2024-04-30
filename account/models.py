from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator

class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=200)
    phone_regex = RegexValidator(regex=r'\+2588[2-7]\d{7}\b',message="O número de telefone deve ser digitado no formato: '+258849293949'. São permitidos até 13 dígitos.")
    phone_number = models.CharField(validators=[phone_regex], max_length=13, unique=True, blank=False)
    email = models.EmailField(('email address'), blank=True)
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

# Create your models here.
