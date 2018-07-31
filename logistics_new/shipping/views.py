# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render, redirect
from .models import *
from loguser.models import *
import datetime
from datetime import datetime, timedelta, time
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
import random
from jsignature.utils import draw_signature
##from somewhere import handle_uploaded_file
from django.views.generic.base import View
from django.core.files.storage import FileSystemStorage
import os

##from django.db.models import Q
##
##Item.objects.filter(Q(creator=owner) | Q(moderated=False))

from jsignature.utils import draw_signature

def my_view(request):
    form = SignatureForm(request.POST or None)
    print "going to enter into ifs"
    if  request.method == 'POST':
        print "post method"
        print "form", form
        if form.is_valid():
            print "form valid"
            signature = form.cleaned_data.get('signature')
            print "signature form"
            if signature:
                print "entered signature"
                # as an image
                signature_picture = draw_signature(signature)

                #if os.direxists(os.path.join(os.getcwd()),username = request.user):
                #    os.mkdir(os.path.join(os.getcwd())+ request.user,signature_picture)
                # or as a file
                signature_file_path = draw_signature(signature, as_file=True)
                
    else:
        print "else"
        return render(request, 'my_template.html',{'form':form})
            
# Create your views here.
@login_required  
def Index(request):
    user = User.objects.get(username = request.user)
    print "user", user.id
    if Employee.objects.filter(user_id = user.id):
        employee = Employee.objects.get(user_id = user.id)
        designation = employee.designation
        if designation == "sender":
            trans = Transaction.objects.filter(sender = user.id)#filter(sender = user.id)
        elif designation == "carrier":
            trans = Transaction.objects.filter(carreir = user.id)#filter(sender = user.id)
        elif designation == "reciver":
            trans = Transaction.objects.filter(reciver = user.id)#filter(sender = user.id)
        else:
            pass
        context_dict = {'trans' : trans}
        return render(request, 'select-desg.html', context_dict)

    else:
        print "else"
        done = False
        if request.method == 'POST':
            try:
                print "entering designation"
                designation = request.POST['designation']
                print "designation", designation
                user_id = user.id
                print "user", user
                employee_desig = Employee.objects.create(designation = designation, user = user)
                print "employee added"
                done = True
                return HttpResponseRedirect("/")
            except Exception,e:
                print "errors", e
        else:
            return render(request, 'designation.html',{'done' : done})

def sendmail(request, slug):
    print "slug", slug
    trans = Transaction.objects.get(id = slug)
    if trans.carrier_ack == True:
        pass
    else:
        carrier = trans.carreir    
        user = User.objects.get(username = carrier)

        mail = user.email
        otp = random.randint(0000,9999)
        print "otp", otp
        subject = "confirmatin of goods recived"
        from_email, to = "nithinrushik69@gmail.com", mail
        print "to mail", mail
        text_content = 'Text'
        html_content = 'Open the link to activate that you had reciverd  the cargo 127.0.0.1:8000/carrier/'+slug+'/'+str(otp)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        trans.carreir_otp = otp
        trans.carrier_ack = True
        trans.save()
        return render(request, 'success.html')


def delivergoods(request, slug):
    trans = Transaction.objects.get(id = slug)
    if trans.reciver_ack == True:
        pass
    else:
        reciver = trans.reciver    
        user = User.objects.get(username = reciver)

        mail = user.email
        otp = random.randint(0000,9999)
        print "otp", otp
        subject = "confirmatin of goods recived"
        from_email, to = "nithinrushik69@gmail.com", mail
        print "to mail", mail
        text_content = 'Text'
        html_content = 'Open the link to activate that you had reciverd  the cargo 127.0.0.1:8000/reciver/'+slug+'/'+str(otp)
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        trans.reciver_otp = otp
        trans.reciver_ack = True
        trans.save()
        return render(request, 'success.html')



@login_required  
def sender(request):        
    user = User.objects.get(username = request.user)
    employee = Employee.objects.get(user_id = user.id)
    designation = employee.designation
    print "designation", designation
    trans = Transaction.objects.filter(sender = user.id)#filter(sender = user.id)
    print "trans", trans
    context_dict = {'trans' : trans}
    return render(request, 'sender.html', context_dict)

