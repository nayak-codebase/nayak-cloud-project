# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-21 02:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0007_auto_20171019_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileitem',
            name='download',
            field=models.URLField(blank=True, null=True),
        ),
    ]