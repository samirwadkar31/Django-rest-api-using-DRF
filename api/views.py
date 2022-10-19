from django.shortcuts import render
from rest_framework import viewsets
from api.models import CompanyDetails,EmployeeDetails
from api.serializers import CompanySerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset= CompanyDetails.objects.all()
    serializer_class=CompanySerializer

    #companies/{companyId}/emplyees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:
            company=CompanyDetails.objects.get(pk=pk)
            emps=EmployeeDetails.objects.filter(company=company)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Company might not exists !! Error'
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=EmployeeDetails.objects.all()
    serializer_class=EmployeeSerializer
