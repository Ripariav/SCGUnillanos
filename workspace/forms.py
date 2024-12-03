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
    numero_contrato = forms.IntegerField(required=False)
    tipo_contratacion = forms.CharField(required=False)
    objeto = forms.CharField(required=True)
    clase = forms.CharField(required=False)
    valor = forms.DecimalField(required=False)
    fecha_suscripcion_contrato = forms.DateField(required=False)
    CDP_num = forms.IntegerField(required=False)
    CDP_fecha = forms.DateField(required=False)
    RP_num = forms.IntegerField(required=False)
    RP_fecha = forms.DateField(required=False)
    rubro_presupuestal = forms.CharField(required=False)
    numero_poliza = forms.IntegerField(required=False)
    fecha_poliza_expedicion = forms.DateField(required=False)
    fecha_poliza_aprobacion = forms.DateField(required=False)
    fuente_recursos = forms.CharField(required=False)
    plazo_inicio = forms.DateField(required=False)
    plazo_fin = forms.DateField(required=False)
    estado_contrato = forms.CharField(required=False)
    documentos_cargados = forms.URLField(required=False)
    fecha_publicacion_secop = forms.DateField(required=False)
    publicacion_secop = forms.URLField(required=False)
    almacen = forms.BooleanField(required=False)
    fecha_liquidacion = forms.DateField(required=False)
    dependencia_responsable = forms.CharField(required=False)
    ubicacion = forms.CharField(required=False)
    presupuesto_programado = forms.DecimalField(required=False)
    modalidad_seleccion = forms.CharField(required=False)
    contratista = forms.ModelChoiceField(queryset=Contratista.objects.all(), required=False)
    supervisor = forms.ModelChoiceField(queryset=Supervisor.objects.all(), required=False)
    gestor = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    abogado = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    revisor = forms.ModelChoiceField(queryset=User.objects.all(), required=False)
    class Meta:
        model = Contrato
        fields = [
            'numero_contrato',
            'tipo_contratacion',
            'objeto',
            'clase',
            'valor',
            'fecha_suscripcion_contrato',
            'CDP_num',
            'CDP_fecha',
            'RP_num',
            'RP_fecha',
            'rubro_presupuestal',
            'numero_poliza',
            'fecha_poliza_expedicion',
            'fecha_poliza_aprobacion',
            'fuente_recursos',
            'plazo_inicio',
            'plazo_fin',
            'estado_contrato',
            'documentos_cargados',
            'fecha_publicacion_secop',
            'publicacion_secop',
            'almacen',
            'fecha_liquidacion',
            'dependencia_responsable',
            'ubicacion',
            'presupuesto_programado',
            'modalidad_seleccion',
            'adicion',
            'prorroga',
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

