from django.shortcuts import render
from django.http import HttpResponse
from .models import Credentials

def login(request):
    
    return render(request, 'login.html', {'message':message})
def signup(request):
    return render(request, 'login.html', {'message':messaage})
def login_click(request):
    return render(request,'login.html',{'message':message})
# Create your views here.
