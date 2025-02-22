from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .models import ServiceRequest
# Create your views here.
def home(request):
    return render(request,"index.html")

@login_required
def logoutt(request):
    logout(request)
    return redirect('home')

def loginn(request):
    if request.method=="POST":
        uname=request.POST['uname']
        passs=request.POST['pass']
        user=authenticate(request,username=uname,password=passs)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect("login")
    return render(request,"login.html")

def signupp(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        uname=request.POST['uname']
        passs=request.POST['pass']
        try:
            user=User.objects.create_user(first_name=fname,last_name=lname,email=email,username=uname,password=passs)
            return redirect('login')
        except Exception :
            return redirect('signup')
    return render(request,"signup.html")

def generate_request(request):
    if request.method=="POST":
        s_type=request.POST['service_type']
        desc=request.POST['desc']
        file = request.FILES.get('file')
        ServiceRequest.objects.create(user=request.user,service_type=s_type,description=desc,attachment=file)
        return redirect("home")

    return render(request,"generate_request.html")

def request_tracking_list(request):
    list=ServiceRequest.objects.all().filter(user=request.user)
    return render(request,'request_list.html',{'list':list})