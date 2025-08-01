from django.shortcuts import render,redirect
from django.contrib.sessions.models import Session
from store.models import Product,Size
from .models import CartItem,WishItem
from django import template
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST             
from django.contrib.auth.decorators import login_required     


app_name='cart'

# Create your views here.
@login_required
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

@csrf_exempt
@login_required
def add_to_cart(request,product_id):
    sizee = request.GET.get("size", "")
    if sizee:
        try:
            size_obj = Size.objects.get(name=sizee)
        except Size.DoesNotExist:
            size_obj = None
    else:
        size_obj = None

    qt = request.GET.get("quantity", "")
    print(sizee)
    print("User:", request.user)
    product=Product.objects.get(id=product_id)
    cart_item,created=CartItem.objects.get_or_create(product=product,user=request.user,size=size_obj.name)
    print(type(qt))
    if qt:
        cart_item.quantity+=int(qt)
    else:
        cart_item.quantity+=1
    cart_item.save()
    return redirect("cart:view_cart")

@csrf_exempt
@login_required
def add_to_wish(request,product_id):
     
    print("User:", request.user)
    product=Product.objects.get(id=product_id)
    wish_item,created=WishItem.objects.get_or_create(product=product,user=request.user)

    wish_item.save()
    return redirect("cart:wishlist")
@csrf_exempt
@login_required
def remove_from_cart(request,product_id):
    cart_item=CartItem.objects.filter(id=product_id).first()
    if cart_item:
        cart_item.delete()
    return redirect("cart:view_cart")
@csrf_exempt
@login_required
def remove_from_wish(request,product_id):
    wish_item=WishItem.objects.filter(id=product_id).first()
    if wish_item:
        wish_item.delete()
    return redirect("cart:wishlist")
@csrf_exempt
@login_required
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
@login_required
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
 
stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
@login_required
def create_checkout_session(request):
    if request.method == 'POST':
        # Example: get cart total from session or database
        cart_items = CartItem.objects.filter(user=request.user)
        amount = sum(item.product.price * item.quantity for item in cart_items)
        amount = int(amount * 100)
        line_items=[]
        for item in cart_items:
            line_items.append({
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': item.product.name,
                        'description': item.product.description or '',
                        "images":[item.product.image_url1]
                    },
                    'unit_amount': int(item.product.price * 100),  # price in cents
                },
                'quantity': item.quantity,
            })

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url='http://127.0.0.1:8000/checkout_success/',
            cancel_url='http://127.0.0.1:8000/checkout_cancel/',
        )
        return redirect(session.url, code=303)
@login_required
def checkout_success(request):
    print("COOKIES:", request.COOKIES)
    print("SESSION KEY:", request.session.session_key)
    print("User:", request.user, "Authenticated:", request.user.is_authenticated)
    CartItem.objects.filter(user=request.user).delete()
    return render(request, 'cart/success.html', {
        "cart_items": [],
        "total_price": 0,
        "sub_total": 0,
        "product_price": []
    })

@login_required
def checkout_cancel(request):
    return render(request, 'store/home  .html', {
        "cart_items": [],
        "total_price": 0,
        "sub_total": 0,
        "product_price": []
    })
def wishlist(request):
    cart_items=WishItem.objects.filter(user=request.user)
    quantity=request.POST.get('quantity')
    print(request.POST)
    print(quantity)

    total_price=sum(item.product.price * item.quantity for item in cart_items)
    product_price=[str(item.product.price * item.quantity) for item in cart_items]
    print(product_price)
    #n=len(product_price)
    
    sub_total=(total_price/100)*120
    return render(request,"cart/wish.html",{"cart_items":cart_items,"total_price":total_price,"sub_total":sub_total,"product_price":product_price})