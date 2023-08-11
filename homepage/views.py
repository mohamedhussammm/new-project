from django.shortcuts import render
from django.shortcuts import redirect
from .models import photos
def home(request):
    return render(request,'homepage.html',{'home':photos.objects.all()})


def admin_redirect(request):
    return redirect('/admin')
