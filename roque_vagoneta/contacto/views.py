from django.shortcuts import render, redirect
from .forms import ContactoForm
from  django.core.mail import EmailMessage
# Create your views here.
def contacto(request):

    formulario = ContactoForm()

    if request.method=="POST":
        formulario = ContactoForm()
        if formulario.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            consulta = request.POST.get("consulta")

            email = EmailMessage("Consulta desde Roque Vagoneta",
                                 "Nombre: {} Email: {} Consulta: {}".format(nombre,email,consulta),
                                 "",["bansuri.indostanico@gmail.com"],reply_to[email])
            try:
                email.send()
                return render(request, 'contacto/respuesta.html')
            except:
                return render(request, 'contacto/respuesta.html')

    ctx = {'formulario': formulario}
    return render(request, 'contacto/contacto.html', ctx)


def respuesta(request):
    return render(request, 'contacto/respuesta.html')
