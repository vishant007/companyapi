from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CompanySerializer,EmployeeSerializer
from .models import Company, Employee
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer