from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('',views.home,name='home'),
    path("test/",views.test),
    path("about/",views.about,name="about"),
    path("men/",views.men,name="men"),
    path("women/",views.women,name="women"),
    path("product/<int:product_id>/",views.detail,name="product_detail"),
    
    path("shop",views.store)
   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)