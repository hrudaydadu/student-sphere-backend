# from .views import
from django.urls import path,include
from .views import NewupdateApiview,NewsCommentAPIview

urlpatterns = [
    path('update/',NewupdateApiview.as_view(),name="NewupdateApiview"),
    path('news/<int:pk>/',NewupdateApiview.as_view(),name="NewupdateApiview"),
    path('comment/',NewsCommentAPIview.as_view(),name="NewsComment"),
    path('comment/<int:pk>/',NewsCommentAPIview.as_view(),name="NewsComment"),
]
