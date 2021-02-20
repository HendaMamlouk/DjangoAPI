from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departements, Employees
from EmployeeApp.serializers import DepartementSerializer, EmployeeSerializer

from django.core.files.storage import default_storage
# Create your views here.

@csrf_exempt
def employeeApi(request, id=0):
    if request.method=='GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    elif request.method=='POST':
        employee_data=JSONParser().parse(request)
        employee_serializer = EmployeeSerializer(data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Added Successfully!!", safe=False)
        return JsonResponse("Failed to Add.", safe=False)   
    elif request.method=='PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId=employee_data['EmployeeId'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully!!", safe=False)
        return JsonResponse("Failed to update.", safe=False)
    elif request.method=='DELETE':
        employee = Employees.objects.get(EmployeeId=id)
        employee.delete()
        return JsonResponse("Deleted Successfully!!", safe=False)

@csrf_exempt
def SaveFile(request):
    file = request.FILES['uploadedFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)


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