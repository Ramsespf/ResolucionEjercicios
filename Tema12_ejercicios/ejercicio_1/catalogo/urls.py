from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^catalogo/$', views.director, name='director'),
    re_path(r'^catalogo/movies/$', views.movies, name='movies'),
]