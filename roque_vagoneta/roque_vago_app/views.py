from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'roque_vago_app/index.html')

def tienda(request):
    return render(request,'roque_vago_app/tienda.html')

def contacto(request):
    return render(request, 'roque_vago_app/contacto.html')