@login_required  
def carrier(request):        
    user = User.objects.get(username = request.user)
    employee = Employee.objects.get(user_id = user.id)
    designation = employee.designation
    print "designation", designation
    trans = Transaction.objects.filter(carreir = user.id)#filter(sender = user.id)
    print "trans", trans
    context_dict = {'trans' : trans}
    return render(request, 'carrier.html', context_dict)


@login_required  
def reciver(request):        
    user = User.objects.get(username = request.user)
    employee = Employee.objects.get(user_id = user.id)
    designation = employee.designation
    print "designation", designation
    trans = Transaction.objects.filter(reciver = user.id)#filter(sender = user.id)
    print "trans", trans
    context_dict = {'trans' : trans}
    return render(request, 'reciver.html', context_dict)

##@login_required  
##def sender(request):        
##    user = User.objects.get(username = request.user)
##    employee = Employee.objects.get(sender = user.id)
##    designation = employee.designation
##    print "designation", designation
##    trans = Transaction.objects.filter(sender = user.id)#filter(sender = user.id)
##    print "trans", trans
##    context_dict = {'trans' : trans}
##    return render(request, 'select-desg.html', context_dict)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/accounts/login/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required 
def designation(request):
    user = User.objects.get(username = request.user)
    employee = Employee.objects.get(user = user)
    designation = employee.designation
    print "designation", designation
    if designation == "":
##        if request.method == 'POST':
##            form = SignUpForm(request.POST)
##            if form.is_valid():
##                form.save()
        print "designation is"

    else:
        return HttpResponseRedirect("/")

def transfer(request, slug):
    user = User.objects.get(username = request.user)
    employee = Employee.objects.get(user = user)
    designation = employee.designation
    print "designation", designation
    carriers_list = Employee.objects.filter(designation = "carrier")
    user_id = user.id
    print "user_id", user_id
    carriers = User.objects.get(id = user_id)
    transaction = Transaction.objects.get(id = slug)
    done = False
    if request.method == 'POST':
        try:
            transfer_to = request.POST['designation']
            image_doc = request.POST['image_doc']
            print "transfer_to", transfer_to
            transfer = Transfer.objects.create(transaction = transaction, carrier_transfer_from = carriers, carreir_transfer_to = User.objects.get(id=transfer_to), image_doc = image_doc)
            transaction = Transaction.objects.filter(id = slug)
            transaction.update(carreir = User.objects.get(id=transfer_to))
            print "Transfer is sucessfull"
            done = True
            return render(request, 'success.html',{})
        except Exception,e:
            print "errors", e
    else:
        return render(request, 'transfer.html',{'done' : done, 'carriers_list' : carriers_list, 'slug' : slug, 'transaction' : transaction})


##def sendmail(request, slug):
##    otp = random.randint(0000,9999)
##    print "otp", otp
##    subject = "confirmatin of goods recived"
##    from_email, to = "nithinrushik69@gmail.com", "nithinsaikumar25@gmail.com"
##    text_content = 'Text'
##    html_content = 'Open the link to activate that you had reciverd  the cargo 127.0.0.1:8000/carrier/'+slug+'/'+str(otp)
##    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
##    msg.attach_alternative(html_content, "text/html")
##    msg.send()
##    carrier = Carrier.objects.filter(id  = slug).order_by('-id')[0]
##    carrier.sender_otp = otp
##    carrier.save()
##    
##    return render(request, 'success.html')


