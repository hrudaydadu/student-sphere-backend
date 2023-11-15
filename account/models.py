from django.db import models
from django.contrib.auth.models import AbstractUser,PermissionsMixin
from django.utils.translation import gettext_lazy  as _
from account.managers import CustomUserManager
from rest_framework_simplejwt.tokens import RefreshToken
# Create your models here.
from django.contrib.auth.models import User


# resgiter the user
AUTH_PROVIDERS = {'email': 'email'}
class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    phone_no = models.CharField(unique=True,  null=True,max_length=10)

    name = models.CharField(max_length=100,null=True)
    auth_provider = models.CharField(max_length=255, blank=False, null=False, default=AUTH_PROVIDERS.get('email'))

    profile_picture = models.URLField(blank=True,null=True)
    personal_website = models.URLField(blank=True,null=True)
    facebook_profile = models.URLField(blank=True,null=True)
    linkdin_profile = models.URLField(blank=True,null=True)
    collage_id = models.CharField(max_length=100,blank=True,null=True)
    Grades = models.CharField(max_length=255,blank=True,null=True)
    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    objects = CustomUserManager() 
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.email
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }
    

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)