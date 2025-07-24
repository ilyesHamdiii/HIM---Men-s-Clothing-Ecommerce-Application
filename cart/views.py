from django.shortcuts import render,redirect
from django.contrib.sessions.models import Session
from store.models import Product
from .models import CartItem



# Create your views here.
def view_cart(request):
    cart_items=CartItem.objects.filter(user=request.user)
    total_price=sum(item.product.price * item.quantity for item in cart_items)
    sub_total=(total_price/100)*120
    return render(request,"cart/shopping-cart.html",{"cart_items":cart_items,"total_price":total_price,"sub_total":sub_total})
def add_to_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    cart_item,created=CartItem.objects.get_or_create(product=product,user=request.user)

    cart_item.quantity+=1
    cart_item.save()
    return redirect("cart:view_cart")
def remove_from_cart(request,item_id):
    cart_item=CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect(request,"cart:view_cart")