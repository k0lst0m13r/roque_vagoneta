from django.db import models

# Create your models here.
class Reposteria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='articulos')
    precio = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Reposteria'
        verbose_name_plural = 'Reposteria'

    def __str__(self):
        return self.nombre

class DisfracesYaccesorios(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='articulos')
    precio = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Disfraces Y Accesorios'
        verbose_name_plural = 'Disfraces Y Accesorios'

    def __str__(self):
        return self.nombre


class Descartables(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='articulos')
    precio = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Descartables'
        verbose_name_plural = 'Descartables'

    def __str__(self):
        return self.nombre

class Decoracion(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='articulos')
    precio = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Decoracion'
        verbose_name_plural = 'Decoracion'

    def __str__(self):
        return self.nombre

class Cumpleanios(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='articulos')
    precio = models.DecimalField(max_digits=7, decimal_places=2, default=0.00)

    class Meta:
        verbose_name = 'Cumpleaños'
        verbose_name_plural = 'Cumpleaños'

    def __str__(self):
        return self.nombre
