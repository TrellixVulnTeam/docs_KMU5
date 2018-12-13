# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-10 18:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webdoctor', '0010_auto_20181211_0014'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='pincode',
            name='Pin',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cat', to='webdoctor.Pin'),
        ),
    ]