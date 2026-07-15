from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    img = models.CharField(max_length=255)
    disponivel = models.BooleanField(default=True)
    categorias = models.ManyToManyField(Categoria, blank=True)
    data = models.DateField()

    def __str__(self):
        return self.nome
