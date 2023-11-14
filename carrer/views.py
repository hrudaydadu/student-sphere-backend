from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from rest_framework import status
# Create your views here.


class CarrerApiview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
            
        try:
            return Carrer.objects.get(pk=pk)
        except Carrer.DoesNotExist:
            raise Http404
       
    def get(self, request, pk=None, format=None):
        current_user = request.user
        if pk:
            data = self.get_object(pk)
            serializer = CarrerSerializer(data)
            return Response(serializer.data)

        else:
            data = Carrer.objects.filter()
            serializer = CarrerSerializer(data, many=True)
            if not data.exists():
                return Response({'detail': 'No Carrer found for the current user'}, status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.data)
        
    def post(self, request, format=None):
            current_user = request.user
            mutable_data = request.data.copy()
            mutable_data['user'] = current_user.id  
            serializer = CarrerSerializer(data=mutable_data)
            
            serializer.is_valid(raise_exception=True)
            serializer.save()

            response = Response()

            response.data = {
                'message': 'News  Created Successfully',
                'data': serializer.data
            }

            return response
    

    def patch(self, request, pk=None, format=None):
                # Get the todo to update
            Carrer_to_update = Carrer.objects.get(pk=pk)

            serializer = CarrerSerializer(instance=Carrer_to_update,data=request.data, partial=True)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response()

            response.data = {
                'message': 'Carrer Updated Successfully',
                'data': serializer.data
            }

            return response
    

    def delete(self, request, pk, format=None):
            Carrer_to_delete =  Carrer.objects.get(pk=pk)

            # delete the todo
            Carrer_to_delete.delete()

            return Response({
                'message': 'Carrer Deleted Successfully'
            })
    


class CarrerCommentAPIview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
            
        try:
            return CarrerComment.objects.get(pk=pk)
        except CarrerComment.DoesNotExist:
            raise Http404
       
    def get(self, request, pk=None, format=None):
        current_user = request.user
        if pk:
            data = self.get_object(pk)
            serializer = CarrerCommentSerialzier(data)
            return Response(serializer.data)

        else:
          
            career_id = request.GET.get('career_id')

          
            if not career_id:
                return Response({'detail': 'Career ID is required'}, status=status.HTTP_400_BAD_REQUEST)

           
            comments = CarrerComment.objects.filter(carrers__id=career_id)
            
           
            if not comments.exists():
                return Response({'detail': 'No career comments found for the specified career'}, status=status.HTTP_404_NOT_FOUND)

            serializer = CarrerCommentSerialzier(comments, many=True)
            return Response(serializer.data)
        
    def post(self, request, format=None):
            current_user = request.user
            mutable_data = request.data.copy()
            mutable_data['user'] = current_user.id  
            serializer = CarrerCommentSerialzier(data=mutable_data)
            
            serializer.is_valid(raise_exception=True)
            serializer.save()

            response = Response()

            response.data = {
                'message': 'comment post Successfully',
                'data': serializer.data
            }

            return response
    