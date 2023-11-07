from django.db import models
from account.models import BaseModel,User
from tinymce.models import HTMLField
# Create your models here.


class NewsUpdate(BaseModel):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    Description = HTMLField(blank=True,null=True)


class NewsComment(BaseModel):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    news = models.ForeignKey(NewsUpdate,on_delete=models.CASCADE)
    comment = models.CharField(max_length=100)
