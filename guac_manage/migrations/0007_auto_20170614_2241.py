# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guac_manage', '0006_developer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='users',
        ),
        migrations.AlterField(
            model_name='company',
            name='purchased',
            field=models.NullBooleanField(default=False),
        ),
    ]