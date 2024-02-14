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
def index (request):
    #Se crea una variable que almacene la informacion que se quiere poner en la pagina.
    template = """
                        <h1>Inicio</h1>
                        <p>Años desde el 2024 hasta 2050</p>
                        <ul>
                        """
    #Se crea una variable que almacene el año 2024
    year=2024
    #se crea una lista a cual se actualizara cada vez que se entre
    while year <= 2050:
        template += f"<li> {str(year)} </li>"
        year += 1
    """</ul><hr>"""

    if year % 4 != 0:
        print("No es bisiesto")
    elif year % 4 == 0 and year % 100 == 0 or year % 400 == 0:
        print("Es un año bisiento")

    
    return HttpResponse(template)

