from django.urls import path
from . import views

urlpatterns = [
    path('admin-redirect/', views.admin_redirect, name='admin_redirect'),
]