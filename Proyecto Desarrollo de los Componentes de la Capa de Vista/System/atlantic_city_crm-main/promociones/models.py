from django.db import models


class Promocion(models.Model):
    ESTADO_CHOICES = [
        ('activa', 'Activa'),
        ('inactiva', 'Inactiva'),
        ('finalizada', 'Finalizada'),
    ]

    nombre = models.CharField(max_length=120)

    descripcion = models.TextField()

    fecha_inicio = models.DateField()

    fecha_fin = models.DateField()

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='activa'
    )

    fecha_registro = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Promoción'
        verbose_name_plural = 'Promociones'
        ordering = ['-fecha_inicio']

    def __str__(self):
        return self.nombre


class ClientePromocion(models.Model):
    ESTADO_CHOICES = [
        ('asignada', 'Asignada'),
        ('usada', 'Usada'),
        ('vencida', 'Vencida'),
    ]

    cliente = models.ForeignKey(
        'clientes.Cliente',
        on_delete=models.CASCADE,
        related_name='promociones_cliente'
    )

    promocion = models.ForeignKey(
        Promocion,
        on_delete=models.CASCADE,
        related_name='clientes_promocion'
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,
        default='asignada'
    )

    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    observacion = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Promoción asignada'
        verbose_name_plural = 'Promociones asignadas'
        ordering = ['-fecha_asignacion']

    def __str__(self):
        return f'{self.cliente} - {self.promocion}'