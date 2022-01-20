from .models import contact
from django.forms import ModelForm
from django import forms

class contactFormul(ModelForm):
    class Meta:
        model=contact
        widgets={
            'name':forms.TextInput(attrs={'placeholder':'Name'}),
            'email':forms.EmailInput(attrs={'placeholder':'Email'}),
            'subject':forms.TextInput(attrs={'placeholder':'Subject'}),
            'message':forms.TextInput(attrs={'placeholder':'Message'})
        }
        fields=['name','email','subject','message',]
