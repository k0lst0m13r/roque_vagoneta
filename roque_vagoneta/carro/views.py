from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import *

# Create your views here.

#------------------AGREGAR AL CARRO-----------------

def agregar_reposteria(request, articulo_id):
    carro = Carro(request)
    articulo = Reposteria.objects.get(id=articulo_id)
    carro.agregar_articulo(articulo=articulo)
    return redirect("tienda")

def agregar_disfraces(request, articulo_id):
    carro = Carro(request)
    articulo = DisfracesYaccesorios.objects.get(id=articulo_id)
    carro.agregar_articulo(articulo=articulo)
    return redirect("tienda")

def agregar_descartables(request, articulo_id):
    carro = Carro(request)
    articulo = Descartables.objects.get(id=articulo_id)
    carro.agregar_articulo(articulo=articulo)
    return redirect("tienda")

def agregar_decoracion(request, articulo_id):
    carro = Carro(request)
    articulo = Decoracion.objects.get(id=articulo_id)
    carro.agregar_articulo(articulo=articulo)
    return redirect("tienda")


#---------------------ELIMINAR DEL CARRO-------------------

def eliminar_reposteria(request, articulo_id):
    carro = Carro(request)
    articulo = Reposteria.objects.get(id=articulo_id)
    carro.eliminar_articulo(articulo=articulo)
    return redirect("tienda")

def eliminar_disfraces(request, articulo_id):
    carro = Carro(request)
    articulo = DisfracesYaccesorios.objects.get(id=articulo_id)
    carro.eliminar_articulo(articulo=articulo)
    return redirect("tienda")

def eliminar_descartables(request, articulo_id):
    carro = Carro(request)
    articulo = Descartables.objects.get(id=articulo_id)
    carro.eliminar_articulo(articulo=articulo)
    return redirect("tienda")

def eliminar_decoracion(request, articulo_id):
    carro = Carro(request)
    articulo = Decoracion.objects.get(id=articulo_id)
    carro.eliminar_articulo(articulo=articulo)
    return redirect("tienda")


#--------------------SACAR DEL CARRO----------------

def sacar_reposteria(request, articulo_id):
    carro = Carro(request)
    articulo = Reposteria.objects.get(id=articulo_id)
    carro.sacar_articulo(articulo=articulo)
    return redirect("tienda")

def sacar_disfraces(request, articulo_id):
    carro = Carro(request)
    articulo = DisfracesYaccesorios.objects.get(id=articulo_id)
    carro.sacar_articulo(articulo=articulo)
    return redirect("tienda")

def sacar_descartables(request, articulo_id):
    carro = Carro(request)
    articulo = Descartables.objects.get(id=articulo_id)
    carro.sacar_articulo(articulo=articulo)
    return redirect("tienda")

def sacar_decoracion(request, articulo_id):
    carro = Carro(request)
    articulo = Decoracion.objects.get(id=articulo_id)
    carro.sacar_articulo(articulo=articulo)
    return redirect("tienda")


#---------------VACIAR CARRO-----------------------

def vaciar_carro(request, articulo_id):
    carro = Carro(request)
    carro.vaciar_carro()
    return redirect("tienda")
