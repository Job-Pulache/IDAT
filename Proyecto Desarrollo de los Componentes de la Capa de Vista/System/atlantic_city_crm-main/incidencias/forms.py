from django import forms
from .models import Incidencia


class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia

        # El cliente no va en el formulario porque se tomará desde la ficha.
        # Así evitamos asociar la incidencia al cliente incorrecto.
        fields = [
            'tipo',
            'asunto',
            'descripcion',
            'estado',
            'respuesta',
        ]

        widgets = {
            'tipo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'asunto': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: Demora en atención'
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Describa la incidencia reportada por el cliente'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
            'respuesta': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Respuesta o acción tomada. Puede dejarse vacío al inicio.'
            }),
        }