# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20170630_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='preset',
            field=models.CharField(choices=[(0, 'preset_reset'), (1, 'preset_player'), (2, 'preset_overlap'), (3, 'preset_replay')], default=0, max_length=2),
        ),
    ]
