# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-28 02:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatapp', '0003_auto_20160824_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default=0, max_length=15),
            preserve_default=False,
        ),
    ]
