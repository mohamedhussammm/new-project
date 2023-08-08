from django.shortcuts import render

from django.shortcuts import redirect
def home(request):
    return render(request,'homepage.html')


def admin_redirect(request):
    return redirect('/admin')
