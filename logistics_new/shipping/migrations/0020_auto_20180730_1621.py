# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-30 10:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0019_auto_20180730_1543'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='carreir_address',
            new_name='carrier_address',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='carreir_otp',
            new_name='carrier_otp',
        ),
    ]
