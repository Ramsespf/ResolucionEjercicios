from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count()  #cuenta todos los libros esta es la sintaxis de django
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.all().count()

    disponibles = BookInstance.objects.filter(status__exact='a').count() # Si vamos al modelo d esta forma se filtra 

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_authors': num_authors,
            'disponibles': disponibles,
            'num_instance': num_instances
        }
    )
