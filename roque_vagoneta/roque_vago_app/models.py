from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    categoria = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='articulos')
    precio = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'

    def __str__(self):
        return self.nombre
