from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import *

# Create your views here.

def agregar_reposteria(request, articulo_id):
    carro = Carro(request)
    articulo = Reposteria.objects.get(id=articulo_id):
    carro.agregar_articulo(articulo=articulo)
    return redirect("tienda")

def agregar_disfraces(request, articulo_id):
    carro = Carro(request)
    articulo = DisfracesYaccesorios.objects.get(id=articulo_id):
    carro.agregar_articulo(articulo=articulo)
    return redirect("tienda")

def agregar_descartables(request, articulo_id):
    carro = Carro(request)
    articulo = Descartables.objects.get(id=articulo_id):
    carro.agregar_articulo(articulo=articulo)
    return redirect("tienda")

def agregar_deoracion(request, articulo_id):
    carro = Carro(request)
    articulo = Decoracion.objects.get(id=articulo_id):
    carro.agregar_articulo(articulo=articulo)
    return redirect("tienda")
