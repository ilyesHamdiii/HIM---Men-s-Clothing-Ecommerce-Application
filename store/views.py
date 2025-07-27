from django.shortcuts import render
from .models import  Product,Category
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from cart.views import view_cart
app_name='store'
def home(request):
    return render(request,"store/home.html",{
    })
""" def about(request):
    return render(request,"store/about.html") """
def store2(request):
    Products=Product.objects.all()
    return render(request,"store/shop.html",{"products":Products})



def test(request):
    return render(request,"store/base.html")
def about(request):
    return render(request,"store/about.html")
def men(request):
    return render(request,"store/men.html")
def women(request):
    return render(request,"store/women.html")


def detail(request,product_id):

    Products=Product.objects.get(id=product_id)
    print(Products)
    return render(request,"store/shop-details.html",{"products":Products})
def store(request):
    categorys=Category.objects.all()
    print(categorys)
    
    product_list = Product.objects.all().order_by('id')  
    paginator = Paginator(product_list,20)  

    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)

    context = {
    'page_obj': page_obj,
    'products': product_list,
    "categories": categorys,

    }
    return render(request, 'store/shop.html', context)
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
    }
    return render(request, "store/shop.html", context)

def store_cat2(request):
    products = Product.objects.all()

    min_price = request.GET.get("min")
    max_price = request.GET.get("max")

    if min_price:
        try:
            min_price = float(min_price)
            products = products.filter(price__gte=min_price)
        except ValueError:
            pass

    if max_price:
        try:
            max_price = float(max_price)
            products = products.filter(price__lte=max_price)
        except ValueError:
            pass

    paginator = Paginator(products, 20)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "store/shop.html", {
        "page_obj": page_obj,
        "categories": Category.objects.all(),
        "min_price": min_price,
        "max_price": max_price,
    })
