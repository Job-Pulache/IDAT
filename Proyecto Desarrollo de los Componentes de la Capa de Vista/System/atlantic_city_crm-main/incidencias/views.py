from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from clientes.models import Cliente
from .models import Incidencia
from .forms import IncidenciaForm


@login_required
@permission_required('incidencias.view_incidencia', raise_exception=True)
def lista_incidencias(request):
    # Tomamos el texto que el usuario escribe en el buscador.
    busqueda = request.GET.get('buscar', '')

    # Traemos todas las incidencias junto con los datos del cliente.
    incidencias = Incidencia.objects.select_related('cliente').all().order_by('-fecha_registro')

    # Si el usuario escribió algo, filtramos por datos del cliente y de la incidencia.
    if busqueda:
        incidencias = incidencias.filter(
            Q(cliente__dni__icontains=busqueda) |
            Q(cliente__nombres__icontains=busqueda) |
            Q(cliente__apellidos__icontains=busqueda) |
            Q(cliente__correo__icontains=busqueda) |
            Q(tipo__icontains=busqueda) |
            Q(asunto__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(respuesta__icontains=busqueda)
        )

    return render(request, 'incidencias/lista_incidencias.html', {
        'incidencias': incidencias,
        'busqueda': busqueda
    })

@login_required
@permission_required('incidencias.add_incidencia', raise_exception=True)
def crear_incidencia(request, cliente_id):
    # Buscamos el cliente al que se le registrará la incidencia.
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        form = IncidenciaForm(request.POST)

        if form.is_valid():
            # Detenemos el guardado para asignar primero el cliente correcto.
            incidencia = form.save(commit=False)
            incidencia.cliente = cliente
            incidencia.save()

            return redirect('detalle_cliente', cliente_id=cliente.id)

    else:
        form = IncidenciaForm()

    return render(request, 'incidencias/form_incidencia.html', {
        'form': form,
        'cliente': cliente
    })