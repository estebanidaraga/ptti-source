# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 15:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ptti', '0004_testasignado_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='psicologo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ptti.Psicologo'),
        ),
    ]
