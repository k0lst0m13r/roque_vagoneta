from django.shortcuts import render, redirect
from .carro import Carro
from tienda.models import *

# Create your views here.

def agregar_articulo(request, articulo_id):
    carro = Carro(request)
    
