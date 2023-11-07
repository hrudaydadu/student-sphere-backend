from django.shortcuts import render
from .models import NewsUpdate,NewsComment
from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializer import NewsUpdateSerializer,NewCommentSerialzier
from rest_framework import status
# Create your views here.


class NewupdateApiview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
            
        try:
            return NewsUpdate.objects.get(pk=pk)
        except NewsUpdate.DoesNotExist:
            raise Http404
       
    def get(self, request, pk=None, format=None):
        current_user = request.user
        if pk:
            data = self.get_object(pk)
            serializer = NewsUpdateSerializer(data)
            return Response(serializer.data)

        else:
            data = NewsUpdate.objects.filter(user=current_user)
            serializer = NewsUpdateSerializer(data, many=True)
            if not data.exists():
                return Response({'detail': 'No NewsUpdate found for the current user'}, status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.data)
        
    def post(self, request, format=None):
            current_user = request.user
            mutable_data = request.data.copy()
            mutable_data['user'] = current_user.id  
            serializer = NewsUpdateSerializer(data=mutable_data)
            
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
            NewsUpdate_to_update = NewsUpdate.objects.get(pk=pk)

            serializer = NewsUpdateSerializer(instance=NewsUpdate_to_update,data=request.data, partial=True)

            serializer.is_valid(raise_exception=True)
            serializer.save()
            response = Response()

            response.data = {
                'message': 'News and Update Updated Successfully',
                'data': serializer.data
            }

            return response
    

    def delete(self, request, pk, format=None):
            NewsUpdate_to_delete =  NewsUpdate.objects.get(pk=pk)

            # delete the todo
            NewsUpdate_to_delete.delete()

            return Response({
                'message': 'NewsUpdate Deleted Successfully'
            })
    


class NewsCommentAPIview(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
            
        try:
            return NewsComment.objects.get(pk=pk)
        except NewsComment.DoesNotExist:
            raise Http404
       
    def get(self, request, pk=None, format=None):
        current_user = request.user
        if pk:
            data = self.get_object(pk)
            serializer = NewCommentSerialzier(data)
            return Response(serializer.data)

        else:
            data = NewsComment.objects.filter(user=current_user)
            serializer = NewCommentSerialzier(data, many=True)
            if not data.exists():
                return Response({'detail': 'No News comment found for the current user'}, status=status.HTTP_404_NOT_FOUND)

            return Response(serializer.data)
        
    def post(self, request, format=None):
            current_user = request.user
            mutable_data = request.data.copy()
            mutable_data['user'] = current_user.id  
            serializer = NewCommentSerialzier(data=mutable_data)
            
            serializer.is_valid(raise_exception=True)
            serializer.save()

            response = Response()

            response.data = {
                'message': 'comment post Successfully',
                'data': serializer.data
            }

            return response
    