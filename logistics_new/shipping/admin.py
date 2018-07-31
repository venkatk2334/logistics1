# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import *
from datetime import datetime, timedelta, time
from django.contrib import admin
from django.shortcuts import redirect
from loguser.models import *

class ItemInline(admin.TabularInline):
    model = Item

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id','transaction_from','transaction_to', 'sender','carreir')
    fields = ('transaction_from','transaction_to','sender', 'carreir','reciver','shipping_cost', 'shipping_item_name','shipping_weight','shipping_quantity','summary','image_doc',"sender_email","sender_mobileNo","sender_address","receiver_address","receiver_mobileNo","receiver_email","carrier_address","carreir_mobileNo","carreir_email","currency","weight")
##    readonly_fields = ('sender',)
    inlines = [
        ItemInline,
        ]





##    def formfield_for_foreignkey(self, db_field, request, **kwargs):
##        user = User.objects.get(username = request.user)
##        print "user", user.id
##        if Employee.objects.filter(user_id = user.id):
##            employee = Employee.objects.get(user_id = user.id)
##            designation = employee.designation
##            kwargs['initial'] = request.user.id
##        return super(TransactionAdmin, self).formfield_for_foreignkey(
##            db_field, request, **kwargs
##        )
##    
##    def save_model(self, request, obj, form, change):
##        if not obj.sender:
##            print "entered if condition"
##            obj.sender = request.user
##        else:
##            obj.sender = request.user
##        obj.save()

##    def save_model(self, request, instance, form, change):
##        user = request.user 
##        instance = form.save(commit=False)
##        sender = user
##        instance.save()
##        form.save_m2m()
##        return instance

    def response_add(self, request, obj, post_url_continue=None):
        return redirect('/')

    def response_change(request, obj):
        return redirect('/')


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Item)
admin.site.register(Transfer)
