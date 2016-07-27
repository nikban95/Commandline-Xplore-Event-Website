# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20151105_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 28, 0, 22, 1, 273901)),
        ),
    ]
