from django.shortcuts import render, HttpResponse

# Create your views here.

layout = """
        <h1>Sitio web con Django | Nicolas Paulo Vega</h1>
        </hr>
        <ul>
            <li>
                <a href="/hola_mundo">Hola Mundo</a>
            </li>
            <li>
                <a href="/saludo">Saludo</a>
            </li>
            <li>
                <a href="/presentacion">Presentacion</a>
            </li>
            <li>
                <a href="/">Inicio</a>
            </li>
        </ul>
        """


def hola_mundo (request):
    return HttpResponse(layout+"Hola Mundo desde Django")
def saludo (request):
    return HttpResponse(layout+"""
                        <h1>Saludo de bienvenida</h1>
                        <h2>bienvenido al SENA Tolima</h2>
                        """)
def presentacion (request):
    return HttpResponse(layout+"""
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
    template += """</ul><hr>"""

    
    template += """
                    <h1>Años biciestos</h1>
                    <ul>
                """
    year1 = 2024
    while year1 <= 2050:
        if year1 % 4 == 0:
            template += f"<li>{str(year1)}</li>"
        year1 += 1
    template += """</ul><hr>"""

    template += """
                <h1>Años pares</h1>
                <ul>
                """
    year2 = 2024
    while year2 <= 2050:
        if year2 % 2 == 0:
            template += f"<li>{str(year2)}</li>"
        year2 += 1
    template += """</ul><hr>"""

    return HttpResponse(layout+template)