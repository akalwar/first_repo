from django.shortcuts import render
#creating first view for pages app
from django.http import HttpResponse

def homepageview(request):
    return HttpResponse('Hello world!!! Welcome to my first website')
