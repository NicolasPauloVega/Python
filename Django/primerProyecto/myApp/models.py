# Importando el módulo models de Django
from django.db import models

# Definición del modelo Article (Artículo)
class Article(models.Model):
    # Campo para el título del artículo, como "Cómo Aprender Python Fácilmente"
    title = models.CharField(max_length=150)
    # Campo para el contenido del artículo, donde escribirías el texto principal del artículo
    content = models.TextField()
    # Campo para la imagen del artículo, aquí puedes subir una imagen que acompañe al artículo
    image = models.ImageField(default='null')
    # Campo para indicar si el artículo está disponible públicamente o no (sí o no)
    public = models.BooleanField()
    # Campo para la fecha y hora en que se creó el artículo
    create_date = models.DateTimeField(auto_now_add=True)
    # Campo para la fecha de la última vez que se actualizó el artículo
    update_date = models.DateField(auto_now=True)

# Definición del modelo Category (Categoría)
class Category(models.Model):
    # Campo para el nombre de la categoría, como "Tecnología" o "Deportes"
    name = models.CharField(max_length=110)
    # Campo para describir de qué se trata la categoría, por ejemplo, "Últimas novedades sobre tecnología"
    description = models.CharField(max_length=250)
    # Campo para la fecha en que se creó la categoría
    create_date = models.DateField()