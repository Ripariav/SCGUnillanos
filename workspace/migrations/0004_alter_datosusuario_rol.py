# Generated by Django 5.1.1 on 2024-09-16 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0003_contrato_abogado_contrato_gestor_contrato_revisor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosusuario',
            name='rol',
            field=models.CharField(choices=[('gestor', 'Gestor'), ('abogado', 'Abogado'), ('revisor', 'Revisor')], max_length=10, null=True),
        ),
    ]
