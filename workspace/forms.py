from django import forms
from .models import Contrato, Contratista, Supervisor, User, Rol, FUENTE_RECURSOS_CHOICES

class ContratistaForm(forms.ModelForm):
    class Meta:
        model = Contratista
        fields = '__all__'

class SupervisorForm(forms.ModelForm):
    class Meta:
        model = Supervisor
        fields = '__all__'

class ContratoForm(forms.ModelForm):
    
    contratista = forms.ModelChoiceField(
        queryset=Contratista.objects.all(), 
        required=False,
        empty_label="Seleccione un contratista"
    )
    supervisor = forms.ModelChoiceField(
        queryset=Supervisor.objects.all(), 
        required=False,
        empty_label="Seleccione un supervisor"
    )
    gestor = forms.ModelChoiceField(
        queryset=User.objects.filter(roles__rol='gestor'), 
        required=False,
        empty_label="Seleccione un gestor"
    )
    abogado = forms.ModelChoiceField(
        queryset=User.objects.filter(roles__rol='abogado'), 
        required=False,
        empty_label="Seleccione un abogado"
    )
    revisor = forms.ModelChoiceField(
        queryset=User.objects.filter(roles__rol='revisor'), 
        required=False,
        empty_label="Seleccione un revisor"
    )

    publicacion_secop = forms.URLField(required=False, empty_value=None)
    fuente_recursos = forms.ChoiceField(
        choices=[('', '--------')] + list(FUENTE_RECURSOS_CHOICES), 
        required=False
    )
    numero_poliza = forms.IntegerField(required=False, min_value=0)

    class Meta:
        model = Contrato
        fields = [
            'rubro_presupuestal',
            'tipo_contratacion',
            'clase', 
            'dependencia_responsable', 
            'descripcion', 
            'ubicacion',
            'CDP_num', 
            'CDP_fecha', 
            'RP_num', 
            'RP_fecha', 
            'fecha_suscripcion_contrato', 
            'plazo_inicio', 
            'plazo_fin',
            'estado_contrato', 
            'fecha_publicacion_secop', 
            'publicacion_secop', 
            'presupuesto_programado', 
            'numero_contrato', 
            'valor', 
            'modalidad_seleccion', 
            'fuente_recursos', 
            'numero_poliza', 
            'fecha_poliza_expedicion', 
            'fecha_poliza_aprobacion',
            'almacen',
            'documentos_cargados',
            'fecha_liquidacion',
            'contratista',
            'supervisor',
            'gestor',
            'abogado',
            'revisor',
        ]

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['contratista'].queryset = Contratista.objects.all()
            self.fields['supervisor'].queryset = Supervisor.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        for field in ['publicacion_secop', 'fuente_recursos', 'numero_poliza']:
            if cleaned_data.get(field) == '':
                cleaned_data[field] = None
        return cleaned_data
