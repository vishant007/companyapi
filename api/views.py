from django.shortcuts import render
from rest_framework import viewsets, status
from .serializers import CompanySerializer,EmployeeSerializer
from .models import Company, Employee
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().order_by('name')
    serializer_class = CompanySerializer

    # create a custom action to get all employees of a company
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = self.get_object()
            employees = Employee.objects.filter(company=company)
            serializer = EmployeeSerializer(employees, many=True, context={'request': request})
            return Response(serializer.data)
        except Company.DoesNotExist:
            return Response({"error": "Company not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer