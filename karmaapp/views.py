from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('hello world')
    #return render(request,'index.html')
