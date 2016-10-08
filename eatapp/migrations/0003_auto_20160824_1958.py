# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-24 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eatapp', '0002_auto_20160822_1556'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('categoriesno', models.IntegerField(primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=100)),
                ('resno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eatapp.Restaurants')),
            ],
        ),
        migrations.AddField(
            model_name='menus',
            name='categoriesno',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eatapp.Categories'),
            preserve_default=False,
        ),
    ]