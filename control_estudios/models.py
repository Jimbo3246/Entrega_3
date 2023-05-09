from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre =models.CharField(max_length=64)
    comision =models.IntegerField()

class Persona(models.Model):
    apellido =models.CharField(max_length=256)
    nombre =models.CharField(max_length=256)
    email= models.EmailField()
    class Meta:
        abstract=True

class Profesor(Persona):
    profesion=models.CharField(max_length=256)

class Estudiante(Persona):
    pass 
class Entregable(models.Model):
     nombre =models.CharField(max_length=256)
     fecha_entrega=models.DateTimeField()
     entregado=models.BooleanField(default=False)


    
