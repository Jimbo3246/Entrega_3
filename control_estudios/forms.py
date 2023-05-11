from django import forms

class CursoFormulario(forms.Form):
    nombre=forms.CharField(max_length=64)
    comision=forms.IntegerField(required=True, max_value=5000)


class EstudianteFormulario(forms.Form):
    nombre=forms.CharField(max_length=256)
    apellido=forms.CharField(max_length=256)
    email=forms.EmailField()

class ProfesorFormulario(forms.Form):
    nombre=forms.CharField(max_length=256)
    apellido=forms.CharField(max_length=256)
    profesion=forms.CharField(max_length=256)
    email=forms.EmailField()
class EntregableFormulario(forms.Form):
    nombre=forms.CharField(max_length=256)
    fecha_entrega=forms.DateField(label='Fecha de entrega', input_formats=['%d/%m/%Y'])
    entregado=forms.BooleanField(label='Entregado',help_text='Marcar si esta entregado')
    