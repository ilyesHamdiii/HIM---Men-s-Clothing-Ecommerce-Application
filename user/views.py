from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from . import models 

# Create your views here.

app_name='user'
def login_view(request):
    if request.method == "POST":
        name = request.POST.get('uname')
        password = request.POST.get('upassword')
        userr = authenticate(request, username=name, password=password)
        if userr is not None:
            auth_login(request, userr) 
            return redirect('/login')
        else:
            return redirect('store:store_cat2')

    return render(request, "user/login.html")

def signup_view(request):
    error = None
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if not name:
            error = 'Username is required.'
        elif not email:
            error = 'Email is required.'
        elif not password1 or not password2:
            error = 'Both password fields are required.'
        elif password1 != password2:
            error = 'Passwords do not match.'
        else:
            newUser = User.objects.create_user(username=name, email=email, password=password1)
            newUser.save()
            return redirect('/login')
    return render(request, "user/signup.html", {'error': error})
@login_required
def signout_view(request):
    logout(request)
    return redirect("/login_view") 
