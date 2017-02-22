# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 06:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djesapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='rss_url',
            new_name='url',
        ),
        migrations.AddField(
            model_name='article',
            name='url',
            field=models.CharField(max_length=512, null=True),
        ),
    ]
