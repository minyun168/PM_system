# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('PM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='date_add',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 24, 17, 26, 56, 576923, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='finished_time',
            field=models.DateTimeField(),
        ),
    ]
