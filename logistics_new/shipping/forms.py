from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from jsignature.forms import JSignatureField
from loguser.models import *
from django import forms
from jsignature.forms import JSignatureField

class SignatureForm(forms.Form):
    signature = JSignatureField()

    
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_staff', 'is_superuser')


# class MobileNumber(forms.ModelForm):
#     phone_number = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
#                                 error_message = ("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."))


##class DocumentForm(forms.ModelForm):
##
##    class Meta:
##        model = Document
##        # item_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
##        # weight = forms.CharField(max_length=30, required=False, help_text='Optional.')
##        # value = forms.CharField(max_length=30, required=False, help_text='Optional.')
##        # quantity = forms.CharField(max_length=30, required=False, help_text='Optional.')
##        unit_price = forms.FloatField(required=False, help_text='Optional.')
##        shipping_cost = forms.CharField(max_length=30, required=False, help_text='Optional.')
##        summary = forms.TextInput(attrs={'size': 10, 'title': 'Summary'})
##        image_doc = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
##        # fields = ('item_name','weight','value', 'quantity', 'unit_price', 'shipping_cost', 'summary', 'image_doc')
##        fields = '__all__'
##


class TransactionForm(forms.ModelForm):

    class Meta:
        model = Transaction
        fields = '__all__'
