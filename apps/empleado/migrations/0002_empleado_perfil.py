# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='Perfil',
            field=models.CharField(default=datetime.date(2015, 6, 19), max_length=50),
            preserve_default=False,
        ),
    ]
