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

class employeelist(APIView):

    def get(self, request):
        employees1 = employees.objects.all()
        serializers = employeesSerializer(employees1, many = True)
        return Response(serializers.data)

    def post(self):
        pass