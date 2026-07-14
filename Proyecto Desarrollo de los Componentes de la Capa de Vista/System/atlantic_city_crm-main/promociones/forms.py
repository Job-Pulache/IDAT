from django import forms
from .models import ClientePromocion


class ClientePromocionForm(forms.ModelForm):
    class Meta:
        model = ClientePromocion

        # El cliente no va aquí porque lo tomaremos desde la ficha.
        # El usuario solo elegirá la promoción y el estado.
        fields = [
            'promocion',
            'estado',
            'observacion',
        ]

        widgets = {
            'promocion': forms.Select(attrs={
                'class': 'form-select'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'observacion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Ingrese una observación sobre la asignación'
            }),
        }