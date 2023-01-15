from django.db import models
import os

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre



class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='articulos')
    precio = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return self.nombre
