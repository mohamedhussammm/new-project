from django.contrib import admin
from .models import Checkout
from .models import items,drinks,lunch,dinner,composes,Cart,CartItem

admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(items)
admin.site.register(drinks)
admin.site.register(lunch)
admin.site.register(dinner)
admin.site.register(composes)
admin.site.register(Checkout)




