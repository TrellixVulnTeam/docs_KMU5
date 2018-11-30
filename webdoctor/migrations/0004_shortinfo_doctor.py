# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-09 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webdoctor', '0003_shortinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='shortinfo',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='webdoctor.doctor'),
        ),
    ]