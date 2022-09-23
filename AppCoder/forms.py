from django import forms

class FormularioCurso(forms.Form):

    curso = forms.CharField()
    camada = forms.IntegerField()   