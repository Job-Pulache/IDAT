from django.db import models


class Incidencia(models.Model):
    # Cada incidencia pertenece a un cliente específico.
    cliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete=models.CASCADE,
        related_name='incidencias'
    )

    TIPO_CHOICES = [
        ('consulta', 'Consulta'),
        ('reclamo', 'Reclamo'),
        ('queja', 'Queja'),
        ('sugerencia', 'Sugerencia'),
        ('problema', 'Problema'),
        ('otro', 'Otro'),
    ]

    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_proceso', 'En proceso'),
        ('resuelta', 'Resuelta'),
        ('cerrada', 'Cerrada'),
    ]

    tipo = models.CharField(
        max_length=30,
        choices=TIPO_CHOICES,
        default='consulta'
    )

    asunto = models.CharField(max_length=150)

    descripcion = models.TextField()

    estado = models.CharField(
        max_length=30,
        choices=ESTADO_CHOICES,
        default='pendiente'
    )

    respuesta = models.TextField(blank=True)

    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Incidencia'
        verbose_name_plural = 'Incidencias'
        ordering = ['-fecha_registro']

    def __str__(self):
        return f'{self.get_tipo_display()} - {self.cliente}'