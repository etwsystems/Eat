# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-02 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatapp', '0004_customer_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='orderend',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]