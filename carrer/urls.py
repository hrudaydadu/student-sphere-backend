# from .views import
from django.urls import path,include
from .views import *

urlpatterns = [
    path('carrer/',CarrerApiview.as_view(),name="CarrerApiview"),
    path('carrer/<int:pk>/',CarrerApiview.as_view(),name="CarrerApiview"),
    path('comment/',CarrerCommentAPIview.as_view(),name="CarrerCommentAPIview"),
    path('comment/<int:pk>/',CarrerCommentAPIview.as_view(),name="CarrerCommentAPIview"),
]
