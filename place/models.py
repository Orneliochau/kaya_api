from django.db import models
from account.models import CustomUser 


class PleaceInformation(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    province = models.CharField(max_length=200)
    city = models.CharField(max_length=300, unique=False)
    street_adress = models.CharField(max_length=200, unique=False)
    price = models.FloatField(blank=True)
    facebook = models.URLField(max_length=300, blank=True)
    instagram = models.URLField(max_length=300, blank=True)

class placeImages(models.Model):
    place = models.ForeignKey(PleaceInformation, on_delete=models.CASCADE)
    front = models.ImageField(upload_to='images/front')
    back = models.ImageField(upload_to='images/back')
    right = models.ImageField(upload_to='images/right')
    left = models.ImageField(upload_to='images/left')

    
    




    



    

# Create your models here.
