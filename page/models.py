from django.db import models
from django.contrib.admin import ModelAdmin
from django import forms
# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()
class contactadmin(ModelAdmin):
    list_display = ('name','email','subject','message',)
    list_filter = ('name',)
    search_fields = ['name',]