##def carrier(request, slug, otp):
##    nowtime = datetime.now()
##    print nowtime
##    carrier = Carrier.objects.filter(id  = slug).order_by('-id')[0]
##    if carrier.sender_otp == otp: 
##        carrier.time_of_taken = nowtime
##        carrier.save()
##        rotp = random.randint(0000,9999)
##        print type(carrier)
##        cr = Reciver.objects.filter(carrier = slug).order_by('-id')[0]
##        cr.carrier_otp = rotp
##        cr.save()
##        cr_id = cr.id
##        cr_name = cr.reciver_name
####        reciver = Reciver.objects.filter(id = cr_id)
##        subject = "confirmatin of goods recived by "+str(cr_name)
##        from_email = "nithinrushik69@gmail.com"
##        to = "nithinsaikumar69@gmail.com"
##        text_content = 'Text'
##        html_content = """please check the goods that are delivered to you are in sound and good condition and then click the below link \n
##                        127.0.0.1:8000/reciver/"""+str(cr_id)+"""/"""+str(rotp)
##        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
##        msg.attach_alternative(html_content, "text/html")
##        msg.send()
##        return render(request, 'success.html')
##    else:
##        return render(request, 'sorry.html')


##def reciver(request, slug, otp):
##    nowtime = datetime.now()
##    print nowtime
##    reciver = Reciver.objects.filter(id  = slug).order_by('-id')[0]
##    if reciver.carrier_otp == otp:
##        form = SignatureForm(request.POST or None)
##        if form.is_valid():
##            signature = form.cleaned_data.get('signature')
##            if signature:
##                # as an image
##                signature_picture = draw_signature(signature)
##                # or as a file
##                signature_file_path = draw_signature(signature, as_file=True)
##        reciver.updated_on = nowtime
##        reciver.carrier.time_of_delevered = nowtime
##        reciver.save()
##        return render(request, 'thanks.html')
##    else:
##        return render(request, 'sorry.html')

def document(request, slug):
    documents  = Transaction.objects.get(id = slug)
    items = Item.objects.filter(transaction = slug)
    transfers = Transfer.objects.filter(transaction = slug)

    print "%%%%%%%%%%%", transfers
    return render(request, 'document_details.html',{'documents':documents, 'items':items, 'transfers':transfers})


def sendgoods(request):
    user = User.objects.get(username = request.user)
    employee = Employee.objects.get(user_id = user.id)
    designation = employee.designation
    print "designation", designation
    carriers = Employee.objects.filter(designation = "carrier")
    recivers = Employee.objects.filter(designation = "reciver")    

    done = False
    if request.method == "POST":
        form = DocumentForm(request.POST, request.FILES)
        # print "request.FILESrequest.FILESrequest.FILESrequest.FILES"
        print request.FILES
        if form.is_valid():
            newdoc = Document(image_doc = request.FILES['image_doc'])
            print newdoc
            newdoc.save()
            sender = user
            carrier = request.POST['carrier']
            reciver = request.POST['reciver']
            from_loc = request.POST['transfer_from']
            to_loc = request.POST['transfer_to']
            document = Document.objects.all().order_by('-id')[0]
            transaction_create = Transaction.objects.create(transaction_from = from_loc, transaction_to = to_loc, reciver = User.objects.get(employee__id = reciver), carreir = User.objects.get(employee__id = carrier), document = document, sender = sender)
            transaction_create.save()
            done = True
            return HttpResponseRedirect("/sender/")
    else:
        form = DocumentForm()

    return render(request, 'shipper/sendgoods.html',{'form':form, 'done' : done, 'carriers' : carriers, 'recivers' : recivers})

##        carrier = request.POST['carrier']
##        vehicle = request.POST['vehicle']
##        reciver = request.POST['reciver']
##        shipper = user
##        transaction_create = Transaction.objects.create(reciver = reciver, carrier = carrier, vehicle = vehicle, shipper = shipper)
    
##    else:
##        print "GETTTT "

     #{'carrier_form':carrier_form, 'vehicle_form': vehicle_form, 'reciver_form' : reciver_form })


##    if request.method == "POST":
##        transaction_form = TransactionForm(data=request.POST)
##        try:
##            if transaction_form.is_valid():
##                TransactionForm = transaction_form.save()
##        except Exception,e:
##            print "c1 errors", e  



