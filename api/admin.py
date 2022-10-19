from django.contrib import admin
from api.models import CompanyDetails,EmployeeDetails
# Register your models here..

class CompanyAdmin(admin.ModelAdmin):
    list_display=('company_name','location','type')
    search_fields=('company_name',)

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')
    list_filter=('company',)

admin.site.register(CompanyDetails,CompanyAdmin)
admin.site.register(EmployeeDetails,EmployeeAdmin)
