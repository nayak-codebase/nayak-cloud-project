# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-19 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_remove_fileitem_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileitem',
            name='url',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
