from django.shortcuts import render
from .models import  Product,Category
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
def home(request):
    return render(request,"store/home.html",{})
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
def store_cat(request,slug):
    category=Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category).order_by('id')
    paginator = Paginator(products,20)  
    page_number = request.GET.get('page')  
    page_obj = paginator.get_page(page_number)




    print(category)
    categories=Category.objects.all()
    context={
        "page_obj": page_obj, 
        "categories": categories,
        "selected_category": category,

    }
    return render(request, "store/shop.html", context)


def store_cat2(request,slug):
    price = request.GET.get("price")
    products=Product.objects.filter(price=price)
    context={
        "products":products,
    }
    return render(request,"store/shop.html",context) 