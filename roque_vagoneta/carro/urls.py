from django.urls import path
from .import views

app_name ="carro"

urlpatterns = [

  path("agregar/<int:articulo_id>/", views.agregar_articulo, name='agregar'),
  path("eliminar/<int:articulo_id>/", views.eliminar_articulo, name='eliminar'),
  path("sacar/<int:articulo_id>/", views.sacar_articulo, name='sacar'),
  path("vaciar_carro/", views.vaciar_carro, name='vaciar'),
  
]
