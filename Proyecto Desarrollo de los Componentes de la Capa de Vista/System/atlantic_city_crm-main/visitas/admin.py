from django.contrib import admin
from .models import Visita


@admin.register(Visita)
class VisitaAdmin(admin.ModelAdmin):
    # Columnas visibles en el listado del admin.
    list_display = (
        'cliente',
        'motivo',
        'fecha_visita',
    )

    # Filtros rápidos.
    list_filter = (
        'motivo',
        'fecha_visita',
    )

    # Buscador por datos del cliente relacionado.
    search_fields = (
        'cliente__dni',
        'cliente__nombres',
        'cliente__apellidos',
        'cliente__correo',
    )

    # Ordenamos mostrando primero las visitas más recientes.
    ordering = ('-fecha_visita',)