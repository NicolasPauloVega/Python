# Importando el módulo models de Django
from django.db import models

# Definición del modelo Article (Artículo)
class Article(models.Model):
    # Campo para el título del artículo, como "Cómo Aprender Python Fácilmente"
    title = models.CharField(max_length=150, verbose_name="Titulo")
    # Campo para el contenido del artículo, donde escribirías el texto principal del artículo
    content = models.TextField(verbose_name="Contenido")
    # Campo para la imagen del artículo, aquí puedes subir una imagen que acompañe al artículo
    image = models.ImageField(default='null', verbose_name="imagen")
    # Campo para indicar si el artículo está disponible públicamente o no (sí o no)
    public = models.BooleanField(verbose_name="¿Publicado?")
    # Campo para la fecha y hora en que se creó el artículo
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    # Campo para la fecha de la última vez que se actualizó el artículo
    update_date = models.DateField(auto_now=True, verbose_name="Fecha actual")
    #Creamos una clase Meta
    class Meta:
        #db_table=""
        verbose_name="Articulo"
        verbose_name_plural="Articulos"
        #Ordenamos de forma ascendente los articulos
        ordering=['id']
    def __str__(self):
        if self.public:
            publico:

# Definición del modelo Category (Categoría)
class Category(models.Model):
    # Campo para el nombre de la categoría, como "Tecnología" o "Deportes"
    name = models.CharField(max_length=110, verbose_name="Nombre")
    # Campo para describir de qué se trata la categoría, por ejemplo, "Últimas novedades sobre tecnología"
    description = models.CharField(max_length=250, verbose_name="Describcion")
    # Campo para la fecha en que se creó la categoría
    create_date = models.DateField(verbose_name="Fecha de creacion")
    #creamos una clase Meta para cambiar la visualizacion (nombre) de categoria
    class Meta:
        #db_table=""
        verbose_name="Categoria"
        verbose_name_plural="Categorias"