from django.contrib import admin

# Register your models here.
from .models import Contrato, Rol, Contratista, Supervisor

# Register your models here.
@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = (
        'numero_contrato',       # Cambiado de 'codigo_unspsc' a 'numero_contrato'
        'dependencia_responsable', 
        'descripcion', 
        'plazo_inicio',          # Cambiado de 'fecha_estimada_inicio' a 'plazo_inicio'
        'plazo_fin'              # Cambiado de 'fecha_estimada_ofertas' a 'plazo_fin'
    )
    search_fields = (
        'numero_contrato',       # Ajuste similar aquí
        'dependencia_responsable', 
        'descripcion'
    )
    list_filter = (
        'plazo_inicio',          # Ajuste basado en el nuevo modelo
        'plazo_fin'              # Ajuste basado en el nuevo modelo
    )

@admin.register(Rol)
class RolUsuario(admin.ModelAdmin):
    list_display = ('usuario', 'get_rol_display')
    search_fields = ('usuario__username', 'rol')
    list_filter = ('rol',)
    
    # Opcional: Para que el campo 'rol' se muestre como un desplegable en el formulario
    fieldsets = (
        (None, {
            'fields': ('usuario', 'rol'),
        }),
    )

@admin.register(Contratista)
class ContratistaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nit_o_cc', 'representante_legal', 'telefono', 'email', 'fecha_agregado')
    search_fields = ('nombre', 'nit_o_cc', 'representante_legal')
    list_filter = ('fecha_agregado',)

@admin.register(Supervisor)
class SupervisorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nit_o_cc', 'cargo', 'telefono', 'email', 'fecha_agregado')
    search_fields = ('nombre', 'nit_o_cc', 'cargo')
    list_filter = ('fecha_agregado',)