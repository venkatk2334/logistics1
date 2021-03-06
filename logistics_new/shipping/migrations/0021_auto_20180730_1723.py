# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-30 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0020_auto_20180730_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='carreir_email',
            field=models.TextField(blank=True, null=True, verbose_name='carrier_email'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='carreir_mobileNo',
            field=models.TextField(blank=True, null=True, verbose_name='carreir_mobileNo'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='receiver_email',
            field=models.TextField(blank=True, null=True, verbose_name='receiver_email'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='receiver_mobileNo',
            field=models.TextField(blank=True, null=True, verbose_name='receiver_mobileNo'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sender_email',
            field=models.TextField(blank=True, null=True, verbose_name='sender_email'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sender_mobileNo',
            field=models.TextField(blank=True, null=True, verbose_name='sender_mobileNo'),
        ),
    ]
