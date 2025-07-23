from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('cart/', views.cart_view,name="cart_view"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


