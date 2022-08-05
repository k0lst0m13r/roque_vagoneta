from django.shortcuts import render, HttpResponse
from roque_vago_app.models import *

# Create your views here.
def index(request):
    return render(request, 'roque_vago_app/index.html')

def tienda(request):

    articulos = Reposteria.objects.all()
    ctx = {'articulos': articulos}
    return render(request,'roque_vago_app/tienda.html', ctx)

    articulos = DisfracesYaccesorios.objects.all()
    ctx = {'articulos': articulos}
    return render(request,'roque_vago_app/tienda.html', ctx)

    articulos = Descartables.objects.all()
    ctx = {'articulos': articulos}
    return render(request,'roque_vago_app/tienda.html', ctx)

    articulos = Decoracion.objects.all()
    ctx = {'articulos': articulos}
    return render(request,'roque_vago_app/tienda.html', ctx)

    articulos = Cumpleanios.objects.all()
    ctx = {'articulos': articulos}
    return render(request,'roque_vago_app/tienda.html', ctx)
