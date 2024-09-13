from django.contrib import admin
from .models import Contrato

# Register your models here.
@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ('codigo_unspsc', 'dependencia_responsable', 'descripcion', 'fecha_estimada_inicio', 'fecha_estimada_ofertas')
    search_fields = ('codigo_unspsc', 'dependencia_responsable', 'descripcion')
    list_filter = ('fecha_estimada_inicio', 'fecha_estimada_ofertas')