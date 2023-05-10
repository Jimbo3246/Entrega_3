from django.shortcuts import render

# Create your views here.
def listar_estudiantes(request):
    contexto={
        "estudiantes": [
        {"nombre":"Jenifer", "apellido":"Bujele"},
        {"nombre":"Ibonne", "apellido":"Tenorio"},
        {"nombre":"Roxana", "apellido":"Prince"},
        {"nombre":"Katy", "apellido":"Salas"},
        ]
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/lista_estudiantes.html',
        context=contexto,
    )
    return http_responde
def listar_cursos(request):
    contexto={
        "cursos": [
        {"nombre":"Bases geometricas del diseño", "comision":"101"},
        {"nombre":"Macroeconomia", "comision":"401"},
        {"nombre":"Fisicoquimica", "comision":"402"},
        {"nombre":"Dibujo asistido por computadora", "comision":"501"},
        ]
    }
    http_responde = render(
        request=request,
        template_name='control_estudios/lista_cursos.html',
        context=contexto,
    )
    return http_responde