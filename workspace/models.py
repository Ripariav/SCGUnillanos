from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from django.core.validators import URLValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.db.models import Max
from datetime import date

 #Opciones
MODALIDAD_SELECCION_CHOICES = [
        ('Sin Clasificar', 'Sin Clasificar'),
        ('Directa', 'Directa'),
        ('Privada', 'Privada'),
        ('Publica', 'Publica'),
    ]
CLASE_CONTRATO_CHOICES = [
        ('Arrendamiento', 'Arrendamiento'),
        ('Cesión Derechos Patrimoniales', 'Cesión Derechos Patrimoniales'),
        ('Compraventa', 'Compraventa'),
        ('Consultoría', 'Consultoría'),
        ('Interadministrativo', 'Interadministrativo'),
        ('Obra Pública', 'Obra Pública'),
        ('Orden Compra Colombia Compra Eficiente', 'Orden Compra Colombia Compra Eficiente'),
        ('Prestación de Servicios', 'Prestación de Servicios'),
        ('Prestación de Servicios y Compraventa', 'Prestación de Servicios y Compraventa'),
        ('Prestación de Servicios y Suministro', 'Prestación de Servicios y Suministro'),
        ('Seguros', 'Seguros'),
        ('Prestación de Servicios Profesionales', 'Prestación de Servicios Profesionales'),
        ('Suministro', 'Suministro'),
    ]
FUENTE_RECURSOS_CHOICES = [('Recursos propios', 'Recursos propios'),
        ('Presupuesto de entidad nacional', 'Presupuesto de entidad nacional'),
        ('Regalías', 'Regalías'),
        ('Recursos de credito', 'Recursos de credito'),
        ('SGP', 'SGP'),
        ('No Aplica', 'No Aplica'),
    ]
ESTADO_CONTRATO_CHOICES = [
        ('Activo', 'Activo'),
        ('Suspendido', 'Suspendido'),
        ('Liquidado', 'Liquidado'),
    ]


class Contratista(models.Model):
    nombre = models.CharField(max_length=255, blank=False, unique=True)
    nit_o_cc = models.IntegerField(blank=True, null=True)
    representante_legal = models.CharField(max_length=255, blank=True, null=True)
    nit_o_cc_representante_legal = models.IntegerField(blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    email_secundario = models.EmailField(blank=True, null=True)
    consorcio = models.CharField(max_length=255, blank= True, null = True )
    #extra
    fecha_agregado = models.DateField(auto_now_add=True, null=True)

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



# INICIO DE LO RELACIONADO CON CONTRATO ===========================================================================================================

#TODO: revisar todos lso modelos en su integracion
# Estas con las que puede coexistir con el proceso de manera activa
class Adicion(models.Model):
    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE, related_name='adiciones', null=True)
    adicion_1 = models.CharField(max_length=255)
    adicion_2 = models.CharField(max_length=255, blank=True, null=True)
    adicion_3 = models.CharField(max_length=255, blank=True, null=True)
    valor_total = models.DecimalField(max_digits=20, decimal_places=2)
    #extra
    fecha = models.DateField()

class Prorroga(models.Model):
    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE, related_name='prorrogas', null=True)
    fecha = models.DateField(null=True)
    justificacion = models.TextField(null=True)
    nueva_fecha_terminacion = models.DateField(null=True)
    fecha_suspension = models.DateField(blank=True, null=True)
    fecha_reinicio = models.DateField(blank=True, null=True)
    

class Modificacion(models.Model):
    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE, related_name='modificaciones', null=True)
    fecha_subscripcion =  models.DateField(null=True)
    motivo =  models.CharField( max_length=250,null=True)

class Aclaracion(models.Model):
    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE, related_name='aclaraciones', null=True)
    fecha_subscripcion =  models.DateField(null=True)
    motivo =  models.CharField( max_length=250,null=True)

# Estas con las que NO puede coexistir con el proceso de manera activa

class Suspension(models.Model):
    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE, related_name='suspensiones', null=True)
    fecha_subscripcion =  models.DateField(null=True)
    plazo= models.DateField(null=True)
    fecha_posible_reinicio =  models.DateField(blank = True, null = True)

