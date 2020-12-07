from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import requests as req
from .models import *

# Create your views here.

def Login(request):
    if request.user.is_authenticated:
        return redirect("enter_url")
    error=None
    if request.method=="POST":
        data=request.POST
        username=data["username"]
        password=data["password"]
        usr=authenticate(username=username,password=password)
        if usr:
            login(request,usr)
            return redirect("enter_url")
        error=True
    dict={"error":error}
    return render(request,"login.html",dict)

def Register(request):
    if request.user.is_authenticated:
        return redirect("login")
    error=None
    if request.method=="POST":
        data=request.POST
        un=data["username"]
        ps=data["password"]
        r_ps=data["repeat_password"]
        email=data["email"]
        already_exist=User.objects.filter(username=un)
        if (not already_exist) and (r_ps==ps):
            usr=User.objects.create_user(un,email,ps)
            if usr:
                redirect("login")

        error=True
    dict={"error":error}
    return render(request,"login.html",dict)

def Show_Url(request):
    if not request.user.is_authenticated:
        return redirect("login")
    recent_query=URL.objects.all().order_by("-id")
    dict={"recent_queries":recent_query}
    return render(request,"show_url.html",dict)

def Enter_Url(request):
    if not request.user.is_authenticated:
        return redirect("login")
    data=None
    if request.method == "POST":
        data = request.POST
        url = data["url"]
        already_exist=URL.objects.filter(url=url)
        if not already_exist:
            if  req.get(url).text:
               URL.objects.create(url=url,content=data,usr=User.objects.get(username=request.user.username))
            else:
                data="Some Sites are not allowed to search on Python Anywhere platform." \
                     "You can add this site to the whitelist of python anywhere.com" \
                     "If you want to search then there are a lot whitelisted sites ." \
                     "visite https://www.pythonanywhere.com/whitelist/"
                URL.objects.create(url=url, content=data, usr=User.objects.get(username=request.user.username))
        data=URL.objects.get(url=url)
        #print(data)
        dict = {"data": data}
        return render(request,"show_url.html",dict)
    return render(request,"enter_url.html")

def Logout(request):
    if not request.user.is_authenticated:
        return redirect("login")
    logout(request)
    return redirect("login")

def Show_Web(request,q_id):
    return render(request,"show_web.html",{"data":URL.objects.get(id=q_id)})
