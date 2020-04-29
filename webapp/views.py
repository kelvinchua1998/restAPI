from django.shortcuts import render
from django.db import models
# Create your views here.
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