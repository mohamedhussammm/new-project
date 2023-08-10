from django.urls import path
from .import views

urlpatterns = [
    path('',views.item,name="item"),
    path('drinks/',views.itemdrinks,name="itemdrinks"),
    path('lunch/',views.itemlunch,name="itemlunch"),
    path('dinner/',views.itemdinner,name="itemdinner"),
    path('composes/',views.itemcompose,name="itemcompose"),
    path('checkout/',views.checkout,name="check"),
  



    
]
