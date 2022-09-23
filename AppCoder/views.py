from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from AppCoder.forms import *

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

        formulario = FormularioCurso(request.POST)

        if formulario.is_valid:

            info = formulario.cleaned_data

            cursoF = Curso(nombre=info["curso"], camada=info["camada"])
            cursoF.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario = FormularioCurso()
 
    return render(request, "AppCoder/formulario.html", {"form1":formulario})
