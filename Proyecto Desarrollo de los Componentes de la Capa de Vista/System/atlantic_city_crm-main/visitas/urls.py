from django.urls import path
from . import views


urlpatterns = [
    # Lista general de todas las visitas registradas.
    path('', views.lista_visitas, name='lista_visitas'),

    # Registro de una nueva visita para un cliente específico.
    path('cliente/<int:cliente_id>/nueva/', views.crear_visita, name='crear_visita'),
]