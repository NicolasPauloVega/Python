from django.shortcuts import render, HttpResponse

# Create your views here.

def hola_mundo (request):
    return HttpResponse("Hola Mundo desde Django")
def saludo (request):
    return HttpResponse("""
                        <h1>Saludo de bienvenida</h1>
                        <h2>bienvenido al SENA Tolima</h2>
                        """)
def presentacion (request):
    return HttpResponse("""
                        <h1>Identificación: </h1>
                        <h2>Nicolas Paulo Vega</h2>
                        <h2>nicolas.paulo.vega06@gmail.com</h2>
                        <h2>+57 310 207 5306</h2>
                        """)