##def sendgoods(request):
##    user = User.objects.get(username = request.user)
##    print type(user)
##    user = user.id
##    shipper = Shipper.objects.get(id = user)
##    done = False
##    if request.method == "POST":
####        try:
####            print "12"
####            carrier_form = CarrierForm(data=request.POST)
####            print "13"
####            vehicle_form = VehicleForm(data=request.POST)
####            print "14"
####            reciver_form = ReciverForm(data=request.POST)
####            print "15"
####            print "carrier_form", carrier_form
####            if carrier_form.is_valid():
####                print "1"
####                #carrier = carrier_form.save()
##            try:
##                carrier_name = request.POST['carrier_name']
##                mail_id = request.POST['mail_id']
##                phone = request.POST['phone']
##                
##                print "2"
##                vehicle_no = request.POST['vehicle_no']
##                print "3"
##                vehicle_name = request.POST['vehicle_name']
##                print "4"
##                registered_on = request.POST['registered_on']
##                print "5"
##                licence_no = request.POST['licence_no']
##                print "6"
##                reciver_name = request.POST['reciver_name']
##                print "7"
##                rec_mail_id = request.POST['rec_mail_id']
##                print "8"
##                rec_phone = request.POST['rec_phone']
##                print "9"
##                carrier_create = Carrier.objects.create(carrier_name = carrier_name, mail_id = mail_id, phone = phone)
##                print "12"
##                carrier = Carrier.objects.last()
##                carrier.shipper = shipper
##                carrier.save()
##                vehicle_create = Vehicle.objects.create(vehicle_no = vehicle_no, vehicle_name=vehicle_name, registered_on=registered_on, licence_no=licence_no)
##                print "10"
##                carrier = Carrier.objects.all().order_by('-id')[0]
##                vehicle = Vehicle.objects.last()
##                vehicle.carrier = carrier
##                vehicle.save()
##                reciver_create = Reciver.objects.create(reciver_name=reciver_name, mail_id=rec_mail_id, phone=rec_phone)
##                print "11"
##                reciver = Reciver.objects.last()
##                reciver.carrier = carrier
##                reciver.save()
##                print "saved"
##                done = True
####                carrier = carrier_form.save()
##            except Exception,e:
##                print "c1 errors", e  
####        except Exception,e:
####            print "c1 errors", e  
##
##    else:
##        print "GETTTT "
####    carrier_form = CarrierForm()
####    vehicle_form = VehicleForm()
####    reciver_form = ReciverForm()
####
####    entries = Vehicle.objects.last()
##
##    return render(request, 'shipper/sendgoods.html',{'done' : done})
##     #{'carrier_form':carrier_form, 'vehicle_form': vehicle_form, 'reciver_form' : reciver_form })
    

##def sendmail(request, slug):
##    subject = "confirmatin of goods recived"
##    message = """
##Hello there!
##
##I wanted to personally write an email in order to welcome you to our platform.\
## We have worked day and night to ensure that you get the best service. I hope \
##that you will continue to use our service. We send out a newsletter once a \
##week. Make sure that you read it. It is usually very informative.
##
##Cheers!
##
##<a href = "linkk"> as</a>
##
##~ Nithin
##    """
##    from_email = ['nithinrushhik69@gmail.com']
##    if subject and message and from_email:
##        try:
##            send_mail(subject, message, from_email, ['nithinsaikumar25@gmail.com'])
##        except Exception as e:
##            print "error is: ", e
##            return HttpResponse('Invalid header found.')
##        return render(request, 'success.html')
##    else:
##        return HttpResponse('Make sure all fields are entered and valid.')
##    return HttpResponse("/")
##




##def success(request):
##    #email = request.POST.get('email', '')
##    email = ['nithinsaikumar69@gmail.com']
##    data = """
##Hello there!
##
##I wanted to personally write an email in order to welcome you to our platform.\
## We have worked day and night to ensure that you get the best service. I hope \
##that you will continue to use our service. We send out a newsletter once a \
##week. Make sure that you read it. It is usually very informative.
##
##Cheers!
##~ Yasoob
##    """
##    send_mail('Welcome!', data, "Yasoob",
##              [email], fail_silently=False)
##    return render(request, 'success.html')
