from django.shortcuts import render
from .filters import SearchCollageFilters
from .serializer import SearchCollageSerialzier
from .models import SearchCollage
from rest_framework import generics,status
from rest_framework.permissions import AllowAny
import django_filters
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
# Create your views here.


class SearchCollageSearchView(generics.ListAPIView):
    permission_classes = [AllowAny]
    queryset = SearchCollage.objects.all()
    serializer_class = SearchCollageSerialzier
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend, SearchFilter]
    filterset_class = SearchCollageFilters
    search_fields = ['name']


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        
        if not queryset.exists():
            return Response({'detail': 'No data found'}, status=status.HTTP_204_NO_CONTENT)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)