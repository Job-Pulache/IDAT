from django.contrib import admin
from .models import Incidencia


@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = (
        'cliente',
        'tipo',
        'asunto',
        'estado',
        'fecha_registro',
    )

    list_filter = (
        'tipo',
        'estado',
        'fecha_registro',
    )

    search_fields = (
        'cliente__dni',
        'cliente__nombres',
        'cliente__apellidos',
        'asunto',
        'descripcion',
    )

    ordering = ('-fecha_registro',)