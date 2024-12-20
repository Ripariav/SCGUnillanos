# Generated by Django 5.1.1 on 2024-09-16 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0002_contrato_finalizado_contrato_valor_estimado_actual'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='contrato',
            name='abogado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='abogado_contratos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contrato',
            name='gestor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='gestor_contratos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contrato',
            name='revisor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='revisor_contratos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='datosUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(choices=[('gestor', 'Gestor'), ('abogado', 'Abogado'), ('revisor', 'Revisor')], max_length=10)),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
