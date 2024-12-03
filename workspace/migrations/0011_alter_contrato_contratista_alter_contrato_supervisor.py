# Generated by Django 5.1.1 on 2024-11-30 05:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0010_alter_contrato_clase_alter_contrato_numero_poliza_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='contratista',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workspace.contratista'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='supervisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workspace.supervisor'),
        ),
    ]