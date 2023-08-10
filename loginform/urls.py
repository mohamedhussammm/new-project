from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name="index"),
    path('',views.logout_view,name="logout"),
    

  
    
    
]  
