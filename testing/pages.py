
import imp
import re
from django.http import HttpResponse
from django.shortcuts import render
from .form import ContactForm


def HomePage(request):
    a = {
        "first" : "pouya is here"
    }
    return render(request , "home.html" ,a )


def AboutMe(request) :
    return HttpResponse("ok this is me")  


def Contact(request) :
    contact_info = ContactForm(request.POST or None)
    data = {"form" : contact_info }

    if contact_info.is_valid():
    # if request.method == "POST" :
        # name = request.POST.get('fullname')
        # email = request.POST.get('email')
        # text = request.POST.get('message')
        # data = {
        #     "name" : name,
        #     "email" : email,
        #     "text" : text
        # }
        data = contact_info.cleaned_data
        return render(request , "show.html" , data )

    return render(request , "contact.html" , data)    

