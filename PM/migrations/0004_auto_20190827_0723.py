# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0003_auto_20190827_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='finished_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='year',
            field=models.CharField(max_length=100),
        ),
    ]
