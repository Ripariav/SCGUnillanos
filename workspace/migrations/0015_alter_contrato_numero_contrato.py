# Generated by Django 5.1.1 on 2024-12-03 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0014_alter_contrato_cdp_num_alter_contrato_rp_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='numero_contrato',
            field=models.IntegerField(blank=True, default=0, null=True, unique=True),
        ),
    ]
