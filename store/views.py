from django.shortcuts import render,redirect
from .models import  Product,Category,Brand
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from cart.views import view_cart
from urllib.parse import urlencode
from django.db.models import Q
from django.urls import reverse
app_name='store'
def home(request):
    query=request.GET.get("search","")
    products=Product.objects.all()
    if query:
        base_url=reverse("store:shop")
        products=products.filter(Q(name__icontains=query) | Q(category__name__icontains=query))
        query_string=urlencode({"search":query})
        url=f"{base_url}?{query_string}"    

        return redirect(url)

    product10 = Product.objects.get(id=10)
    product2 = Product.objects.get(id=2)
    product3 = Product.objects.get(id=3)
    product4 = Product.objects.get(id=4)
    product5 = Product.objects.get(id=5)
    product6 = Product.objects.get(id=6)
    product7 = Product.objects.get(id=7)
    product8 = Product.objects.get(id=8)
    context = {
        'product10': product10,
        'product2': product2,
        'product3': product3,
        'product4': product4,
        'product5': product5,
        'product6': product6,
        'product7': product7,
        'product8': product8,
        

    }
    return render(request,"store/home.html",context)

def store2(request):
    Products=Product.objects.all()
    return render(request,"store/shop.html",{"products":Products})





def detail(request,product_id):

    Products=Product.objects.get(id=product_id)
    print(Products)
    return render(request,"store/shop-details.html",{"products":Products})
def store(request):
    order=request.GET.get("order")

    query = request.GET.get("search", "")
    color = request.GET.get("color")
    print(color)

    product_list = Product.objects.all()
    if color:
        product_list=product_list.filter(color=color)
        print(product_list)
    print('not color')

    if query:
        product_list = product_list.filter(Q(name__icontains=query) | Q(category__name__icontains=query))

    product_list = product_list.order_by('id')



    paginator = Paginator(product_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    brands = Brand.objects.all()
    if order=="High":
        product_list = product_list.order_by('price')
    else:
        product_list = product_list.order_by('-price')

    context = {
        "page_obj": page_obj,
        "products": product_list,
        "categories": categories,
        "brands": brands,
        "search_query": query 
    }

    return render(request, "store/shop.html", context)
def store_cat(request, slug):


    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)

    min_price = request.GET.get("min")
    max_price = request.GET.get("max")

    # Apply min price filter
    if min_price:
        try:
            min_price = float(min_price)
            products = products.filter(price__gte=min_price)
        except ValueError:
            pass

    # Apply max price filter
    if max_price:
        try:
            max_price = float(max_price)
            products = products.filter(price__lte=max_price)
        except ValueError:
            pass

    paginator = Paginator(products, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "page_obj": page_obj,
        "selected_category": category,
        "categories": Category.objects.all(),
        "min_price": min_price,
        "max_price": max_price,
        "brands": Brand.objects.all(),
    }
    return render(request, "store/shop.html", context)
def store_brand(request, slug):
    order=request.GET.get("order")

    brand = get_object_or_404(Brand, slug=slug)
    products = Product.objects.filter(brand=brand)

    min_price = request.GET.get("min")
    max_price = request.GET.get("max")

    # Apply min price filter
    if min_price:
        try:
            min_price = float(min_price)
            products = products.filter(price__gte=min_price)
        except ValueError:
            pass

    # Apply max price filter
    if max_price:
        try:
            max_price = float(max_price)
            products = products.filter(price__lte=max_price)
        except ValueError:
            pass
    if order=="High":
        products = products.order_by('price')
    else:
        products = products.order_by('-price')  
    

    paginator = Paginator(products, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "brands": Brand.objects.all(),
        "categories": Category.objects.all(),

        "min_price": min_price,
        "max_price": max_price,
    }
    return render(request, "store/shop.html", context)

def store_cat2(request):
    order = request.GET.get("order", "").lower()
    min_price = request.GET.get("min")
    max_price = request.GET.get("max")
    color = request.GET.get("color")

    product_list = Product.objects.all()

    if color:
        product_list = product_list.filter(color__name__iexact=color)

    if min_price:
        try:
            min_price = float(min_price)
            product_list = product_list.filter(price__gte=min_price)
        except ValueError:
            pass

    if max_price:
        try:
            max_price = float(max_price)
            product_list = product_list.filter(price__lte=max_price)
        except ValueError:
            pass

    # ✅ Apply sorting BEFORE pagination
    if order == "low":
        product_list = product_list.order_by("price")
    elif order == "high":
        product_list = product_list.order_by("-price")

    paginator = Paginator(product_list, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "store/shop.html", {
        "page_obj": page_obj,
        "categories": Category.objects.all(),
        "brands": Brand.objects.all(),
        "min_price": min_price,
        "max_price": max_price,
    })

def about(request):
    return render(request,"store/about.html")
def blog(request):
    return render(request,"store/blog.html")
def contact(request):
    return render(request,"store/contact.html")