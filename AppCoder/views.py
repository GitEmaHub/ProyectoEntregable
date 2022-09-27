from http.client import HTTPResponse
from django.shortcuts import render
from AppCoder.models import *
from AppCoder.forms import FormularioCurso
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

def formulario1(request):

    if request.method=="POST":

        formulario1 = FormularioCurso(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            cursoF = Curso(nombre=info["curso"], camada=info["camada"])
            cursoF.save()

            return render(request, "AppCoder/inicio.html")

    else:

        formulario1 = FormularioCurso()
 
    return render(request, "AppCoder/formu1.html", {"form1":formulario1})


def BusquedaCurso(request):

    return render(request, "AppCoder/BusquedaCurso.html")

def buscar(request):

    if request.GET["camada"]:
        
        busqueda = request.GET["camada"]
        cursos = Curso.objects.filter(camada__iexact=busqueda)

        return render(request, "AppCoder/inicio.html", {"cursos":cursos, "busqueda":busqueda})

    else:

        mensaje = "No enviaste los datos correctos."

    return HttpResponse(mensaje)
