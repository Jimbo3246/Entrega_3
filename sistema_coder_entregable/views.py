from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
def inicio(request):
    contexto={}
    http_responde = render(
        request=request,
        template_name='control_estudios/index.html',
        context=contexto,
    )
    return http_responde

def saludar(request):
    saludo="Hola amigos"
    pagina_html=HttpResponse(saludo)
    return pagina_html
def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo=f"Hola amigos {hoy.day}/{hoy.month}/{hoy.year}"
    pagina_html=HttpResponse(saludo)
    return pagina_html
def saludar_con_html(request):
    contexto={}
    http_responde=render(
        request=request,
        template_name='control_estudios/base.html',
        context=contexto,
    )
    return http_responde
