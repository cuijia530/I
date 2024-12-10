from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("欢迎您进入博客系统")

def user_list(request):
    return render(request,"user_list.html")

def user_add(request):
    return HttpResponse("添加用户")

def runoob(request):
    context = {}
    context['hello'] = 'Hello World'
    return render(request,'index.html' , context)