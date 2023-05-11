"""
    URL configuration for sistema_coder_entregable project.

    The `urlpatterns` list routes URLs to views. For more information please see:
        https://docs.djangoproject.com/en/4.2/topics/http/urls/
    Examples:
    Function views
        1. Add an import:  from my_app import views
        2. Add a URL to urlpatterns:  path('', views.home, name='home')
    Class-based views
        1. Add an import:  from other_app.views import Home
        2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
    Including another URLconf
        1. Import the include() function: from django.urls import include, path
        2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
 """
from sistema_coder_entregable.views import *
from django.contrib import admin

from django.urls import path
from control_estudios.views import *

urlpatterns = [
    path('estudiantes/', listar_estudiantes, name="lista_estudiantes"),
    path('cursos/', listar_cursos, name="lista_cursos"),
    path('profesores/', listar_profesores, name="lista_profesores"),
    path('entregables/', listar_entregables, name="lista_entregables"),
    path('crear-curso/', crear_curso, name="crear_curso"),
    path('crear-estudiante/', crear_estudiante, name="crear_estudiante"),
    path('crear-profesor/', crear_profesor, name="crear_profesor"),
    path('crear-entregable/', crear_entregable, name="crear_entregable"),
    path('buscar-cursos/', buscar_cursos, name="buscar_cursos"),
]