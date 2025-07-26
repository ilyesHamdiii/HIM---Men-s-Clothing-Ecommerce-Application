from django.shortcuts import render,redirect
from django.contrib.sessions.models import Session
from store.models import Product
from .models import CartItem
from django import template

app_name='cart'

# Create your views here.
def view_cart(request):
    cart_items=CartItem.objects.filter(user=request.user)
    quantity=request.POST.get('quantity')
    print(request.POST)
    print(quantity)

    total_price=sum(item.product.price * item.quantity for item in cart_items)
    product_price=[str(item.product.price * item.quantity) for item in cart_items]
    print(product_price)
    #n=len(product_price)
    
    sub_total=(total_price/100)*120
    return render(request,"cart/shopping-cart.html",{"cart_items":cart_items,"total_price":total_price,"sub_total":sub_total,"product_price":product_price})
def add_to_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    cart_item,created=CartItem.objects.get_or_create(product=product,user=request.user)

    cart_item.quantity+=1
    cart_item.save()
    return redirect("store:store_cat2")
def remove_from_cart(request,product_id):
    cart_item=CartItem.objects.filter(id=product_id).first()
    if cart_item:
        cart_item.delete()
    return redirect("cart:view_cart")
def update_cart(request):
    if request.method == "POST":
        cart_items = CartItem.objects.filter(user=request.user)
        for item in cart_items:
            qty_str = request.POST.get(f'quantity_{item.id}')
            if qty_str is not None:
                try:
                    qty = int(qty_str)
                    if qty > 0:
                        item.quantity = qty
                        item.save()
                    else:
                        item.delete() 
                except ValueError:
                    pass  
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        sub_total = (total_price / 100) * 120
        product_price = [str(item.product.price * item.quantity) for item in cart_items]
        return render(request, "cart/shopping-cart.html", {
            "cart_items": cart_items,
            "total_price": total_price,
            "sub_total": sub_total,
            "product_price": product_price
        })
    return redirect("cart:view_cart")
def checkout(request):
    lp=[]
    cart_items = CartItem.objects.filter(user=request.user)
    for i in range(len(cart_items)):
        lp.append(i)

    total_price = sum(item.product.price * item.quantity for item in cart_items)
    sub_total = (total_price / 100) * 120
    product_price = [str(item.product.price * item.quantity) for item in cart_items]
    return render(request, "cart/checkout.html", {
        "cart_items": cart_items,
        "total_price": total_price,
        "sub_total": sub_total,
        "product_price": product_price,
        "lp":lp
    })
 