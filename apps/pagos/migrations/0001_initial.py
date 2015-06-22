# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('No_Recibo', models.IntegerField(max_length=15)),
                ('Lect_Anterior', models.IntegerField(max_length=15)),
                ('Lect_Actual', models.IntegerField(max_length=15)),
                ('Consumo_M3', models.IntegerField(max_length=15)),
                ('Meses_Rezago', models.IntegerField(max_length=8)),
                ('mesfacturacion', models.CharField(max_length=40)),
                ('Importe', models.IntegerField(max_length=15)),
                ('observaciones', models.CharField(max_length=600)),
                ('Fecha_Pago', models.DateField()),
                ('Total_Pagar', models.IntegerField(max_length=15)),
                ('Cliente', models.ForeignKey(to='cliente.Cliente')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
