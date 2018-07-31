# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from datetime import datetime
from django.contrib.auth.models import User#, AbstractUser
from cities_light.models import *
from cities_light.abstract_models import (AbstractCity, AbstractRegion, AbstractCountry)
from cities_light.receivers import connect_default_signals
from django.utils.translation import ugettext_lazy as _
# from  pytz


class Transaction(models.Model):
    weight_choices = (
        ('lB', 'LB'),
        ('kg', 'KG'),
        ('ton', 'TON'),
        ('pound', 'POUND'),
    )
    currency_choices = (
        ('UK', 'POUNT'),
        ('US', '$'),
        ('EUROPE', 'EURO'),
        ('INDIA', 'RUPEE'),
    )
    transaction_from = models.ForeignKey(City, verbose_name="Transaction From", related_name="transaction_from",
                                         null=True, blank=True)
    # currency = models.CharField(_('currency'), choices=currency_choices)
    currency = models.CharField(_('currency'), choices=currency_choices, max_length=20)
    weight = models.CharField(_('weight'), choices=weight_choices,max_length=20)

    transaction_to =  models.ForeignKey(City, verbose_name="Transaction To", related_name = "transaction_to", null=True, blank=True)
    sender_address=models.TextField(verbose_name="Sender Address", null=True, blank=True)
    sender_mobileNo=models.CharField(max_length=15,verbose_name="sender_mobileNo", null=True, blank=True)
    receiver_mobileNo=models.CharField(max_length=15,verbose_name="receiver_mobileNo", null=True, blank=True)
    carreir_mobileNo=models.CharField(max_length=15,verbose_name="carreir_mobileNo", null=True, blank=True)
    sender_email=models.CharField(max_length=120,verbose_name="sender_email", null=True, blank=True)
    receiver_email=models.CharField(max_length=120,verbose_name="receiver_email", null=True, blank=True)
    carreir_email=models.CharField(max_length=120,verbose_name="carrier_email", null=True, blank=True)

    receiver_address=models.TextField(verbose_name="Receiver address", null=True, blank=True)
    carrier_address=models.TextField(verbose_name="Carreir Address", null=True, blank=True)
##    transaction_from = models.CharField(max_length=20,null=True, blank=True, verbose_name="From Location")
##    transaction_to = models.CharField(max_length=20,null=True, blank=True, verbose_name="To Location")
    sender = models.ForeignKey(User, verbose_name="Sender", related_name = "sender_name", null=True, blank=True)
    carreir = models.ForeignKey(User, verbose_name="Carrier", related_name = "carrier_name", null=True, blank=True)
    reciver = models.ForeignKey(User, verbose_name="Reciver", related_name = "reciver_name", null=True, blank=True)
    shipping_cost = models.CharField(max_length=30,null=True, blank=True, verbose_name="Shipping Cost")
    shipping_item_name = models.CharField(max_length=20, null=True, blank=True, verbose_name="Shipping Item")
    shipping_weight = models.CharField(max_length=20, null=True, blank=True, verbose_name="Shipping Weight")
    shipping_quantity = models.CharField(max_length=20, verbose_name="Shipping Quantity", null=True, blank=True)
    summary = models.TextField(null=True, blank=True, verbose_name="Summary")
    image_doc = models.FileField(upload_to='media', null=True, blank=True, verbose_name="Document")
    carrier_ack = models.BooleanField(default=False)
    carrier_delivery_ack = models.BooleanField(default=False)
    reciver_ack = models.BooleanField(default=False)
    start_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    taken_time = models.DateTimeField(null=True, blank=True)
    delivered_time = models.DateTimeField(null=True, blank=True)
    carrier_otp = models.CharField(max_length=5,null=True, blank=True, verbose_name="Carrier OTP")
    reciver_otp = models.CharField(max_length=5,null=True, blank=True, verbose_name="Reciver OTP")
    # pro_pic = models.ImageField(upload_to='media', null=True, blank=True, verbose_name="Pro Pic")
    sender_sign=models.ImageField(upload_to='media',null=True, blank=True, verbose_name="Sender_Sign")
    reciver_sign=models.ImageField(upload_to='media',null=True, blank=True, verbose_name="Receiver_Sign")




    def __unicode__(self):
        return str(self.id)  


