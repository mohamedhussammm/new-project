from django.shortcuts import render,redirect
from .models import signuppage
from imaplib import _Authenticator
from django .http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signup(request):
 
 if request.method=="POST":


    firstname=request.POST.get("firstname")
    lastname=request.POST.get("lastname")
    username=request.POST.get("username")
    phonenumber=request.POST.get("phonenumber")
    email=request.POST.get("email")
    password=request.POST.get("password")
    cpassword=request.POST.get("cpassword")
    nationalid=request.POST.get("nationalid")
    picture=request.POST.get("picture")
    
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = firstname
    user.last_name = lastname
    user.save()

    data= signuppage (firstname=firstname,lastname=lastname,phonenumber=phonenumber,email=email,password=password,cpassword=cpassword,nationalid=nationalid,picture=picture,username=username)
    data.save()

 return render (request,'register/signup.html')
 


     

   
