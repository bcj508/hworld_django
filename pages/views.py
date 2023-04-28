#from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def homePageView(request):
    return HttpResponse("w00t! this is a test")
