from django.shortcuts import render, HttpResponse
from roque_vago_app.models import *

# Create your views here.
def index(request):
    return render(request, 'roque_vago_app/index.html')

def tienda(request):
    articulos = Articulo.objects.all()
    ctx = {'articulos': articulos}
    return render(request,'roque_vago_app/tienda.html', ctx)

def contacto(request):
    return render(request, 'roque_vago_app/contacto.html')
