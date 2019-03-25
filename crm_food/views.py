from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView

from crm_food.models import (
                        Table,
                        Department,
                        Status,
                        ServicePercentage,
                     )

from crm_food.serializer import (
                        TableSerializer,
                        DepartmentSerializer,
                        StatusSerializer,
                        ServicePercentageSerializer,
                    )




def index(request):
    return render(request,'index.html',{})



class TablesListView(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer

    #def delete



class DepartmentsListView(generics.ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer


class StatusesListView(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer


class ServicePercentageListView(generics.ListCreateAPIView):
    queryset = ServicePercentage.objects.all()
    serializer_class = ServicePercentageSerializer



# Create your views here.
