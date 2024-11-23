from datetime import date
from django import forms
from aplication.core.models import FichaClinica

class FichaClinicaForm(forms.ModelForm):
    class Meta:
        model = FichaClinica
        fields = [
            'paciente',
            'doctor',
            'fecha_consulta',
            'motivo_consulta',
            'observaciones',
            'diagnostico',
            'tratamiento',
            'procedimientos',
            'receta',
            'adjuntos',
            'activo',
        ]
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-select'}),
            'doctor': forms.Select(attrs={'class': 'form-select'}),
            'fecha_consulta': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'motivo_consulta': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'diagnostico': forms.Select(attrs={'class': 'form-select'}),
            'tratamiento': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'procedimientos': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'receta': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'adjuntos': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def clean_fecha_consulta(self):
        """
        Validación personalizada para asegurar que la fecha de consulta no sea futura.
        """
        fecha_consulta = self.cleaned_data.get('fecha_consulta')
        if fecha_consulta and fecha_consulta > date.today():
            raise forms.ValidationError("La fecha de consulta no puede ser en el futuro.")
        return fecha_consulta
