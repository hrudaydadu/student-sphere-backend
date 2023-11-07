from django.urls import path,include
from .views import Register,Login,userData,update_profile,VerifyEmail
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
     path('register/', Register.as_view(),name="register"),
     path('login/', Login.as_view(),name="login"),
     path('profile/',userData.as_view(),name="profile"),
     path('update-profile/',update_profile.as_view(),name="update_profile"),
     path('email-verify/',VerifyEmail.as_view(),name="email-verify"),
]
