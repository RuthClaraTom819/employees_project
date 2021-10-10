from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Employee
from .forms import GreetingAdminForm


class EmployeeAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    search_fields = ('employee_code', 'employee_name',
                     'department', 'age', 'experience')
    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        import pdb
        pdb.set_trace()
        for row in dataset:
            if int(row[4]) < int(row[5]):
                raise ValidationError('Product offer price cannot be greater than Product MRP. '
                                      'Error in row with id = %s' % row[0])



admin.site.register(Employee, EmployeeAdmin)
