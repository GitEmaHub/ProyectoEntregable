from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()

class resena(models.Model):

    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    correo = models.EmailField()
    #comentarios = models.CharField(max_length=60)
    