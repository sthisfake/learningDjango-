
from django.http import HttpResponse
from django.shortcuts import render


def HomePage(request):
    return render(request , "home.html" ,{} )


def AboutMe(request) :
    return HttpResponse("ok this is me")  

