from django.shortcuts import render,redirect
from .models import items , drinks,lunch,dinner,composes
from django.contrib.auth.decorators import login_required


def item(request):
    
    return render(request,'menu/breakfast.html',{'item':items.objects.all()})



def itemdrinks(request):
    
    return render(request,'menu/drinks.html',{'itemdrinks':drinks.objects.all()})



def itemlunch(request):
    
    return render(request,'menu/lunch.html',{'itemlunch':lunch.objects.all()})


def itemdinner(request):
    
    return render(request,'menu/dinner.html',{'itemdinner':dinner.objects.all()})


def itemcompose(request):
    
    return render(request,'menu/composes.html',{'itemcompose':composes.objects.all()})

def checkout(request):
    
    return render(request,'menu/checkout.html')














    
    
    
    
