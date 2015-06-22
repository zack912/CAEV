# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Nombre', models.CharField(max_length=200)),
                ('Direccion', models.CharField(max_length=200)),
                ('Municipio', models.CharField(max_length=50)),
                ('Telefono', models.CharField(max_length=12)),
                ('Sexo', models.CharField(max_length=20, choices=[(b'hombre', b'Hombre'), (b'mujer', b'Mujer')])),
                ('RFC', models.CharField(max_length=13)),
                ('CURP', models.CharField(max_length=15)),
                ('Departamento', models.CharField(max_length=50)),
                ('Puesto', models.CharField(max_length=50)),
                ('Nomb_User', models.CharField(max_length=20)),
                ('Contrasenia', models.CharField(max_length=15)),
                ('No_empleado', models.IntegerField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
