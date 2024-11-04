# Generated by Django 5.1.1 on 2024-09-18 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0005_rename_datosusuario_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='alerta_dias_finalizar',
            field=models.IntegerField(blank=True, default=30, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='alerta_entrega_fisico',
            field=models.IntegerField(blank=True, default=15, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='alerta_secop',
            field=models.IntegerField(blank=True, default=15, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='cargo_supervisor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='cc_supervisor',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='cdp_fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='clase',
            field=models.CharField(blank=True, choices=[('arrendamiento', 'Arrendamiento'), ('cesion_derechos_patrimoniales', 'Cesión de Derechos Patrimoniales'), ('compraventa', 'Compraventa'), ('consultoria', 'Consultoría'), ('interadministrativo', 'Interadministrativo'), ('obra_publica', 'Obra Pública'), ('orden_compra', 'Orden de Compra (Colombia Compra Eficiente)'), ('prestacion_servicios', 'Prestación de Servicios'), ('prestacion_servicios_compraventa', 'Prestación de Servicios y Compraventa'), ('prestacion_servicios_suministro', 'Prestación de Servicios y Suministro'), ('seguros', 'Seguros'), ('prestacion_servicios_profesionales', 'Prestación de Servicios Profesionales'), ('suministro', 'Suministro')], max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='documentos_drive',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='documentos_secop',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='email_contratista',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='email_supervisor',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='estado_contrato',
            field=models.CharField(blank=True, choices=[('activo', 'Activo'), ('finalizado', 'Finalizado'), ('suspendido', 'Suspendido')], default='activo', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_aclaratoria',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_acta_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_acta_liquidacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_ampliacion_suspension',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_aprobacion_poliza',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_entrega_carpeta_fisico',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_expedicion_poliza',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_finalizacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_modificatoria',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_prorroga',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_publicacion_secop',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_reinicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_suscripcion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fecha_suspension',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='fuente_financiacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='funcionario_a_cargo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='justificacion_aclaratoria',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='justificacion_modificatoria',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='justificacion_prorroga',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='justificacion_suspension',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='nit_contratista',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='nit_representante_legal',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='nombre_contratista',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='nueva_fecha_finalizacion',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='numero_cdp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='numero_contrato',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='numero_poliza',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='numero_rp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='objeto',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='plazo_ejecucion',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='representante_legal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='rp_fecha',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='rubro_presupuestal',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='supervisor',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='telefono_contratista',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='tiene_entrada_almacen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contrato',
            name='tipo_contratacion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='union_temporal_consorcio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='valor_adicion_1',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='valor_adicion_2',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='valor_adicion_3',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='valor_final_contrato',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True),
        ),
        migrations.AddField(
            model_name='contrato',
            name='valor_total_adiciones',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15, null=True),
        ),
    ]