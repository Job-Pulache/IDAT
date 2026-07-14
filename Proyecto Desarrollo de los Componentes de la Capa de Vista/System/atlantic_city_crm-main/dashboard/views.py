from django.shortcuts import render

from clientes.models import Cliente
from visitas.models import Visita
from incidencias.models import Incidencia
from promociones.models import Promocion
from django.contrib.auth.decorators import login_required


@login_required
def inicio_dashboard(request):
    # Indicadores principales del sistema.
    total_clientes = Cliente.objects.count()
    total_visitas = Visita.objects.count()
    total_incidencias = Incidencia.objects.count()
    total_promociones = Promocion.objects.count()

    # Estados de clientes.
    clientes_activos = Cliente.objects.filter(estado='activo').count()
    clientes_inactivos = Cliente.objects.filter(estado='inactivo').count()
    clientes_bloqueados = Cliente.objects.filter(estado='bloqueado').count()

    # Estados de incidencias.
    incidencias_pendientes = Incidencia.objects.filter(estado='pendiente').count()
    incidencias_en_proceso = Incidencia.objects.filter(estado='en_proceso').count()
    incidencias_resueltas = Incidencia.objects.filter(estado='resuelta').count()
    incidencias_cerradas = Incidencia.objects.filter(estado='cerrada').count()

    # Estados de promociones.
    promociones_activas = Promocion.objects.filter(estado='activa').count()
    promociones_inactivas = Promocion.objects.filter(estado='inactiva').count()
    promociones_finalizadas = Promocion.objects.filter(estado='finalizada').count()

    # Últimos registros para tener una vista rápida de actividad reciente.
    ultimos_clientes = Cliente.objects.all().order_by('-fecha_registro')[:5]
    ultimas_visitas = Visita.objects.select_related('cliente').all().order_by('-fecha_visita')[:5]

    return render(request, 'dashboard/inicio.html', {
        'total_clientes': total_clientes,
        'total_visitas': total_visitas,
        'total_incidencias': total_incidencias,
        'total_promociones': total_promociones,

        'clientes_activos': clientes_activos,
        'clientes_inactivos': clientes_inactivos,
        'clientes_bloqueados': clientes_bloqueados,

        'incidencias_pendientes': incidencias_pendientes,
        'incidencias_en_proceso': incidencias_en_proceso,
        'incidencias_resueltas': incidencias_resueltas,
        'incidencias_cerradas': incidencias_cerradas,

        'promociones_activas': promociones_activas,
        'promociones_inactivas': promociones_inactivas,
        'promociones_finalizadas': promociones_finalizadas,

        'ultimos_clientes': ultimos_clientes,
        'ultimas_visitas': ultimas_visitas,
    })