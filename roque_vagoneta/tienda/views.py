from django.shortcuts import render
from tienda.models import *

# Create your views here.
def tienda(request):

    reposteria = Reposteria.objects.all()

    disfraces = DisfracesYaccesorios.objects.all()

    descartables = Descartables.objects.all()

    decoracion = Decoracion.objects.all()

    cumple = Cumpleanios.objects.all()


    ctx = {'cumple': cumple, 'reposteria': reposteria, 'disfraces': disfraces, 'descartables': descartables, 'decoracion': decoracion,}
    return render(request,'tienda/tienda.html', ctx)
