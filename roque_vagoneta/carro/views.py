from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import *

# Create your views here.

#------------------AGREGAR AL CARRO-----------------

def agregar_articulo(request, articulo_id):
    carro = Carro(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carro.agregar(articulo=articulo)
    return redirect("tienda")


#---------------------ELIMINAR DEL CARRO-------------------

def eliminar_articulo(request, articulo_id):
    carro = Carro(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carro.eliminar(articulo=articulo)
    return redirect("tienda")


#--------------------SACAR DEL CARRO----------------

def sacar_articulo(request, articulo_id):
    carro = Carro(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carro.sacar(articulo=articulo)
    return redirect("tienda")



#---------------VACIAR EL CARRO-----------------------

def vaciar_carro(request, articulo_id):
    carro = Carro(request)
    carro.vaciar_carro()
    return redirect("tienda")
