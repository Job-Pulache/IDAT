from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from clientes.models import Cliente
from .models import Promocion, ClientePromocion
from .forms import ClientePromocionForm


@login_required
@permission_required('promociones.view_promocion', raise_exception=True)
def lista_promociones(request):
    # Tomamos el texto que el usuario escribe en el buscador.
    busqueda = request.GET.get('buscar', '')

    # Traemos todas las promociones registradas.
    promociones = Promocion.objects.all().order_by('-fecha_inicio')

    # Si el usuario escribió algo, filtramos por nombre, descripción o estado.
    if busqueda:
        promociones = promociones.filter(
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(estado__icontains=busqueda) |
            Q(fecha_inicio__icontains=busqueda) |
            Q(fecha_fin__icontains=busqueda)
        )

    return render(request, 'promociones/lista_promociones.html', {
        'promociones': promociones,
        'busqueda': busqueda
    })

@login_required
@permission_required('promociones.add_promocion', raise_exception=True)
def asignar_promocion(request, cliente_id):
    # Buscamos el cliente al que se le asignará la promoción.
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        form = ClientePromocionForm(request.POST)

        if form.is_valid():
            # No guardamos todavía porque falta asociar el cliente correcto.
            asignacion = form.save(commit=False)
            asignacion.cliente = cliente
            asignacion.save()

            return redirect('detalle_cliente', cliente_id=cliente.id)

    else:
        form = ClientePromocionForm()

    return render(request, 'promociones/form_asignar_promocion.html', {
        'form': form,
        'cliente': cliente
    })