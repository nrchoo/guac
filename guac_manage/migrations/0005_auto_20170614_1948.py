# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-14 19:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('guac_manage', '0004_auto_20170614_0622'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_type', models.CharField(choices=[('BEGINNER', 'Beginner'), ('INTERMEDIATE', 'Intermediate'), ('PROFESSIONAL', 'Professional')], default='BEGINNER', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='package',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='guac_manage.Package'),
        ),
    ]
