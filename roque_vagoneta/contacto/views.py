from django.shortcuts import render
from .forms import ContactoForm

# Create your views here.
def contacto(request):

    formulario = ContactoForm()

    ctx = {'formulario': formulario}
    return render(request, 'contacto/contacto.html', ctx)
