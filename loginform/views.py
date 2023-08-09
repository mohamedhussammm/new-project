from imaplib import _Authenticator
from django.shortcuts import redirect, render
from .models import Login
from register.models import signuppage
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
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
      return redirect('/')  
     else:
      return render(request,'loginform/index.html')
    else:
      return render(request,'loginform/index.html')
    
def logout_view(request):
    logout(request)
    return redirect('register')

    #  res = signuppage.objects.filter(username = username, password = password)
    #  print(res.count()>0)
    #  if res.count()>0:
        # return render(request,'home/')  
           
    #  data=Login(username=username,password=password)
    #  data.save()