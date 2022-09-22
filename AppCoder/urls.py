from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path("", inicio, name="Inicio"), 
    path("curso/", curso, name="Curso"), 
    path("resena/", resena, name="Resena"), 
]
 