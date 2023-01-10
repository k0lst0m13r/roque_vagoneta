from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import *
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.

#------------------AGREGAR AL CARRO-----------------

def agregar_articulo(request, articulo_id):
    carro = Carro(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carro.agregar(articulo=articulo)
    return redirect("carrito")


#---------------------ELIMINAR DEL CARRO-------------------

def eliminar_articulo(request, articulo_id):
    carro = Carro(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carro.eliminar(articulo=articulo)
    return redirect("carrito")


#--------------------SACAR DEL CARRO----------------

def sacar_articulo(request, articulo_id):
    carro = Carro(request)
    articulo = Articulo.objects.get(id=articulo_id)
    carro.sacar(articulo=articulo)
    return redirect("carrito")



#---------------VACIAR EL CARRO-----------------------

def vaciar_carro(request, articulo_id):
    carro = Carro(request)
    carro.vaciar_carro()
    return redirect("tienda")



