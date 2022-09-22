from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse("vista inicio")

def curso(request):

    curso2 = Curso(nombre="Diseno", camada=656)
    curso2.save()

    return render(request, "AppCoder/curso.html")
