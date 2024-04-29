from django.db import models


class PleaceInformation(models.Model):
    place_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    city = models.CharField(max_length=300, unique=False)
    street_adress = models.CharField(max_length=200, unique=False)
    price = models.FloatField(blank=True)
    facebook = models.URLField(max_length=300, blank=True)
    instagram = models.URLField(max_length=300, blank=True)
    images = models.ImageField(upload_to='images')

class placeDetailInfo(models.Model):
    hosts_support = models.CharField(max_length=100)
    Rooms = models.CharField(max_length=100)
    Toilets = models.CharField(max_length=100)

class department_id(models.Model):
    title = models.CharField(max_length=100)

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    



    

# Create your models here.
