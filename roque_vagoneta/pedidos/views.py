from django.shortcuts import render, redirect
from .models import Pedido, DetallePedido
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from carro.carro import Carro



# Create your views here.

##def importe_total(request):
    
  ##  global total
    ##if request.user.is_authenticated:
      ##   for key, value in request.session["carro"].items():
        ##    total = total + float(value["precio"])
            
    ##return total 
    

total = 0
def enviar_pedido(request):
    pedido = Pedido.objects.create(user=request.user)
    carro = Carro(request)
    detalle_pedido = list()
    
    for key, value in carro.carro.items():
        detalle_pedido.append(DetallePedido(
            
            articulo_id = key,         
            cantidad = value["cantidad"],
            user = request.user,
            pedido = pedido, 
                   
        ))
    
    DetallePedido.objects.bulk_create(detalle_pedido)
    
    def importe_total(request):
    
        global total
        if request.user.is_authenticated:
             for key, value in request.session["carro"].items():
                total = total + float(value["precio"])
            
        return total
       
    enviar_mail(
        
        pedido = pedido,
        detalle_pedido = detalle_pedido,
        usuario = request.user.username,
        email_usuario = request.user.email,
        importe = importe_total(request)
        
    )
    messages.success(request, "Envío exitoso!! Nos comunicaremos a la brevedad para combinar Entrega y Forma de pago")
    return redirect("index")

def enviar_mail(**kwargs):
    
    asunto = "Pedido Roque Vagoneta"
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": kwargs.get("pedido"),
        "detalle_pedido": kwargs.get("detalle_pedido"),
        "usuario": kwargs.get("usuario"),
        "email_usuario": kwargs.get("email_usuario"),
        "importe": kwargs.get("importe"),
    })
    
    texto_mensaje = strip_tags(mensaje)
    from_email = "roquevagoweb@gmail.com"
    to = kwargs.get("email_usuario")
    
    send_mail(asunto, texto_mensaje, from_email, [to], html_message=mensaje)