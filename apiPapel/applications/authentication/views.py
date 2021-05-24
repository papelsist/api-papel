from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
import bcrypt 

from .models import Usuario
# Create your views here.


@csrf_exempt
def login(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    usuario = body['usuario']
    password = body['password']
    try:
        user = Usuario.objects.get(username = usuario)
    except Usuario.DoesNotExist:
        user = None
    if user:
        if bcrypt.checkpw(password.encode('utf8'), user.password.encode('utf-8')):
            print("Si es")
        else:
            print("No es")
    else:
        print("Usuario no encontrado")
    
    return JsonResponse("Success", safe=False)

@csrf_exempt
def changePassword(request):
    body_unicode = request.body.decode("utf-8")
    body = json.loads(body_unicode)
    usuario = body['usuario']
    password = body['password']
    try:
        user = Usuario.objects.get(username = usuario)
    except Usuario.DoesNotExist:
        user = None

    if user:
        hashed = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
        user.password = hashed.decode('ascii')
        user.save()
        print(hashed.decode('ascii'))
    else:
        print("Usuario no encontrado")
    
    return JsonResponse("Success", safe=False)

