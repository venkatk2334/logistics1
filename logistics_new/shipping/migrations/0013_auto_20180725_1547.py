# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-25 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shipping', '0012_auto_20180725_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='shipping_item_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Shipping Item'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='shipping_quantity',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Shipping Quantity'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='shipping_weight',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Shipping Weight'),
        ),
        migrations.AlterField(
            model_name='item',
            name='transaction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shipping.Transaction'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='transaction',
            name='image_doc',
            field=models.FileField(blank=True, null=True, upload_to='media', verbose_name='Document'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='shipping_cost',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Shipping Cost'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_from',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='From Location'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_to',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='To Location'),
        ),
    ]
