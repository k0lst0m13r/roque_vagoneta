"""roque_vagoneta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from roque_vago_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('login', views.log_in, name='login'),
    path('logout', views.log_out, name='logout'),
    path('registro', views.registro, name="registro"),
    path('perfil',views.perfil, name="perfil"),
    path('editar_perfil',views.editar_perfil, name="editar_perfil"),
    path('contacto', views.contacto, name="contacto"),


    path("tienda", include("tienda.urls")),
    path("carro", include("carro.urls")),
    path("pedidos", include("pedidos.urls")),
    ]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
