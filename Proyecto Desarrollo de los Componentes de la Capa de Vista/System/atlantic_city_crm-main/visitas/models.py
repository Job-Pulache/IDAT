from django.db import models


class Visita(models.Model):
    # Relacionamos cada visita con un cliente.
    # Si un cliente se elimina, también se eliminan sus visitas.
    cliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete=models.CASCADE,
        related_name='visitas'
    )

    # Fecha y hora de la visita.
    # auto_now_add guarda automáticamente el momento en que se registra.
    fecha_visita = models.DateTimeField(auto_now_add=True)

    # Área o motivo principal de la visita.
    MOTIVO_CHOICES = [
        ('juego', 'Juego'),
        ('promocion', 'Promoción'),
        ('consulta', 'Consulta'),
        ('evento', 'Evento'),
        ('otro', 'Otro'),
    ]

    motivo = models.CharField(
        max_length=30,
        choices=MOTIVO_CHOICES,
        default='juego'
    )

    # Observación libre para registrar algún detalle importante.
    observacion = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'
        ordering = ['-fecha_visita']

    def __str__(self):
        return f'Visita de {self.cliente} - {self.fecha_visita.strftime("%d/%m/%Y")}'