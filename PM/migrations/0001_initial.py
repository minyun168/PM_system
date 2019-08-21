# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('month', models.CharField(max_length=100)),
                ('day', models.CharField(max_length=100)),
                ('finished_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
