# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 05:06
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carreir_transfer_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transfer_to', to=settings.AUTH_USER_MODEL, verbose_name='Transfer TO')),
                ('carrier_transfer_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='transfer_from', to=settings.AUTH_USER_MODEL, verbose_name='Transfer From')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shipping.Transaction', verbose_name='Transaction ID')),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='shipping_cost',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Unit Price'),
        ),
        migrations.AlterField(
            model_name='document',
            name='unit_price',
            field=models.FloatField(blank=True, null=True, verbose_name='Unit Price'),
        ),
    ]