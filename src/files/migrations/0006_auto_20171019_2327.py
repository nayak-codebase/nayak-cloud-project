# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-19 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0005_fileitem_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileitem',
            name='url',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
