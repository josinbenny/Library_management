from django.shortcuts import render
from myapp.models import libraryDB
from myapp.serializers import library_serializer
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def library(request,id=0):
    if request.method=="GET":
        obj=libraryDB.objects.all()
        lib=library_serializer(obj,many=True)
        return JsonResponse(lib.data,safe=False)
    elif request.method=="POST":
        lib_data=JSONParser().parse(request)
        obj=library_serializer(data=lib_data)
        if obj.is_valid():
            obj.save()
            return JsonResponse("New Book Added Successfully", safe=False)
        return JsonResponse("Invalid Data",safe=False)
    elif request.method == "PUT":
        lib_data = JSONParser().parse(request)
        libr = libraryDB.objects.get(Book_id=lib_data['Book_id'])
        obj=library_serializer(libr,data=lib_data)
        if obj.is_valid():
            obj.save()
            return JsonResponse('Book details Updated',safe=False)
        return JsonResponse('Invalid Data Provided',safe=False)
    elif request.method=="DELETE":
        libr = libraryDB.objects.get(Book_id=id)
        libr.delete()
        return JsonResponse('Data deleted..!',safe=False)
