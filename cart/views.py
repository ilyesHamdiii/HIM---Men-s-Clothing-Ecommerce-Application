from django.shortcuts import render
from django.contrib.sessions.models import Session
# Create your views here.
def cart_view(request,product_id):

    return render(request,"cart/shopping-cart.html")