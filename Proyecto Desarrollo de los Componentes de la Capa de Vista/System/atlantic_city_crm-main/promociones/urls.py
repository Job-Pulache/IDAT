from django.urls import path
from . import views


urlpatterns = [
    # Lista general de promociones registradas.
    path('', views.lista_promociones, name='lista_promociones'),

    # Asignar una promoción a un cliente específico.
    path('cliente/<int:cliente_id>/asignar/', views.asignar_promocion, name='asignar_promocion'),
]