__author__ = 'rt'
from django.conf.urls import url, include

from shipping import models, views
from .views import *
from django.contrib.auth import views as auth_views

from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
        url(r'^$', views.Index, name='index'),
##        url(r'^sign/$', TemplateView.as_view(template_name='my_template.html')),
        url(r'^sign/$',  views.my_view, name='my_view'),
        url(r'^sender/$', views.sender, name='sender'),
        url(r'^carrier/$', views.carrier, name='carrier'),
        url(r'^reciver/$', views.reciver, name='reciver'),
        url(r'^document/(?P<slug>[\w\-]+)$', views.document, name='document'),
        url(r'^signup/$', views.signup, name='signup'),
        url(r'^sendgoods/$', views.sendgoods, name='sendgoods'),
        url(r'^password_reset/$', auth_views.password_reset, name='password_reset'),
        url(r'^password_reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
        url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.password_reset_confirm, name='password_reset_confirm'),
        url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),
        #url(r'^success', views.success, name='success'),
        url(r'^transfer/(?P<slug>[\w\-]+)/$', views.transfer, name='transfer'),
        url(r'^sendmail/(?P<slug>[\w\-]+)/$', views.sendmail, name='sendmail'),
        url(r'^delivergoods/(?P<slug>[\w\-]+)/$', views.delivergoods, name='delivergoods'),

#        url(r'^carrier/(?P<slug>[\w\-]+)/(?P<otp>[\w\-]+)$', views.carrier, name='carrier'),
#        url(r'^reciver/(?P<slug>[\w\-]+)/(?P<otp>[\w\-]+)$', views.reciver, name='reciver'),
        url(r'^designation/$', views.designation, name='designation'),
       ]
