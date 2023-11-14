from rest_framework.serializers import  ModelSerializer
from .models import *
from account.serializer import UserSerializers

class CarrerSerializer(ModelSerializer):
    class Meta:
        model = Carrer
        fields = "__all__"
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializers(instance.user).data
        return response
    

class CarrerCommentSerialzier(ModelSerializer):
    class Meta:
        model = CarrerComment
        fields = "__all__"
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializers(instance.user).data
        return response