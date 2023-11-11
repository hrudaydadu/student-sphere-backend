from rest_framework.serializers import  ModelSerializer
from .models import *


    

class SearchCollageSerialzier(ModelSerializer):
    class Meta:
        model = SearchCollage
        fields = "__all__"