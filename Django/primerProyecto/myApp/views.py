from django.shortcuts import render, HttpResponse, redirect
from myApp.models import Article

# Create your views here.

# Definiendo la vista 'hola_mundo'
def hola_mundo(request):
    # Renderiza la plantilla 'hola_mundo.html' y la retorna como respuesta
    return render(request, 'hola_mundo.html')


# Definiendo la vista 'saludo'
def saludo(request, redirigir=0):
    # Lista de nombres
    nombres = ['Nicolas', 'Andres']
    
    # Verificando si se debe redirigir a la vista 'contacto'
    if redirigir == 1:
        # Redirigiendo a la vista 'contacto' con los parámetros especificados
        return redirect('contacto', nombre="Ana", apellido="Cruz")
    
    # Si no se debe redirigir, renderiza la plantilla 'saludo.html' con los nombres
    return render(request, 'saludo.html', {'texto': '', 'names': nombres})

# Definiendo la vista 'presentacion'
def presentacion(request):
    # Renderiza la plantilla 'presentacion.html' y la retorna como respuesta
    return render(request, 'presentacion.html')

# Definiendo la vista 'index'
def index (request):
    #Se crea una variable que almacene la informacion que se quiere poner en la pagina.
    # """template = ""
    #                 <h1>Inicio</h1>
    #                 <p>Años desde el 2024 hasta 2050</p>
    #                  <ul>
    #              """
    # #Se crea una variable que almacene el año 2024
    # year=2024
    # #se crea una lista a cual se actualizara cada vez que se entre
    # while year <= 2050:
    #     template += f"<li> {str(year)} </li>"
    #     year += 1
    # template += """</ul><hr>"""

    
    # template += """
    #                 <h1>Años biciestos</h1>
    #                 <ul>
    #             """
    # year1 = 2024
    # while year1 <= 2050:
    #     if year1 % 4 == 0:
    #         template += f"<li>{str(year1)}</li>"
    #     year1 += 1
    # template += """</ul><hr>"""

    # template += """
    #             <h1>Años pares</h1>
    #             <ul>
    #             """
    # year2 = 2024
    # while year2 <= 2050:
    #     if year2 % 2 == 0:
    #         template += f"<li>{str(year2)}</li>"
    #     year2 += 1
    # template += """</ul><hr>"""

    # Se define una lista de años desde 2024 hasta 2050
    year = 2024
    hasta = range(year,2051)

    # Se define un nombre
    nombre = 'Nicolas Paulo Vega'

    # Se pasan los datos a la plantilla 'index.html'
    return render(request, 'index.html', {
        'mi_variable': 'soy un dato que esta en la vista',
        'title': 'Inicio del sitio',
        'titulo': 'Página de Inicio',
        'name': nombre,
        'years': hasta,
    })


# Definiendo la vista 'contacto'
def contacto(request, nombre="", apellido=""):
    # Inicializando una cadena vacía para almacenar información del aprendiz
    aprendiz = ""
    
    # Comprobando si se proporcionaron valores para nombre y apellido
    if nombre and apellido:
        # Si se proporcionaron ambos, se agrega un encabezado con ambos nombres
        aprendiz += f"<h3>{nombre} {apellido}</h3>"
    elif nombre:
        # Si solo se proporcionó el nombre, se agrega un encabezado con el nombre solamente
        aprendiz += f"<h2>Nombre: {nombre}</h2>"
    elif apellido:
        # Si solo se proporcionó el apellido, se agrega un encabezado con el apellido solamente
        aprendiz += f"<h2>Apellido: {apellido}</h2>"
    else:
        # Si no se proporcionaron ni nombre ni apellido, se muestra un mensaje indicando su ausencia
        aprendiz += f"<h2>Nombre y Apellido inexistente</h2>"

    # Retorna la plantilla 'contacto.html', pasando la información del aprendiz
    return render(request, 'contacto.html')


# Definiendo la vista 'quienes_somos'
def quienes_somos(request):
    # Renderiza la plantilla 'qs.html' y la retorna como respuesta
    return render(request, 'qs.html')

# Definiendo la vista 'productos_servicios'
def productos_servicios(request):
    # Renderizando la plantilla 'pys.html'
    return render(request, 'pys.html')

