from rest_framework.serializers import  ModelSerializer
from .models import *
from account.serializer import UserSerializers

class NewsUpdateSerializer(ModelSerializer):
    class Meta:
        model = NewsUpdate
        fields = "__all__"
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['user'] = UserSerializers(instance.user).data
        return response
    

class NewCommentSerialzier(ModelSerializer):
    class Meta:
        model = NewsComment
        fields = "__all__"