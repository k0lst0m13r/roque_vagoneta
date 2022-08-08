from django.shortcuts import render, HttpResponse
from roque_vago_app.models import *

# Create your views here.
def index(request):
    return render(request, 'roque_vago_app/index.html')

def tienda(request):

    reposteria = Reposteria.objects.all()

    disfraces = DisfracesYaccesorios.objects.all()

    descartables = Descartables.objects.all()

    decoracion = Decoracion.objects.all()

    cumple = Cumpleanios.objects.all()

    
    ctx = {'cumple': cumple, 'reposteria': reposteria, 'disfraces': disfraces, 'descartables': descartables, 'decoracion': decoracion,}
    return render(request,'roque_vago_app/tienda.html', ctx)
