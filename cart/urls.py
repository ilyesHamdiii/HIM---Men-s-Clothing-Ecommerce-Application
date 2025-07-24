from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
app_name='cart'

urlpatterns = [
    path('cart/', views.view_cart,name="view_cart"),
    path('add/<int:product_id>', views.add_to_cart,name="add_to_cart"),
    path('remove/<int:product_id>/', views.remove_from_cart,name="remove_from_cart"),



]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


