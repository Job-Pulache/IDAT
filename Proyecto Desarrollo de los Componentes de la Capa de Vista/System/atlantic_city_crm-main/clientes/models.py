from django.db import models


class Cliente(models.Model):
    # Documento principal del cliente.
    # Lo usamos como dato único para evitar registros duplicados.
    dni = models.CharField(max_length=20, unique=True)

    # Datos básicos del cliente.
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)

    # Datos de contacto.
    telefono = models.CharField(max_length=20, blank=True)
    correo = models.EmailField(unique=True)

    # Dirección del cliente. No es obligatoria porque puede no estar disponible al inicio.
    direccion = models.CharField(max_length=200, blank=True)

    # Estado del cliente dentro del sistema.
    # Esto nos permite mantener el registro sin eliminarlo.
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('inactivo', 'Inactivo'),
        ('bloqueado', 'Bloqueado'),
    ]

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='activo'
    )

    # Fechas automáticas para saber cuándo se creó y cuándo se actualizó el registro.
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        # Esto hace que en el panel admin se vea el nombre completo del cliente.
        return f'{self.nombres} {self.apellidos}'