from django.urls import path
from . import views


urlpatterns = [
    # Lista general de todas las incidencias registradas.
    path('', views.lista_incidencias, name='lista_incidencias'),

    # Registro de una nueva incidencia para un cliente específico.
    path('cliente/<int:cliente_id>/nueva/', views.crear_incidencia, name='crear_incidencia'),
]