# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2019-12-22 21:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='comment',
            field=models.CharField(default='', max_length=10),
            preserve_default=False,
        ),
    ]
