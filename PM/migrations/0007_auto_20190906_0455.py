# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0006_auto_20190906_0444'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='year',
            new_name='deadline',
        ),
    ]
