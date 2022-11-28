from django.shortcuts import render
from .models import *

# Create your views here.
def tienda(request):

    articulos = Articulo.objects.all()


    ctx = {"articulos": articulos}
    return render(request,'tienda/tienda.html', ctx)
