# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0004_auto_20190827_0723'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='state',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
