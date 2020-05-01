from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import speedtest_result
from . serializers import resultSerializer
from rest_framework.parsers import JSONParser
import json
var = {"error code": 0, "message": "success"}

class speedtest_list(APIView):
    def get(self, request):
        all_result = speedtest_result.objects.all()
        serializers = resultSerializer(all_result, many = True)
        return Response(data=var,status=201)

    def post(self,request):
        serializers = resultSerializer(data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(data = var, status= 201)
        return Response(serializers.errors, status= 400)


class speedtest_detail(APIView):
    def get_object(self, id):
        try:
            return speedtest_result.objects.get(id=id)
        except:
            return Response(serializers.errors, status= 400)

    def get(self, request, id):
        one_result = self.get_object(id)
        serializers = resultSerializer(one_result)
        return Response(serializers.data)

    def put(self,request, id):
        one_result = self.get_object(id)
        serializers = resultSerializer(one_result, data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= 201)
        return Response(serializers.errors, status= 400)

    def delete(self, request, id, format=None):
        one_result = self.get_object(id)
        one_result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
