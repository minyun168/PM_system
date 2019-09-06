# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0005_project_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='day',
        ),
        migrations.RemoveField(
            model_name='project',
            name='month',
        ),
    ]
