from django import forms
from aplication.core.models import Certificado

class CertificadoForm(forms.ModelForm):
    class Meta:
        model = Certificado
        fields = ['paciente', 'doctor', 'fecha_emision', 'motivo', 'descripcion', 'duracion_reposo', 'firma', 'activo']
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-control'}),
            'doctor': forms.Select(attrs={'class': 'form-control'}),
            'fecha_emision': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'motivo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'duracion_reposo': forms.NumberInput(attrs={'class': 'form-control'}),
            'firma': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'paciente': 'Paciente',
            'doctor': 'Doctor',
            'fecha_emision': 'Fecha de Emisión',
            'motivo': 'Motivo/Diagnóstico',
            'descripcion': 'Descripción Adicional',
            'duracion_reposo': 'Duración de Reposo (días)',
            'firma': 'Firma Digital',
            'activo': 'Activo',
        }
        help_texts = {
            'motivo': 'Ingrese el diagnóstico o motivo del certificado.',
            'descripcion': 'Ingrese cualquier recomendación o información adicional.',
            'duracion_reposo': 'Ingrese la duración del reposo en días (deje vacío si no aplica).',
            'firma': 'Suba la firma digital del certificado (opcional).',
        }


