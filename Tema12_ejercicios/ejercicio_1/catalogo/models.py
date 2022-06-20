from django.db import models
from django.urls import reverse

class Directores(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.id)])

    def __str__(self) -> str:
        return '%s  %s' % (self.first_name, self.last_name)

class Movies(models.Model):
    title = models.CharField(max_length=32)
    director = models.ForeignKey("Directores", on_delete=models.SET_NULL, null=True)  # Relaciona la tabla Book con otra tabla Author
    summary = models.TextField(max_length=350, help_text='Da una breve descripcion de la Pelicula')
    
    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.id)])
