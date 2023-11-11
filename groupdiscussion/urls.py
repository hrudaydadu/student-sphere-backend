# from .views import
from django.urls import path,include
from .views import SearchCollageSearchView

urlpatterns = [
    path('search/',SearchCollageSearchView.as_view(),name="SearchCollageSearchView"),
]
