from django.shortcuts import render
from .models import  Product

# Create your views here.
def home(request):
    return render(request,"store/home.html",{})
""" def about(request):
    return render(request,"store/about.html") """
def test(request):
    return render(request,"store/base.html")
def about(request):
    return render(request,"store/about.html")
def men(request):
    return render(request,"store/men.html")
def women(request):
    return render(request,"store/women.html")
def detail(request):
    Products=Product.objects.all()
    return render(request,"store/detail.html",{"products":Products})