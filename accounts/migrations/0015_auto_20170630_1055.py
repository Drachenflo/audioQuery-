# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20170630_1045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='button',
            name='preset',
            field=models.CharField(choices=[(0, 0), (1, 1), (2, 2), (3, 3)], default=0, max_length=15),
        ),
    ]