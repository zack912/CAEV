# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('consumo_promedio', '0001_initial'),
        ('tipo_usuario', '0001_initial'),
        ('marca_medidor', '0001_initial'),
        ('diametro_toma', '0001_initial'),
        ('tipo_servicio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Zona', models.CharField(max_length=10)),
                ('Dig_verf', models.CharField(max_length=3)),
                ('Contrato', models.CharField(unique=True, max_length=20)),
                ('Fecha_Registro', models.DateField(default=datetime.datetime.now)),
                ('Nombre', models.CharField(max_length=200)),
                ('RFC', models.CharField(max_length=20)),
                ('Telefono', models.CharField(max_length=10)),
                ('Calle', models.CharField(max_length=50)),
                ('Municipio', models.CharField(max_length=50)),
                ('No_Interior', models.CharField(max_length=5)),
                ('Colonia', models.CharField(max_length=45)),
                ('No_Medidor', models.IntegerField(max_length=10)),
                ('Capacidad_Digitos', models.CharField(max_length=15)),
                ('sector', models.CharField(max_length=45)),
                ('ruta', models.CharField(max_length=45)),
                ('folio', models.CharField(max_length=20)),
                ('lectura', models.CharField(max_length=6)),
                ('status', models.BooleanField(default=True)),
                ('consumo_promedio', models.ForeignKey(to='consumo_promedio.consumo_promedio')),
                ('diametro_toma', models.ForeignKey(to='diametro_toma.diametro_toma')),
                ('marca_medidor', models.ForeignKey(to='marca_medidor.marca_medidor')),
                ('tipo_servicio', models.ForeignKey(to='tipo_servicio.tipo_servicio')),
                ('tipo_usuario', models.ForeignKey(to='tipo_usuario.tipo_usuario')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
