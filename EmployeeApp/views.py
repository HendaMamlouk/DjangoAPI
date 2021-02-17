from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departements, Employees
from EmployeeApp.serializers import DepartementSerializer, EmployeeSerializer
# Create your views here.

@csrf_exempt
def departementApi(request, id=0):
    if request.method=='GET':
        departements = Departements.objects.all()
        departements_serializer = DepartementSerializer(departements, many=True)
        return JsonResponse(departements_serializer.data, safe=False)
    elif request.method=='POST':
        departement_data=JSONParser().parse(request)
        departement_serializer = DepartementSerializer(data=departement_data)
        if departement_serializer.is_valid():
            departement_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)   
    elif request.method=='PUT':
        departement_data = JSONParser().parse(request)
        departement = Departements.objects.get(DepartementId=departement_data['DepartementId'])
        departement_serializer = DepartementSerializer(departement, data=departement_data)
        if departement_serializer.is_valid():
            departement_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to update.", safe=False)
    elif request.method=='DELETE':
        departement = Departements.objects.get(DepartementId=id)
        departement.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)