from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from clientes.models import Cliente
from .models import Visita
from .forms import VisitaForm


@login_required
@permission_required('visitas.add_visita', raise_exception=True)
def crear_visita(request, cliente_id):
    # Buscamos el cliente al que se le registrará la visita.
    # La visita siempre quedará asociada a este cliente.
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        form = VisitaForm(request.POST)

        if form.is_valid():
            # No guardamos de inmediato porque falta asignar el cliente.
            visita = form.save(commit=False)
            visita.cliente = cliente
            visita.save()

            return redirect('detalle_cliente', cliente_id=cliente.id)

    else:
        form = VisitaForm()

    return render(request, 'visitas/form_visita.html', {
        'form': form,
        'cliente': cliente
    })

@login_required
@permission_required('visitas.view_visita', raise_exception=True)
def lista_visitas(request):
    # Tomamos el texto que el usuario escribe en el buscador.
    busqueda = request.GET.get('buscar', '')

    # Traemos todas las visitas junto con los datos del cliente.
    visitas = Visita.objects.select_related('cliente').all().order_by('-fecha_visita')

    # Si el usuario escribió algo, filtramos por datos del cliente y de la visita.
    if busqueda:
        visitas = visitas.filter(
            Q(cliente__dni__icontains=busqueda) |
            Q(cliente__nombres__icontains=busqueda) |
            Q(cliente__apellidos__icontains=busqueda) |
            Q(cliente__correo__icontains=busqueda) |
            Q(motivo__icontains=busqueda) |
            Q(observacion__icontains=busqueda)
        )

    return render(request, 'visitas/lista_visitas.html', {
        'visitas': visitas,
        'busqueda': busqueda
    })