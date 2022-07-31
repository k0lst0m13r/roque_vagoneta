from django.db import models

# Create your models here.
class Articulo(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    categoria = models.CharField(max_lengt h=50)
    imagen = models.ImageField(upload_to='articulos')

    class Meta:
        verbose_name = 'Servicio'
        verbose_name_plural = 'Servicios'

    def __str__(self):
        return self.nombre
