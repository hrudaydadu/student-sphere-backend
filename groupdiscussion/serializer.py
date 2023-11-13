from rest_framework.serializers import  ModelSerializer
from .models import *
from account.serializer import UserSerializers
from account.models import User


    

class SearchCollageSerialzier(ModelSerializer):
    class Meta:
        model = SearchCollage
        fields = "__all__"

class HouseSerialzier(ModelSerializer):
    class Meta:
        model = House
        fields = "__all__"
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializers(instance.user).data
        return response

class HouseCommentSerialzier(ModelSerializer):
    class Meta:
        model = HouseComment
        fields = "__all__"