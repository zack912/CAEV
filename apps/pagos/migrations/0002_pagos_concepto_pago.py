# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagos',
            name='concepto_pago',
            field=models.CharField(default=datetime.date(2015, 6, 30), max_length=15),
            preserve_default=False,
        ),
    ]
