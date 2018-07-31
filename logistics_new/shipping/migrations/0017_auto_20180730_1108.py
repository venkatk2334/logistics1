# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-30 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0016_auto_20180728_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='reciver_sign',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Receiver_Sign'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='sender_sign',
            field=models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Sender_Sign'),
        ),
    ]
