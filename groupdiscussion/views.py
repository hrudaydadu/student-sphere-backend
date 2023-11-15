from django.shortcuts import render
from .filters import SearchCollageFilters
from .serializer import  *
from .models import  *
from rest_framework import generics,status
from rest_framework.permissions import AllowAny,IsAuthenticated
import django_filters
from rest_framework.filters import SearchFilter
from rest_framework.response import Response

from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework import status
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
    



# Create your views here.


class HouseApiview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
            
        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            raise Http404
       
    def get(self, request, pk=None, format=None):
        current_user = request.user
        if pk:
            data = self.get_object(pk)
            serializer = HouseSerialzier(data)
            return Response(serializer.data)

        else:
            data = House.objects.all().order_by('-id')
            serializer = HouseSerialzier(data, many=True)
            if not data.exists():
                return Response({'detail': 'No House found for the current user'}, status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.data)
        
    def post(self, request, format=None):
            current_user = request.user
            mutable_data = request.data.copy()
            mutable_data['user'] = current_user.id  
            serializer = HouseSerialzier(data=mutable_data)
            
            serializer.is_valid(raise_exception=True)
            serializer.save()

            response = Response()

            response.data = {
                'message': 'House  Created Successfully',
                'data': serializer.data
            }

            return response
    

    def patch(self, request, pk=None, format=None):
                # Get the todo to update
            House_to_update = House.objects.get(pk=pk)

            serializer = HouseSerialzier(instance=House_to_update,data=request.data, partial=True)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response()

            response.data = {
                'message': 'House Updated Successfully',
                'data': serializer.data
            }

            return response
    

    def delete(self, request, pk, format=None):
            House_to_delete =  House.objects.get(pk=pk)

            # delete the todo
            House_to_delete.delete()

            return Response({
                'message': 'House Deleted Successfully'
            })
    



class HouseuserApiview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
            
        try:
            return House.objects.get(pk=pk)
        except House.DoesNotExist:
            raise Http404
       
    def get(self, request, pk=None, format=None):
        current_user = request.user
        if pk:
            pass

        else:
            data = House.objects.filter(user=current_user).order_by('-id')
            serializer = HouseSerialzier(data, many=True)
            if not data.exists():
                return Response({'detail': 'No House found for the current user'}, status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.data)


class HouseCommentAPIview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
            
        try:
            return HouseComment.objects.get(pk=pk)
        except HouseComment.DoesNotExist:
            raise Http404
       
    def get(self, request, pk=None, format=None):
        current_user = request.user
        if pk:
            data = self.get_object(pk)
            serializer = HouseCommentSerialzier(data)
            return Response(serializer.data)

        else:
              
            houses_id = request.GET.get('houses_id')

          
            if not houses_id:
                return Response({'detail': 'Houses ID is required'}, status=status.HTTP_400_BAD_REQUEST)

           
            comments = HouseComment.objects.filter(houses_id__id=houses_id).order_by('-id')
            
           
            if not comments.exists():
                return Response({'detail': 'No Houses comments found for the specified House'}, status=status.HTTP_404_NOT_FOUND)

            serializer = HouseCommentSerialzier(comments, many=True)
            return Response(serializer.data)
        
    def post(self, request, format=None):
            current_user = request.user
            mutable_data = request.data.copy()
            mutable_data['user'] = current_user.id  
            serializer = HouseCommentSerialzier(data=mutable_data)
            
            serializer.is_valid(raise_exception=True)
            serializer.save()

            response = Response()

            response.data = {
                'message': 'comment post Successfully',
                'data': serializer.data
            }

            return response
    