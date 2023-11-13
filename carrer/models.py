from django.db import models
from account.models import BaseModel,User
from tinymce.models import HTMLField
# Create your models here.


class Carrer(BaseModel):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    Description = HTMLField(blank=True,null=True)


class CarrerComment(BaseModel):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    carrers = models.ForeignKey(Carrer,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
