# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-25 06:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0010_auto_20180725_1150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shipping.Transaction', verbose_name='Documents'),
        ),
    ]