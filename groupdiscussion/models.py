from django.db import models
from account.models import BaseModel,User
from tinymce.models import HTMLField
# Create your models here.

class SearchCollage(models.Model):
    image_urls = models.URLField()
    name = models.CharField(max_length=100)


class House(BaseModel):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=150,blank=True)
    rent_cost = models.IntegerField(null=True)
    property_url = models.URLField(blank=True,null=True)
    bedroom = models.CharField(max_length=100,blank=True)
    bathroom = models.CharField(max_length=100,blank=True)
    distance_walk = models.CharField(max_length=100,blank=True)
    maximum_occupancy = models.IntegerField(null=True,blank=True)
    special_notes = models.CharField(max_length=100,blank=True)
    available_date = models.DateField(null=True,blank=True)
    contact_name = models.BigIntegerField(null=True)
    whatsApp_number = models.BigIntegerField(null=True)
    email = models.EmailField(blank=True)
    Description = HTMLField(blank=True,null=True)


    


class HouseComment(BaseModel):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    houses_id = models.ForeignKey(House,on_delete=models.CASCADE)
    sheduleDate = models.DateField(null=True)
    comment = models.CharField(max_length=100)