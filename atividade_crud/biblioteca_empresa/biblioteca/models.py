from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=255) # campo de texto para o título
    autores = models.CharField(max_length=255)  # campo de texto para os autores
    ano = models.CharField(max_length=255)  # Campo de texto para o ano de publicação

    def __str__(self):
        return self.titulo # Mostra o título como nome do objeto no admin
    
    class Meta:
        verbose_name_plural = "Livros" # plural correto no Django Admin