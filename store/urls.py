from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
app_name='store'
urlpatterns = [
    path('',views.home,name='home'),
    path("test/",views.test),
    path("about/",views.about,name="about"),
    path("men/",views.men,name="men"),
    path("women/",views.women,name="women"),
    path("product/<int:product_id>/",views.detail,name="product_detail"),
    path("store_cat/<slug:slug>/",views.store_cat,name="store_cat"),
    path("store_brand/<slug:slug>/",views.store_brand,name="store_brand"),
    path("store_cat2/",views.store_cat2,name="store_cat2"),
    path("about/",views.about,name="about"),
    path("blog/",views.blog,name="blog"),
    
    path("shop",views.store,name="shop"),
    path("",include('cart.urls'))

   
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)