# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 10:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0005_auto_20180723_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='image_doc',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
    ]