# Definiendo la vista 'ejemplos'
def ejemplos(request):
    # Creando una lista vacía llamada 'nombres'
    nombres = []
    
    # Retornando la plantilla 'ejemplos.html' con diferentes datos
    return render(request, 'ejemplos.html', {
        # Lista de nombres
        'lista': ["Nicolas P.", "Juan Carlo P.","2", "Sara V.", "Maria Alejandra R."],
        # Rango de números del 1 al 10
        'numeros': range(1, 11),
        # Lista vacía 'nombres'
        'nombres': nombres,
        # Lista de valores [1, 2, 3]
        'value': [1, 2, 3],
        # Dirección de correo electrónico
        'correoE': "nicolas. paulo. vega. 06 @ gmail. com",
        # Número divisible
        'divisible': 30,
        # Cadena de caracteres
        'letras': "Hola mundo!!",
        # Lista de nombres de aprendices
        'aprendices': ["Juan Diego","Mathew Guarnizo","Maria Fernanda","Nicolas Paulo","Miguel Angel","Maicol Esteban","Kevin Londoño","Marlon","Maria Jose","Nataly"],
    })

# Definiendo la vista 'crear_articulo'
def crear_articulo(request, title, content, public):
    # Crear una instancia de Article con los datos proporcionados
    articulo = Article(
        title=title,
        content=content,
        public=public,
    )
    # Guardar el artículo en la base de datos
    articulo.save()
    
    # Retornar una respuesta con los detalles del artículo creado
    return HttpResponse(f"Aticulo creado: {articulo.title} - {articulo.content}")

# Definiendo la vista 'articulo'
def articulo(request):
    try:
        # Intenta obtener un artículo con unos parametros desde la base de datos
        articulo = Article.objects.get(pk=4, public=False)
        
        # Si se encuentra el artículo, construye una respuesta con los detalles del artículo
        response = f"Articulo creado: {articulo.title} - {articulo.content} - Estado:{articulo.public}"
    
    except:
        # Si hay una excepción (por ejemplo, si no se encuentra el artículo), construye una respuesta de error
        response = "<h1><strong>Articulo no encontrado</strong></h1>"

    # Retorna la respuesta, ya sea los detalles del artículo o un mensaje de error
    return HttpResponse(response)

#Definiendo la vista 'editar_articulo'
def editar_articulo(request,id):
    #Intenta obtener un articulo basado en unos parametros desde la base de datos
    articulo= Article.objects.get(pk=id)
    #se actualizan los datos de title,content y public
    articulo.title="El principito"
    articulo.content="Cuento de planetas"
    articulo.public=False
    #se guardan los cambios
    articulo.save()
    #se muestra en la pantalla
    return HttpResponse(f"El articulo {articulo.id} de nombre: {articulo.title} ha sido actualizado, su descripcion es: {articulo.content} y su estado es: {articulo.public}")

#Definiendo la vista 'articulos'
def articulos(request):
    #guardar todos los objetos (registros) de article.
    articulos = Article.objects.order_by('id')
    articulos = Article.objects.filter(public = True, id=1)
    #Lookups en Django
    articulos = Article.objects.filter(title__contains = "media") #Búsqueda de artículos cuyo título contiene la palabra "media" de forma case-sensitive.
    articulos = Article.objects.filter(title__exact = "Divina comedia") #Búsqueda de artículos cuyo título es exactamente "Divina comedia".
    articulos = Article.objects.filter(title__iexact = "divina comedia") #Búsqueda de artículos cuyo título es exactamente "divina comedia", ignorando mayúsculas y minúsculas.
    articulos = Article.objects.filter(id__gte=1) #Búsqueda de artículos cuyo ID es mayor o igual a 1.
    articulos = Article.objects.filter(id__lt=5) #Búsqueda de artículos cuyo ID es menor que 5.
    articulos = Article.objects.filter(id__in=[1,6,8]) #Búsqueda de artículos cuyos IDs están en la lista [1, 6, 8].
    #Enviando la informacion a el template articulos
    return render(request, 'articulos.html',{
        'articulos':articulos
    })

def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    return redirect('Listar')