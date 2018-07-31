# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-25 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0011_auto_20180725_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='document',
        ),
        migrations.AddField(
            model_name='transaction',
            name='image_doc',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='shipping_cost',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='shipping_cost'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='summary',
            field=models.TextField(blank=True, null=True, verbose_name='Summary'),
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
