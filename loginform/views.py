from imaplib import _Authenticator
from django.shortcuts import redirect, render
from .models import Login
from register.models import signuppage

def index(request):
    if request.method=="POST":
    
     username=request.POST.get("username")
     password=request.POST.get("password")
     res = signuppage.objects.filter(username = username, password = password)
     print(res.count()>0)
     if res.count()>0:
        return render(request,'home/')        

    #  data=Login(username=username,password=password)
    #  data.save()
    
    return render(request,'loginform/index.html')