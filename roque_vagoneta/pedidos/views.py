from django.shortcuts import render
from .models import Pedido, DetallePedido
from django.contrib import messages

# Create your views here.

def enviar_pedido():
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    detalle_pedido = list()
    for key, value in carro.carro.items():
        detalle_pedido.append(DetallePedido(
            
            articulo_id = key,         
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido 
                   
        ))
    
    DetallePedido.objects.bulk_create(detalle_pedido)
    
    enviar_mail(
        
        pedido = pedido,
        detalle_pedido = detalle_pedido,
        usuario = requet.username,
        email_usuario = request.usermail
        
    )
    messages.success(request, "Envío exitoso!! Nos comunicaremos a la brevedad para combinar Entrega y Forma de pago")
    return redirect("../tienda")