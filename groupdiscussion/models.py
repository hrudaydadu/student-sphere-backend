from django.db import models
from account.models import BaseModel,User
from tinymce.models import HTMLField
# Create your models here.

class SearchCollage(models.Model):
    image_urls = models.URLField()
    name = models.CharField(max_length=100)


class House(BaseModel):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    Description = HTMLField(blank=True,null=True)


    


class HouseComment(BaseModel):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    houses = models.ForeignKey(House,on_delete=models.CASCADE)
    sheduleDate = models.DateField(null=True)
    comment = models.CharField(max_length=100)