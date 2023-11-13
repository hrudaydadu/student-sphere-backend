# from .views import
from django.urls import path,include
from .views import SearchCollageSearchView,HouseCommentAPIview,HouseApiview

urlpatterns = [
    path('search/',SearchCollageSearchView.as_view(),name="SearchCollageSearchView"),
    path('house-comment/',HouseCommentAPIview.as_view(),name="HouseCommentAPIview"),
    path('house-comment/<int:pk>/',HouseCommentAPIview.as_view(),name="HouseCommentAPIview"),
    path('house/',HouseApiview.as_view(),name="HouseApiview"),
    path('house/<int:pk>/',HouseApiview.as_view(),name="HouseApiview"),
]