class Reinicio(models.Model):
    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE, related_name='reinicios', null=True)
    fecha_subscripcion =  models.DateField(null=True)
    fecha_terminacion = models.DateField(null=True)

class Ampliacion(models.Model):
    contrato = models.ForeignKey('Contrato', on_delete=models.CASCADE, related_name='ampliaciones', null=True)
    fecha_subscripcion =  models.DateField(null=True)
    fecha_terminacion = models.DateField(null=True)


# CONTRATO ===========================================================================================================

class Contrato(models.Model):
    

    #Datos Generales
    objeto = models.TextField(blank=True, null=True, default="no se ha presentado objeto")
    numero_contrato = models.IntegerField(unique=True, blank=True, null=True, default=0)
    tipo_contratacion = models.CharField(max_length=600, choices=MODALIDAD_SELECCION_CHOICES, default="Sin Tipo")
    clase = models.CharField(max_length=600, choices=CLASE_CONTRATO_CHOICES, blank=True, null=True, default="Sin Clase")
    valor = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True, default=0)  # final
    plazo = models.CharField(max_length=50 , blank= True, null = True)
    fecha_suscripcion_contrato = models.DateField(blank=True, null=True)
    #Contractual ----------------------------------------------------------------------------------------------------------------------------
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
    aseguradora = models.CharField(blank=True, null=True, max_length=50)
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
    estado_contrato=models.CharField(default='Activo' , max_length=200, choices=ESTADO_CONTRATO_CHOICES)
    #documentos
    documentos_cargados = models.URLField(max_length=600, blank=True, null=True)
    #Secop
    fecha_publicacion_secop = models.DateField(blank=True, null=True, default="www.unillanos.edu.co")
    publicacion_secop = models.URLField(
        max_length=600, 
        blank=True,
        null=True,
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
    # gestores involucrados
    contratista = models.ForeignKey(Contratista, on_delete=models.SET_NULL, blank=True, null=True)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.SET_NULL, blank=True, null=True)

    # Usuarios involucrados
    gestor = models.ForeignKey(User, related_name='gestor_contratos', on_delete=models.SET_NULL, null=True, blank=True)
    abogado = models.ForeignKey(User, related_name='abogado_contratos', on_delete=models.SET_NULL, null=True, blank=True)
    revisor = models.ForeignKey(User, related_name='revisor_contratos', on_delete=models.SET_NULL, null=True, blank=True)

# workspace/forms.py

    
    def __str__(self):
        return f"Contrato {self.numero_contrato}"

    @property
    def ultima_fecha(self):
        """
        Calcula la fecha más reciente entre todas las modificaciones del contrato
        """
        fechas = []
        
        # Añadir fecha fin original del contrato
        if self.plazo_fin:
            fechas.append(self.plazo_fin)

        # Verificar prórrogas
        ultima_prorroga = self.prorrogas.aggregate(Max('nueva_fecha_terminacion'))
        if ultima_prorroga['nueva_fecha_terminacion__max']:
            fechas.append(ultima_prorroga['nueva_fecha_terminacion__max'])

        # Verificar ampliaciones
        ultima_ampliacion = self.ampliaciones.aggregate(Max('fecha_terminacion'))
        if ultima_ampliacion['fecha_terminacion__max']:
            fechas.append(ultima_ampliacion['fecha_terminacion__max'])

        # Verificar suspensiones y reinicios
        ultima_suspension = self.suspensiones.aggregate(Max('fecha_posible_reinicio'))
        if ultima_suspension['fecha_posible_reinicio__max']:
            fechas.append(ultima_suspension['fecha_posible_reinicio__max'])

        ultimo_reinicio = self.reinicios.aggregate(Max('fecha_terminacion'))
        if ultimo_reinicio['fecha_terminacion__max']:
            fechas.append(ultimo_reinicio['fecha_terminacion__max'])

        # Retornar la fecha más reciente
        return max(fechas) if fechas else None

    @property
    def dias_hasta_ultima_fecha(self):
        """
        Calcula los días restantes hasta la última fecha
        """
        if self.ultima_fecha:
            return (self.ultima_fecha - date.today()).days
        return None




