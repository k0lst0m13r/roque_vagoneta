from django.urls import path
from .import views

app_name ="carro"

urlpatterns = [

  path("agregar_reposteria/int:articulo_id/", views.agregar_reposteria, name='agregar_reposteria'),
  path("agregar_disfraces/int:articulo_id/", views.agregar_disfraces, name='agregar_disfraces'),
  path("agregar_descartables/int:articulo_id/", views.agregar_descartables, name='agregar_descartables'),
  path("agregar_decoracion/int:articulo_id/", views.agregar_decoracion, name='agregar_decoracion'),

  path("eliminar_reposteria/int:articulo_id/", views.eliminar_reposteria, name='eliminar_reposteria'),
  path("eliminar_disfraces/int:articulo_id/", views.eliminar_disfraces, name='eliminar_disfraces'),
  path("eliminar_descartables/int:articulo_id/", views.eliminar_descartables, name='eliminar_descartables'),
  path("eliminar_decoracion/int:articulo_id/", views.eliminar_decoracion, name='eliminar_decoracion'),

  path("sacar_reposteria/int:articulo_id/", views.sacar_reposteria, name='sacar_reposteria'),
  path("sacar_disfraces/int:articulo_id/", views.sacar_disfraces, name='sacar_disfraces'),
  path("sacar_descartables/int:articulo_id/", views.sacar_descartables, name='sacar_descartables'),
  path("sacar_decoracion/int:articulo_id/", views.sacar_decoracion, name='sacar_decoracion'),

  path("vaciar_carro/", views.vaciar_carro, name='vaciar_carro'),

]
