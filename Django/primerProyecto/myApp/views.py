from django.shortcuts import render, HttpResponse

# Create your views here.

def hola_mundo (request):
    return HttpResponse("Hola Mundo desde Django")
def saludo (request):
    return HttpResponse("""
                        <h1>Saludo de bienvenida</h1>
                        <h2>bienvenido al SENA Tolima</h2>
                        """)