from django.shortcuts import render
from .models import  Product
from django.shortcuts import get_object_or_404
# Create your views here.
def home(request):
    return render(request,"store/home.html",{})
""" def about(request):
    return render(request,"store/about.html") """
def store(request):
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