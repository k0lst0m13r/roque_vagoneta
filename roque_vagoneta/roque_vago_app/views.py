from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from roque_vago_app.models import *
from django.contrib.auth import login, logout, authenticate
from .forms import *

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




####################### REGISTER, LOGIN, LOGOUT ###################

def log_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
        else:
            return redirect('login')
    form =  AuthenticationForm()
    ctx = {"form": form}
    return render(request, 'roque_vago_app/login.html',ctx)

def registro(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            form.save()
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')

            return redirect('index')

        return render(request, 'roque_vago_app/registro.html', {"form": form})


    else:
        form = UserRegisterForm()
    return render(request, 'roque_vago_app/registro.html', {"form": form})


def log_out(request):
    logout(request)
    return redirect('index')



################## PERFIL #################

@login_required
def perfil(request):
    if request.user.is_authenticated:
        return render(request, 'roque_vago_app/perfil.html',)

@login_required
def editar_perfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            usuario.username = info['username']
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']

            usuario.save()

            return redirect('perfil')
    else:
        form = UserEditForm(initial={'username': usuario.username, 'email':usuario.email, 'first_name':usuario.first_name, 'last_name': usuario.last_name,})

    ctx = {'form': form,}
    return render(request, 'roque_vago_app/editar_perfil.html', ctx)
