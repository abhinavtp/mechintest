from django.shortcuts import render
from urllib import request

# Create your views here.

def index(request):
    return render(request,'seller/index.html')

def calc(request):
    return render(request,'seller/calc.html')
