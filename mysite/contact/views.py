from django.shortcuts import render
from django.shortcuts import HttpResponse

def main(request):
    return HttpResponse("Hello World! You are at Contact Page")

def sample(request,guess):
    response="Hey you passsed " + guess + ". Great!"+ "\n  Enjoy doing the changes!!"
    return HttpResponse(response)





# Create your views here.
