from django.shortcuts import render,redirect
from django.contrib.sessions.models import Session
from store.models import Product
from .models import CartItem

app_name='cart'

# Create your views here.
def view_cart(request):
    cart_items=CartItem.objects.filter(user=request.user)
    quantity=request.POST.get('quantity')
    print(request.POST)
    print(quantity)

    total_price=sum(item.product.price * item.quantity for item in cart_items)
    sub_total=(total_price/100)*120
    return render(request,"cart/shopping-cart.html",{"cart_items":cart_items,"total_price":total_price,"sub_total":sub_total})
def add_to_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    cart_item,created=CartItem.objects.get_or_create(product=product,user=request.user)

    cart_item.quantity+=1
    cart_item.save()
    return redirect("cart:view_cart")
def remove_from_cart(request,product_id):
    cart_item=CartItem.objects.filter(id=product_id).first()
    if cart_item:
        cart_item.delete()
    return redirect("cart:view_cart")
def update_cart(request):
    if request.method=="POST":
        cart_items=CartItem.objects.filter(user=request.user)
        quantity=int(request.POST.get('quantity'))
        total_price=sum(item.product.price * quantity for item in cart_items)
        sub_total=(total_price/100)*120
        return render(request,"cart/shopping-cart.html",{"cart_items":cart_items,"total_price":total_price,"sub_total":sub_total})
    return redirect("cart:view_cart")
    
def checkout(request):
    return render(request,"cart/checkout.html")
 