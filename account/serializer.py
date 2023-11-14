from .models import User
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from django.contrib import auth
from django.contrib.sites.shortcuts import get_current_site

# register serializers
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name','phone_no','email','password','profile_picture','personal_website','facebook_profile',
                 'linkdin_profile','collage_id','Grades',"is_verified"]
        extra_kwargs = {
            'password' :{'write_only':True}  #  to does not return password in api ## postman
        }
    # convert password to hash key
    def create(self, validated_data):
        email = validated_data.get('email', None)
        if email and not email.endswith('@vasal.com'):
            raise serializers.ValidationError("Invalid email domain")
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        if len(password) <6:
            raise serializers.ValidationError("entre strong password")
        instance.save()
        return instance
    
    def imagePlanImage(self, obj):
        return self.build_absolute_image_url(obj.profile_picture)
    
    def build_absolute_image_url(self, image_path):
        request = self.context.get('request')
        if request is not None:
            return request.build_absolute_uri(image_path)
        else:
            # If request is not available (for example, in shell), use the default site
            site = get_current_site(None)
            return f"{site.scheme}://{site.domain}{image_path}"
   
# login serializers

class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

    class Meta:
        model = User
        fields = ['email', 'password', 'tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        if filtered_user_by_email.exists() and filtered_user_by_email[0].auth_provider != 'email':
            raise AuthenticationFailed(
                detail='Please continue your login using ' + filtered_user_by_email[0].auth_provider)
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        if not user.is_verified:
            raise AuthenticationFailed('Email is not verified')

        return {
            'email': user.email,
            'tokens': user.tokens
        }

        return super().validate(attrs)
    

# email verification
class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