class Item(models.Model):
    item_name = models.CharField(max_length=20, null=True, blank=True, verbose_name="Item Name")
    weight = models.CharField(max_length=20, null=True, blank=True, verbose_name="Weight")
    unit_price = models.FloatField(null=True, blank=True, verbose_name="Unit Price")
    quantity = models.CharField(max_length=20, verbose_name="Quantity", null=True, blank=True)
    value = models.CharField(max_length=20, verbose_name="Value",  null=True, blank=True)
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    def __unicode__(self):
        return str(self.id)


class Transfer(models.Model):
    transaction = models.ForeignKey(Transaction, verbose_name="Transaction ID" )
    carrier_transfer_from = models.ForeignKey(User, verbose_name="Transfer From", related_name = "transfer_from", null=True, blank=True)
    carreir_transfer_to = models.ForeignKey(User, verbose_name="Transfer TO", related_name = "transfer_to", null=True, blank=True)
    image_doc = models.FileField(upload_to='media', null=True, blank=True, verbose_name="Document")
    def __unicode__(self):
        return str(self.id)  
# Create your models here.

##class Shipper(models.Model):
##    shipper_name = models.CharField(max_length=30, verbose_name="Shipper Name")
##    mail_id = models.CharField(max_length=80, verbose_name="Mail Id")
##    phone = models.CharField(max_length=10, null=True, blank=True, verbose_name="Phone No.")
##    time_of_sent = models.DateTimeField(null=True, blank=True)
##    mail_status =  models.BooleanField(default=False)
##
####    #carrier = models.ForeignKey(Carrier)
##    
##    def __unicode__(self):
##        return self.shipper_name
##
##class Carrier(models.Model):
##    carrier_name = models.CharField(max_length=30, verbose_name="Carrier Name")
##    mail_id = models.CharField(max_length=80, verbose_name="Mail Id")
##    phone = models.CharField(max_length=10, verbose_name="Phone No.")
##    time_of_taken = models.DateTimeField(null=True, blank=True)
##    time_of_delivered = models.DateTimeField(null=True, blank=True)
##    added_by = models.ForeignKey(Shipper, null=True, blank=True)
##    mail_status =  models.BooleanField(default=False)
##    sender_otp = models.CharField(max_length=6, null=True, blank=True, verbose_name="OTP of Sender")
##    def __unicode__(self):
##        return self.carrier_name



##class Vehicle(models.Model):
##    vehicle_no = models.CharField(max_length=10,null=True, blank=True, verbose_name="Vehicle No.")
##    vehicle_name = models.CharField(max_length=30,null=True, blank=True, verbose_name="Vehicel Name")
##    registered_on = models.CharField(max_length=30,null=True, blank=True, verbose_name="Registered Name")
##    licence_no = models.CharField(max_length=30,null=True, blank=True, verbose_name="Licence No.")
##    carrier = models.ForeignKey(Carrier, null=True, blank=True)
##
##    def __unicode__(self):
##        return self.vehicle_no

##class Reciver(models.Model):
##    reciver_name = models.CharField(max_length=30, verbose_name="Reciver Name")
##    mail_id = models.CharField(max_length=80, verbose_name="Mail Id")
##    phone = models.CharField(max_length=10, verbose_name="Phone No.")
##    updated_on = models.DateTimeField(null=True, blank=True)
##    added_by = models.ForeignKey(Shipper,null=True, blank=True)
##    carrier_otp = models.CharField(max_length=6, verbose_name="OTP of Carrier")    
##    def __unicode__(self):
##        return self.reciver_name
