# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ptti', '0007_auto_20161007_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Activar'),
        ),
        migrations.AlterField(
            model_name='grupo',
            name='jornada',
            field=models.CharField(choices=[('MANANA', 'MANANA'), ('TARDE', 'TARDE'), ('UNICA', 'UNICA'), ('NOCTURNA', 'NOCTURNA'), ('SABATINA', 'SABATINA')], max_length=200),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Activar'),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='nit',
            field=models.CharField(max_length=200, unique=True, verbose_name='NIT'),
        ),
        migrations.AlterField(
            model_name='institucion',
            name='web',
            field=models.URLField(verbose_name='Sitio web'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('HETEROSEXUAL', 'HETEROSEXUAL'), ('HOMOSEXUAL', 'HOMOSEXUAL'), ('LESBIANA', 'LESBIANA'), ('BISEXUAL', 'BISEXUAL'), ('INDIFERENCIADO', 'INDIFERENCIADO')], max_length=20, verbose_name='Genero'),
        ),
    ]
