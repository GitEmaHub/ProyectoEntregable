from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def curso(request):

    #curso2 = Curso(nombre="Diseno", camada=656)
    #curso2.save()

    return render(request, "AppCoder/curso.html")

def resena(request):

    return render(request, "AppCoder/resena.html")

def formulario(request):

    if request.method=="POST":

        cursoF = Curso(nombre=request.POST["curso"], camada=request.POST["camada"])
        cursoF.save()

        return render(request, "AppCoder/formulario.html")

    return render(request, "AppCoder/formulario.html")
