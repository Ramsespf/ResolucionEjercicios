from django.shortcuts import render

# Create your views here.
from .models import Directores, Movies

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    num_directores=Directores.objects.all().count()
    num_movies=Movies.objects.all().count()
    directores = Directores.objects.all()
    directores_format = f'{directores[0]}, {directores[1]}, {directores[2]}'
    

    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
        context={
            'num_directores':num_directores,
            'num_movies':num_movies,
            'directores': directores_format
        }
    )

def director(request):
    """
    Función vista para la página Directores del sitio.
    """
    # Genera contadores de algunos de los objetos principales
    directores = Directores.objects.all()    
    directores_format = f'{directores[0]}, {directores[1]}, {directores[2]}'
    movies_director = Movies.objects.all()
    
    

    # Renderiza la plantilla HTML director.html con los datos en la variable contexto
    return render(
        request,
        'director.html',
        context={            
            'movies_director':movies_director,
            'directores': directores_format,
            
        }
    )

def movies(request):
    """
    Función vista para la página Movies del sitio.
    """
    movies_format = ''
    movies = Movies.objects.all()
    movies_list = list(movies)
    for i in movies_list:
        movies_format += ', ' + str(i)
    
    

    # Renderiza la plantilla HTML movies.html con los datos en la variable contexto
    return render(
        request,
        'movies.html',
        context={            
            'movies_format':movies_format,
            
            
        }
    )