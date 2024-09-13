from django.db import models

# Create your models here.
class Contrato(models.Model):
    #informacion basica
    codigo_unspsc = models.CharField(max_length=100, help_text="Código UNSPSC")
    dependencia_responsable = models.CharField(max_length=255)
    descripcion = models.TextField()
    observaciones = models.TextField(null=True, blank=True)
    
    fecha_estimada_inicio = models.DateField(help_text="Fecha estimada de inicio del proceso de selección", null=True, blank=True)
    fecha_estimada_ofertas = models.DateField(help_text="Fecha estimada de presentación de ofertas", null=True, blank=True)

    
    def __str__(self):
        return f"Contrato {self.descripcion} ({self.codigo_unspsc})"