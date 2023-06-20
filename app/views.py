from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def char(request):
    return HttpResponse('<h1> Hello! How are U? </h1>')