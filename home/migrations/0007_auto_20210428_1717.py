# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20160728_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 28, 17, 17, 48, 608556)),
        ),
    ]
