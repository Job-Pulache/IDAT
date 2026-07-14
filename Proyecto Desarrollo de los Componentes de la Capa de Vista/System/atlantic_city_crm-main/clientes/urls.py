from django.urls import path
from . import views


urlpatterns = [
    # Lista general de clientes.
    path('', views.lista_clientes, name='lista_clientes'),

    # Formulario para registrar un nuevo cliente.
    path('nuevo/', views.crear_cliente, name='crear_cliente'),

    # Ficha única del cliente.
    path('<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),

    # Formulario para editar los datos de un cliente existente.
    path('<int:cliente_id>/editar/', views.editar_cliente, name='editar_cliente'),
]