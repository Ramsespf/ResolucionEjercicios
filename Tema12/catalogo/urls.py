from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index') #'r^$' es para q muestro todo lo q sea /catalogo/ en la pagina web
]