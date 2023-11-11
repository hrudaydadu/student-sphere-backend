from django.db import models

# Create your models here.

class SearchCollage(models.Model):
    image_urls = models.URLField()
    name = models.CharField(max_length=100)
    