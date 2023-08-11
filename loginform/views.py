from imaplib import _Authenticator
from django.shortcuts import redirect, render
from .models import Login
from register.models import signuppage
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
def index(request):
    if request.method=="POST":
     global username, password
     username = request.POST.get("username")
     password=request.POST.get("password")
     user = authenticate(request, username=username, password=password)
     print(username)
     print(password)
     if user is not None:
      login(request, user)
      messages.success(request, 'You have been logged in.')
      # return redirect('index') 
      return render(request,'menu/breakfast.html')


      # return redirect('/')  
     else:
       messages.success(request, 'error please try again.')
       return render(request,'loginform/index.html')
    else:
     return render(request,'loginform/index.html')
    
def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('/')
    # return render(request,'loginform/index.html')

    

   