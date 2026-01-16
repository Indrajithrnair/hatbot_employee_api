from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer

from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

# Create your views here.

def root(request):
    return JsonResponse({"hello": "world"})

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def employee_list_create(request):
    
    if request.method=="GET":
        employees = Employee.objects.all()

        department = request.query_params.get('department')
        role = request.query_params.get('role')

        if department:
            employees = employees.filter(department=department)
        if role:
            employees = employees.filter(role=role)
        
        paginator = PageNumberPagination()
        paginator.page_size = 10

        page = paginator.paginate_queryset(employees, request)
        serializer = EmployeeSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)
    
    if request.method=="POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', "DELETE"])
@permission_classes([IsAuthenticated])
def employee_detail(request, pk):
    
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({"detail": "Employee not found..!"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method=="PUT":
        serializer = EmployeeSerializer(employee, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=="DELETE":
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
