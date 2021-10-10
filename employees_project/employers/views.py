from django.shortcuts import render
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from rest_framework import permissions
from .serializers import EmployeeSerializer
from .models import Employee


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
