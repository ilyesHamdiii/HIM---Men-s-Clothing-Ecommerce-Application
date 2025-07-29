from django.contrib import admin
from .models import Customer ,Order,OrderItem,Product,Category
from cart.models import CartItem,WishItem
# Register your models here.
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(CartItem)
admin.site.register(WishItem)
