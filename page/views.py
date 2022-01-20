
from django.shortcuts import render,redirect
from .formulaire import contactFormul
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    if request.method == 'POST':
        form = contactFormul(request.POST, request.FILES).save()
        return redirect('/home')
    else:
        form = contactFormul()

    return render(request,'contact.html',{'form': form})
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')
def one(request):
    return render(request,'one-page.html')