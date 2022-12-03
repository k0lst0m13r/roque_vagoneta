from django.db import models
from django.contrib.auth import get_user_model
from tienda.models import Articulo
from django.db.models import F, Sum, FloatField
# Create your models here.

User = get_user_model()

class Pedido(models.Model):

    user = models.Foreign.Key(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.id
    
    @property
    def total(self):
        return self.detallearticulos_set.aggregate(
            
            total = Sum(F("precio")*F("cantidad"), output_FloadField()) 
            
        )["total"]
    
    
    class Meta:
        db_table = "pedidos"
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ["id"]
        
        
class DetalleArticulos(models.Model):
    
    user = models.Foreign.Key(User, on_delete=models.CASCADE)  
    articulo_id = models.Foreign.Key(Articulo, on_delete=models.CASCADE)
    pedido_id = models.Foreign.Key(Pedido, on_delete=models.CASCADE)
    cantidad = models.IntgerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.cantidad}{self.articulo_id.nombre}'
    
    class Meta:
        db_table = 'detallearticulos'
        vervose_name = 'Detalle Articulos'
        ordering = ["id"]
    
    