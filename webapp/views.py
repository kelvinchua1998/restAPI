from django.shortcuts import render
from django.db import models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer
from rest_framework.parsers import JSONParser


class employeelist(APIView):

    def get(self, request):
        employees1 = employees.objects.all()
        serializers = employeesSerializer(employees1, many = True)
        return Response(serializers.data)

    def post(self,request):
        # data = JSONParser().parse(request)
        serializers = employeesSerializer(data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= 201)
        return Response(serializers.errors, status= 400)


class employee_detail(APIView):
    def get_object(self, id):
        try:
            return employees.objects.get(id=id)
        except:
            return Response(serializers.errors, status= 400)

    def get(self, request, id):
        employees1 = self.get_object(id)
        serializers = employeesSerializer(employees1)
        return Response(serializers.data)

    def put(self,request, id):
        employees1 = self.get_object(id)
        serializers = employeesSerializer(employees1, data= request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= 201)
        return Response(serializers.errors, status= 400)

    def delete(self, request, id, format=None):
        employees1 = self.get_object(id)
        employees1.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
