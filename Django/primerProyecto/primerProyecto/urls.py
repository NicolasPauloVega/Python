"""
URL configuration for primerProyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hola_mundo/', myApp.views.hola_mundo, name="hola_mundo"),
    path('saludo/', myApp.views.saludo, name="saludo"),
    path('saludo/<int:redirigir>', myApp.views.saludo, name="saludo"),
    path('presentacion/', myApp.views.presentacion, name="presentacion"),
    path('', myApp.views.index, name="index"),
    path('contacto/', myApp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>', myApp.views.contacto, name="contacto"),
    path('contacto/<str:nombre>/<str:apellido>', myApp.views.contacto, name="contacto"),
    path('productos_servicios/', myApp.views.productos_servicios, name= "productos_y_servicios"),
    path('quienes_somos/', myApp.views.quienes_somos, name="quienes_somos"),
    path('ejemplos/', myApp.views.ejemplos, name="ejemplos"),
]
