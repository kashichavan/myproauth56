from django.shortcuts import render,redirect,HttpResponse
from .forms import *
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def register(request):
    if request.method=='POST':
        u=User.objects.filter(username=request.POST['username'])
        if u.exists():
            messages.info(request,'username already exist')
            return redirect('/register/')
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
    f=RegisterForm()
    return render(request,'register.html',context={'form':f})

def login_view(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            user=authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user:
                login(request,user)
                return redirect(reverse('myapp:home'))
            else:
                messages.info(request,'Username or password is not valid')
                return redirect('/login/')
    f=LoginForm()
    return render(request,'login.html',context={'form':f})  
def home(request):
    return render(request,'home.html') 

def logout_view(request):
    logout(request,User)
    return redirect(reverse('myapp:login'))     



    
