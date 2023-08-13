from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

# Create your views here.
def checkout_view(request):

    return render(request,"menu/checkout.html")
    