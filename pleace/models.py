from django.db import models


class PleaceInformation(models.Model):
    place_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    is_active = models.BooleanField(default=True)

    

# Create your models here.
