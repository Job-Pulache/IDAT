from django.contrib import admin
from .models import Promocion, ClientePromocion


@admin.register(Promocion)
class PromocionAdmin(admin.ModelAdmin):
    # Columnas visibles en el listado de promociones.
    list_display = (
        'nombre',
        'fecha_inicio',
        'fecha_fin',
        'estado',
        'fecha_registro',
    )

    # Filtros rápidos para ubicar promociones.
    list_filter = (
        'estado',
        'fecha_inicio',
        'fecha_fin',
    )

    # Buscador por nombre y descripción.
    search_fields = (
        'nombre',
        'descripcion',
    )

    ordering = ('-fecha_inicio',)


@admin.register(ClientePromocion)
class ClientePromocionAdmin(admin.ModelAdmin):
    # Columnas visibles en las promociones asignadas a clientes.
    list_display = (
        'cliente',
        'promocion',
        'estado',
        'fecha_asignacion',
    )

    # Filtros rápidos.
    list_filter = (
        'estado',
        'fecha_asignacion',
        'promocion',
    )

    # Buscador por datos del cliente y promoción.
    search_fields = (
        'cliente__dni',
        'cliente__nombres',
        'cliente__apellidos',
        'cliente__correo',
        'promocion__nombre',
    )

    ordering = ('-fecha_asignacion',)