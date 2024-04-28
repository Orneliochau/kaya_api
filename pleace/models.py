from django.db import models


class PleaceInformation(models.Model):
    place_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    is_active = models.BooleanField(default=True)

class department_id(models.Model):
    title = models.CharField(max_length=100)

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)


    

# Create your models here.
