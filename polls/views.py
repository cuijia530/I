from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("HELLO,这是一个polls的网页")
