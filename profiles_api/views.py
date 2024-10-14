from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status

class HelloApiView(APIView):
    serializer_class=serializers.HelloSerializer
    def get(self,response,format=None):
        an_apiview=['This updates will get printed','another update']

        return Response({'message': 'Hello view','an_apiview':an_apiview})
    def post(self,request):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data['name']
            msg=f'Hello {name}'
            return Response({'message':msg})
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk=None):
        return Response({'method':'PUT'})
            
