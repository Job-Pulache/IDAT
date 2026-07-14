from django import forms
from .models import Visita


class VisitaForm(forms.ModelForm):
    class Meta:
        model = Visita

        # El cliente no se coloca aquí porque lo tomaremos desde la ficha.
        # Así evitamos que el usuario seleccione un cliente equivocado.
        fields = [
            'motivo',
            'observacion',
        ]

        widgets = {
            'motivo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'observacion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Ingrese una observación de la visita'
            }),
        }