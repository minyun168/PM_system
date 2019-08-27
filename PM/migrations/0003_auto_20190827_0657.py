# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0002_auto_20190824_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='year',
            field=models.CharField(max_length=10),
        ),
    ]
