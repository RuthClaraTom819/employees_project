from django.db import models

# Create your models here.


class Branch(models.Model):
    """
    each organization can have branches
    """
    branch_name = models.CharField(max_length=128)
    address = models.TextField(null=True, blank=True)
    branch_phone = models.CharField(max_length=16, blank=True, null=True)


    def __str__(self):
        return self.branch_name


class Department(models.Model):
    """
    Organisation/branch Department
    """
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    department_name = models.CharField(max_length=128)
    department_desc = models.TextField()

    def __str__(self):
        return self.department_name + "_" + self.branch.branch_name
