from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'roque_vago_app/home.html')

def tienda(request):
    return render(request,'roque_vago_app/tienda.html')

def contacto(request):
    return render(request, 'roque_vago_app/contacto.html')
