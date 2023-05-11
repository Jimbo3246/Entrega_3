from django.shortcuts import render, redirect
from control_estudios.models import *
from control_estudios.forms import *
from django.urls import reverse


# Create your views here.
def listar_estudiantes(request):
    contexto={
        "estudiantes":Estudiante.objects.all(),
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_responde
def listar_cursos(request):

    contexto={
        "cursos": Curso.objects.all(),       
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_responde
def listar_profesores(request):
    contexto={
        "profesores": Profesor.objects.all(),       
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/lista_profesores.html',
        context=contexto,
    )
    return http_responde
def listar_entregables(request):
    contexto={
        "entregables": Entregable.objects.all(),       
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/lista_entregables.html',
        context=contexto,
    )
    return http_responde
def crear_curso(request):
    if request.method == "POST":
       formulario = CursoFormulario(request.POST)
       if formulario.is_valid():
           data=formulario.cleaned_data #es diccionario
           nombre = data["nombre"]
           comision=data["comision"]
           curso = Curso(nombre=nombre, comision=comision)#lo crean solo en el RAM
           curso.save()# Loguardan en la base de datos

           url_exitosa = reverse('lista_cursos')
           return redirect(url_exitosa)            
    else: #GET
        formulario =CursoFormulario(initial=request.POST)
        http_response = render(
            request=request,
            template_name='control_estudios/formulario_curso.html',
            context={'formulario': formulario}
        )
    return http_response
def listar_entregables(request):
    contexto={
        "entregables": Entregable.objects.all(),       
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/lista_entregables.html',
        context=contexto,
    )
    return http_responde

def crear_estudiante(request):
    if request.method == "POST":
       formulario = EstudianteFormulario(request.POST)
       if formulario.is_valid():
           data=formulario.cleaned_data #es diccionario
           nombre = data["nombre"]
           apellido=data["apellido"]
           email=data["email"]
           estudiante = Estudiante(nombre=nombre, apellido=apellido , email=email)#lo crean solo en el RAM
           estudiante.save()# Loguardan en la base de datos
           url_exitosa = reverse('lista_estudiantes')
           return redirect(url_exitosa)            
    else: #GET
        formulario =EstudianteFormulario(initial=request.POST)
        http_response = render(
            request=request,
            template_name='control_estudios/formulario_estudiante.html',
            context={'formulario': formulario}
        )
    return http_response
def crear_profesor(request):
    if request.method == "POST":
       formulario = ProfesorFormulario(request.POST)
       if formulario.is_valid():
           data=formulario.cleaned_data #es diccionario
           nombre = data["nombre"]
           apellido=data["apellido"]
           profesion=data["profesion"]
           email=data["email"]
           profesion = Profesor(nombre=nombre, apellido=apellido ,profesion=profesion, email=email)#lo crean solo en el RAM
           profesion.save()# Loguardan en la base de datos
           url_exitosa = reverse('lista_profesores')
           return redirect(url_exitosa)            
    else: #GET
        formulario =ProfesorFormulario(initial=request.POST)
        http_response = render(
            request=request,
            template_name='control_estudios/formulario_profesor.html',
            context={'formulario': formulario}
        )
    return http_response
def crear_entregable(request):
    if request.method == "POST":
       formulario = EntregableFormulario(request.POST)
       if formulario.is_valid():
           data=formulario.cleaned_data #es diccionario
           nombre = data["nombre"]
           fecha_entrega=data["fecha_entrega"]
           entregado=data["entregado"]         
           entregable = Entregable(nombre=nombre, fecha_entrega=fecha_entrega ,entregado=entregado)#lo crean solo en el RAM
           entregable.save()# Lo guardan en la base de datos
           url_exitosa = reverse('lista_entregables')
           return redirect(url_exitosa)            
    else: #GET
        formulario =EntregableFormulario(initial=request.POST)
        http_response = render(
            request=request,
            template_name='control_estudios/formulario_entregable.html',
            context={'formulario': formulario}
        )
    return http_response

def buscar_cursos(request):
    if request.method =="POST":
        data = request.POST
        busqueda = data["busqueda"]
        cursos =Curso.objects.filter(comision__contains=busqueda)
        contexto={
            "cursos":cursos,
        }
        http_response = render(
            request=request,
            template_name='control_estudios/lista_cursos.html',
            context=contexto,
        )
        return http_response
    
