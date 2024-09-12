from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from API.serializers import empserializer
from dbapp.models import Employee
from rest_framework.status import HTTP_201_CREATED,HTTP_400_BAD_REQUEST
# Create your views here.
@api_view(['GET','POST'])
def empget(request):
    if request.method=='GET':
        data=Employee.objects.all()
        task=empserializer(data,many=True)
        return Response(task.data)
    if request.method=='POST':
        empdata=empserializer(data=request.data)
        if empdata.is_valid():
            empdata.save()
            return Response(status=HTTP_201_CREATED)
        else:
            return Response(status=HTTP_400_BAD_REQUEST)