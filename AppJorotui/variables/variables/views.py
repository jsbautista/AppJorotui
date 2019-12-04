from .models import Variable
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse
from django.http import JsonResponse
import json

def check_productos(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    productos = r.json()
    for producto in productos:
        if data == carrito["id"]:
            return True
    return False
def VariableList(request):
    queryset = Variable.objects.all()
    context = list(queryset.values('id', 'name','i1','i2','i3','i4'))
    return JsonResponse(context, safe=False)

def VariableCreate(request):
    if request.method == 'POST':
        if check_productos(data_json["i1"]) and check_productos(data_json["i2"]) and check_productos(data_json["i3"]) and check_productos(data_json["i4"])
            data = request.body.decode('utf-8')
            data_json = json.loads(data)
            variable = Variable()
            variable.name = data_json["name"]
            variable.p1 = data_json["i1"]
            variable.p2 = data_json["i2"]
            variable.p3 = data_json["i3"]
            variable.p4 = data_json["i4"]
            variable.save()
            return HttpResponse("successfully created carrito")
        else:
            return HttpResponse("unsuccessfully created carrito. producto does not exist")