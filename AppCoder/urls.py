from django.urls import path
from AppCoder.views import work, inicio

urlpatterns = [
    path("", inicio, name="Inicio"), 
    path("work/", work, name="Work"), 
]
 