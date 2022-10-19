from secrets import choice
from django.db import models

# Create your models here.

class CompanyDetails(models.Model):
    company_id=models.AutoField(primary_key=True)
    company_name= models.CharField(max_length=50)
    location=models.CharField(max_length=50)
    about=models.TextField()
    type=models.CharField(max_length=100,choices=
                          (('IT','IT'),
                           ('Non IT','Non IT'),
                           ("Mobiles Phones",'Mobile Phones')
                           ))
    added_date=models.DateTimeField(auto_now=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.company_name +'--'+ self.location

#Employee Model
class EmployeeDetails(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=50)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(
        ('Manager','Manager'),
        ('Software Developer','SDE'),
        ('Project Leader','Project Manager')
    ))

    company=models.ForeignKey(CompanyDetails, on_delete=models.CASCADE)