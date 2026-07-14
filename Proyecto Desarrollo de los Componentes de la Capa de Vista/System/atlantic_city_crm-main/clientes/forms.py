from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente

        # Estos son los campos que el usuario podrá llenar desde el formulario.
        fields = [
            'dni',
            'nombres',
            'apellidos',
            'telefono',
            'correo',
            'direccion',
            'estado',
        ]

        # Aquí damos estilo Bootstrap a cada campo para que el formulario se vea ordenado.
        widgets = {
            'dni': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: 12345678'
            }),
            'nombres': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese los nombres'
            }),
            'apellidos': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese los apellidos'
            }),
            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ejemplo: 999888777'
            }),
            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'cliente@correo.com'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Dirección del cliente'
            }),
            'estado': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

    def clean_dni(self):
        # Normalizamos el DNI para evitar espacios antes o después.
        dni = self.cleaned_data.get('dni', '').strip()

        if not dni:
            raise forms.ValidationError('El DNI es obligatorio.')

        return dni

    def clean_correo(self):
        # Guardamos el correo en minúsculas para evitar duplicados por diferencias de escritura.
        correo = self.cleaned_data.get('correo', '').strip().lower()

        if not correo:
            raise forms.ValidationError('El correo es obligatorio.')

        return correo