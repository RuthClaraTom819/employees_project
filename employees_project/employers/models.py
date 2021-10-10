from django.db import models
from department.models import Department

# Create your models here.


class Employee(models.Model):
    """
    employees details
    """
    employee_code = models.CharField(max_length=50)
    employee_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    age = models.IntegerField()
    experience = models.IntegerField()


    def __str__(self):
        return self.employee_name