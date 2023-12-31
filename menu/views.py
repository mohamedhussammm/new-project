from django.shortcuts import render,redirect
from .models import items , drinks,lunch,dinner,composes,Cart,CartItem
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Checkout
import json
from django.http import JsonResponse
@csrf_exempt



def item(request):
    # print(items.objects(0))
    if request.method == "POST":
        y=request.body
        obj=json.loads(y)
        name = obj.get("name")
        components = obj.get("components")
        price = obj.get("price")
        images = obj.get("images")
        c1 = Checkout (name = name, components = components, price = price, images=images)
        c1.save()
    else:      
        return render(request,'menu/breakfast.html',{'item':items.objects.all()})


def itemdrinks(request):
    if request.method == "POST":
        y=request.body
        obj=json.loads(y)
        name = obj.get("name")
        components = obj.get("components")
        price = obj.get("price")
        images = obj.get("images")
        c1 = Checkout (name = name, components = components, price = price, images=images)
        c1.save()
    else:      
    
        return render(request,'menu/drinks.html',{'itemdrinks':drinks.objects.all()})


def itemlunch(request):
    if request.method == "POST":
        y=request.body
        obj=json.loads(y)
        name = obj.get("name")
        components = obj.get("components")
        price = obj.get("price")
        images = obj.get("images")
        c1 = Checkout (name = name, components = components, price = price, images=images)
        c1.save()
    else:      
    
        return render(request,'menu/lunch.html',{'itemlunch':lunch.objects.all()})


def itemdinner(request):
    if request.method == "POST":
        y=request.body
        obj=json.loads(y)
        name = obj.get("name")
        components = obj.get("components")
        price = obj.get("price")
        images = obj.get("images")
        c1 = Checkout (name = name, components = components, price = price, images=images)
        c1.save()
    else:      
         return render(request,'menu/dinner.html',{'itemdinner':dinner.objects.all()})


def itemcompose(request):
    if request.method == "POST":
        y=request.body
        obj=json.loads(y)
        name = obj.get("name")
        components = obj.get("components")
        price = obj.get("price")
        images = obj.get("images")
        c1 = Checkout (name = name, components = components, price = price, images=images)
        c1.save()
    else:
    
        return render(request,'menu/composes.html',{'itemcompose':composes.objects.all()})

def checkout(request):
    if request.method == "POST":
        y=request.body
        obj=json.loads(y)
        name = obj.get("name")
        components = obj.get("components")
        price = obj.get("price")
        images = obj.get("images")
        c1 = Checkout (name = name, components = components, price = price, images=images)
        c1.save()
    elif request.method=="GET" :
        result = Checkout.objects.all()
        print(result[0].images)
        print("ahmed")
        return render(request,"menu/checkout.html",{'items':result})
    
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

    






def menu_view(request):
    selected_items = ['item1', 'item2', 'item3']
    return redirect('checkout', items=selected_items)








    
    
    
    
