from .models import Measurement
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.http import JsonResponse
from django.urls import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
import requests
import json

def check_carrito(data):
    r = requests.get(settings.PATH_VAR, headers={"Accept":"application/json"})
    carritos = r.json()
    for carrito in carritos:
        if data["carrito"] == carrito["id"]:
            return True
    return False

def MeasurementList(request):
    queryset = Measurement.objects.all()
    context = list(queryset.values('carrito', 'value', 'unit', 'correo'))
    return JsonResponse(context, safe=False)

def MeasurementCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_carrito(data_json) == True:
            measurement = Measurement()
            measurement.carrito = data_json['carrito']
            measurement.value = data_json['value']
            measurement.unit = data_json['unit']
            measurement.correo = data_json['correo']
            measurement.save()
            name = data_json['carrito']
            email = data_json['correo']
            message = data_json['value']

            body = render_to_string(
            'email_content.html', {
                'name': name,
                'email': 'Jorotui@uni.co',
                'message': message,
            },
            )

            email_message = EmailMessage(
            subject='Valor del carrito compras jorotui',
            body=body,
            from_email=['js.bautista@uniandes.edu.co']
            to=email,
            )
            email_message.content_subtype = 'html'
            email_message.send()    
            return HttpResponse("successfully created factura")
        else:
            return HttpResponse("unsuccessfully created factura. Carrito does not exist")