from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # Columnas que veremos en la lista principal del admin.
    list_display = (
        'dni',
        'nombres',
        'apellidos',
        'correo',
        'telefono',
        'estado',
        'fecha_registro',
    )

    # Filtros rápidos al lado derecho.
    list_filter = (
        'estado',
        'fecha_registro',
    )

    # Campos por los que podremos buscar clientes.
    search_fields = (
        'dni',
        'nombres',
        'apellidos',
        'correo',
        'telefono',
    )

    # Orden inicial de la tabla.
    ordering = ('apellidos', 'nombres')

    # Campos que se mostrarán solo como lectura.
    readonly_fields = (
        'fecha_registro',
        'fecha_actualizacion',
    )