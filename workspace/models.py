from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.core.validators import URLValidator, MinValueValidator
from django.core.exceptions import ValidationError


# Choices
MODALIDAD_SELECCION_CHOICES = [
    ('Sin Clasificar', 'Sin Clasificar'),
    ('Directa', 'Directa'),
    ('Privada', 'Privada'),
    ('Publica', 'Publica'),
]

CLASE_CONTRATO_CHOICES = [
    ('Arrendamiento', 'arrendamiento'),
    ('Cesión Derechos Patrimoniales', 'cesion_derechos_patrimoniales'),
    ('Compraventa', 'compraventa'),
    ('Consultoría', 'consultoria'),
    ('Interadministrativo', 'interadministrativo'),
    ('Obra Pública', 'obra_publica'),
    ('Orden Compra Colombia Compra Eficiente', 'orden_compra_colombia_compra_eficiente'),
    ('Prestación de Servicios', 'prestacion_servicios'),
    ('Prestación de Servicios y Compraventa', 'prestacion_servicios_compraventa'),
    ('Prestación de Servicios y Suministro', 'prestacion_servicios_suministro'),
    ('Seguros', 'seguros'),
    ('Prestación de Servicios Profesionales', 'prestacion_servicios_profesionales'),
    ('Suministro', 'suministro'),
]

FUENTE_RECURSOS_CHOICES = [
    ('recursos_propios', 'Recursos propios'),
    ('presupuesto_entidad_nacional', 'Presupuesto de entidad nacional'),
    ('regalias', 'Regalías'),
    ('recursos_credito', 'Recursos de crédito'),
    ('sgp', 'SGP'),
    ('no_aplica', 'No Aplica'),
]


class Contratista(models.Model):
    nombre = models.CharField(max_length=255, blank=False, unique=True)
    nit_o_cc = models.IntegerField(blank=True, null=True)
    representante_legal = models.CharField(max_length=255, blank=True, null=True)
    nit_o_cc_representante_legal = models.IntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    #extra
    fecha_agregado = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Supervisor(models.Model):
    nombre = models.CharField(max_length=255)
    nit_o_cc = models.IntegerField()
    cargo = models.CharField(max_length=255, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    #extra
    fecha_agregado = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Adicion(models.Model):
    adicion_1 = models.CharField(max_length=255)
    adicion_2 = models.CharField(max_length=255, blank=True, null=True)
    adicion_3 = models.CharField(max_length=255, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=20, decimal_places=2)
    #extra
    fecha = models.DateField()

class Prorroga(models.Model):
    fecha = models.DateField()
    justificacion = models.TextField()
    nueva_fecha_finalizacion = models.DateField()
    fecha_suspension = models.DateField(blank=True, null=True)
    fecha_reinicio = models.DateField(blank=True, null=True)

class Contrato(models.Model):

    #Fundamentales
    numero_contrato = models.IntegerField(unique=True, blank=True, null=True, default=0)
    tipo_contratacion = models.CharField(max_length=600, choices=MODALIDAD_SELECCION_CHOICES, default="noinfo")
    descripcion = models.TextField(blank=True, null=True, default="no se ha presentado objeto")
    clase = models.CharField(max_length=600, choices=CLASE_CONTRATO_CHOICES, blank=True, null=True)
    valor = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=0)  # final

    #Contractual ----------------------------------------------------------------------------------------------------------------------------
    fecha_suscripcion_contrato = models.DateField(blank=True, null=True)  # Fecha cuando se inicia la firma del contrato
    # CDP y RP
    CDP_num = models.IntegerField(unique=True, blank=True, null=True)
    CDP_fecha = models.DateField(blank=True, null=True)
    RP_num = models.IntegerField(unique=True, blank=True, null=True)
    RP_fecha = models.DateField(blank=True, null=True)
    #Rubro Presupuestal
    rubro_presupuestal = models.CharField(blank=True,null=True, max_length=500)
    # polizas
    numero_poliza = models.PositiveIntegerField(
        blank=True, 
        null=True, 
        validators=[MinValueValidator(0, message="El número de póliza debe ser un entero positivo.")],
        default=0
    )
    fecha_poliza_expedicion = models.DateField(blank=True, null=True)
    fecha_poliza_aprobacion = models.DateField(blank=True, null=True)
    #fuente de recursos
    fuente_recursos = models.CharField(
        max_length=600, 
        choices=FUENTE_RECURSOS_CHOICES, 
        blank=True, 
        null=True
    )  # SIGEP
    # plazos 
    plazo_inicio = models.DateField(blank=True, null=True)
    plazo_fin = models.DateField(blank=True, null=True)
    #estados
    estado_contrato=models.CharField(default='En Ejecución', max_length=200)
    #documentos
    documentos_cargados = models.URLField(max_length=600, blank=True, null=True)
    #Secop
    fecha_publicacion_secop = models.DateField(blank=True, null=True)
    publicacion_secop = models.URLField(
        max_length=600, 
        blank=True, 
        null=True, 
        validators=[URLValidator(message="Ingrese una URL válida o deje el campo en blanco.")]
    )
    #Almacen
    almacen = models.BooleanField(default=False)
    fecha_liquidacion = models.DateField(blank=True, null=True)

    #PAA ----------------------------------------------------------------------------------------------------------------------------------------
    dependencia_responsable = models.CharField(max_length=255, blank=True, null=True)
    ubicacion = models.CharField(max_length=600, blank=True, null=True)
    presupuesto_programado = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True) 
    modalidad_seleccion = models.CharField(max_length=600, blank=True, null=True)  

    
    # llaves foraneas ---------------------------------------------------------------------------------------------------------------------------
    # Extensiones del contrato si llega a suceder
    adicion = models.ForeignKey(Adicion, on_delete=models.SET_NULL, blank=True, null=True)
    prorroga = models.ForeignKey(Prorroga, on_delete=models.SET_NULL, blank=True, null=True)

    # gestores involucrados
    contratista = models.ForeignKey(Contratista, on_delete=models.CASCADE, blank=True, null=True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, blank=True, null=True)

    # Usuarios involucrados
    gestor = models.ForeignKey(User, related_name='gestor_contratos', on_delete=models.SET_NULL, null=True, blank=True)
    abogado = models.ForeignKey(User, related_name='abogado_contratos', on_delete=models.SET_NULL, null=True, blank=True)
    revisor = models.ForeignKey(User, related_name='revisor_contratos', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Contrato {self.numero_contrato}"

    def clean(self):
        if self.publicacion_secop == '':
            self.publicacion_secop = None
        
        if self.fuente_recursos == '':
            self.fuente_recursos = None
        
        if self.numero_poliza == '':
            self.numero_poliza = None

class Rol(models.Model):
    USUARIO_ROLES = (
        ('gestor', 'Gestor'),
        ('abogado', 'Abogado'),
        ('revisor', 'Revisor'),
    )

    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roles')
    rol = models.CharField(max_length=10, choices=USUARIO_ROLES)
    grupo = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True)
    permisos_adicionales = models.ManyToManyField(Permission, blank=True)

    class Meta:
        unique_together = ('usuario', 'rol')

    def __str__(self):
        return f"{self.usuario.username} ({self.get_rol_display()})"

