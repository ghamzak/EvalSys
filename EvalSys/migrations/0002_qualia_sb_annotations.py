# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-14 06:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EvalSys', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qualia',
            name='sb_annotations',
            field=models.BooleanField(default=False),
        ),
    ]
