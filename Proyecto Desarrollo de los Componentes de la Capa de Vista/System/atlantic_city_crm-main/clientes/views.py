from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
from .models import Cliente
from .forms import ClienteForm


@login_required
@permission_required('clientes.view_cliente', raise_exception=True)
def lista_clientes(request):
    # Tomamos el texto que el usuario escribe en el buscador.
    # Si no escribió nada, usamos una cadena vacía.
    busqueda = request.GET.get('buscar', '')

    # Empezamos trayendo todos los clientes.
    clientes = Cliente.objects.all().order_by('apellidos', 'nombres')

    # Si el usuario escribió algo, filtramos por varios campos.
    if busqueda:
        clientes = clientes.filter(
            Q(dni__icontains=busqueda) |
            Q(nombres__icontains=busqueda) |
            Q(apellidos__icontains=busqueda) |
            Q(correo__icontains=busqueda) |
            Q(telefono__icontains=busqueda)
        )

    # Enviamos también el texto buscado para mantenerlo visible en el input.
    return render(request, 'clientes/lista_clientes.html', {
        'clientes': clientes,
        'busqueda': busqueda
    })

@permission_required('clientes.add_cliente', raise_exception=True)
@login_required
def crear_cliente(request):
    # Si el usuario envía el formulario, Django recibe los datos por POST.
    if request.method == 'POST':
        form = ClienteForm(request.POST)

        # Si los datos cumplen las reglas del modelo y del formulario, se guarda.
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')

    else:
        # Si todavía no se envió nada, mostramos un formulario vacío.
        form = ClienteForm()

    return render(request, 'clientes/form_cliente.html', {
        'form': form,
        'titulo': 'Nuevo cliente',
        'boton': 'Guardar cliente'
    })

@permission_required('clientes.view_cliente', raise_exception=True)
@login_required
def detalle_cliente(request, cliente_id):
    # Buscamos el cliente por su ID.
    # Si no existe, Django mostrará una página 404.
    cliente = get_object_or_404(Cliente, id=cliente_id)

    # Contamos todas las visitas del cliente.
    total_visitas = cliente.visitas.count()

    # Mostramos primero las visitas más recientes.
    visitas = cliente.visitas.all().order_by('-fecha_visita')[:5]

    # Contamos todas las incidencias del cliente.
    total_incidencias = cliente.incidencias.count()

    # Mostramos primero las incidencias más recientes.
    incidencias = cliente.incidencias.all().order_by('-fecha_registro')[:5]

    # Contamos todas las promociones asignadas al cliente.
    total_promociones = cliente.promociones_cliente.count()

    # Mostramos primero las promociones asignadas más recientes.
    promociones_cliente = cliente.promociones_cliente.select_related('promocion').all().order_by('-fecha_asignacion')[:5]

    return render(request, 'clientes/detalle_cliente.html', {
        'cliente': cliente,
        'visitas': visitas,
        'total_visitas': total_visitas,
        'incidencias': incidencias,
        'total_incidencias': total_incidencias,
        'promociones_cliente': promociones_cliente,
        'total_promociones': total_promociones
    })

@login_required
@permission_required('clientes.change_cliente', raise_exception=True)
def editar_cliente(request, cliente_id):
    # Buscamos el cliente que se quiere editar.
    # Si el ID no existe, mostramos un error 404 en lugar de romper la página.
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == 'POST':
        # Enviamos instance=cliente para actualizar ese registro,
        # no para crear uno nuevo.
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            form.save()
            return redirect('detalle_cliente', cliente_id=cliente.id)

    else:
        # Cargamos el formulario con los datos actuales del cliente.
        form = ClienteForm(instance=cliente)

    return render(request, 'clientes/form_cliente.html', {
        'form': form,
        'titulo': 'Editar cliente',
        'boton': 'Guardar cambios'
    })