from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre =models.CharField(max_length=64)
    comision =models.IntegerField()
    def __str__(self):
        return f"{self.nombre} | {self.comision}"

class Persona(models.Model):
    apellido =models.CharField(max_length=256)
    nombre =models.CharField(max_length=256)
    email= models.EmailField(blank=True)
    class Meta:
        abstract=True

class Profesor(Persona):
    profesion=models.CharField(max_length=256)
    def __str__(self):
        return f"{self.nombre}  {self.apellido} | {self.profesion}"

class Estudiante(Persona):
    def __str__(self):
        return f"{self.nombre}  {self.apellido}" 
    
class Entregable(models.Model):
     nombre =models.CharField(max_length=256)
     fecha_entrega=models.DateTimeField()
     entregado=models.BooleanField(default=False)
     def __str__(self):
        return f"{self.nombre} | {self.fecha_entrega}" 


    
