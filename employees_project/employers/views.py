from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework import permissions
from .serializers import EmployeeSerializer, FileUploadSerializer,SaveFileSerializer
from .models import Employee
from django.shortcuts import render
from rest_framework import generics
import io, csv, pandas as pd
from rest_framework.response import Response
from department.models import Department
from rest_framework import status


# Create your views here.

class CreateEmployeesView(CreateAPIView):
    """
    API to create employees
    """

    permission_classes = [permissions.IsAuthenticated]  
    serializer_class = EmployeeSerializer


class ListEmployeesView(ListAPIView):
    """
    API to list all the employees
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        employees = Employee.objects.all()
        return employees



class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    
    def post(self, request, *args, **kwargs):
        """
        Api to upload a csv file and insert 
        the data to employee model
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _, row in reader.iterrows():
            department = Department.objects.get(id=row['department'])
            new_file = Employee(
                       employee_code = row['employee_code'],
                       employee_name= row["employee_name"],
                       department= department,
                       age= row["age"],
                       experience= row["experience"]
                       )
            new_file.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)
