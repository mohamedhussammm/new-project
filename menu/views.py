from django.shortcuts import render,redirect
from .models import items , drinks,lunch,dinner,composes,Cart,CartItem
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json


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


def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = drinks.objects.get(id=product_id)
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created =CartItem.objects.get_or_create(cart=cart, drink=product)
        cartitem.quantity += 1
        cartitem.save()
    return JsonResponse("working", safe=False)

    














    
    
    
    
