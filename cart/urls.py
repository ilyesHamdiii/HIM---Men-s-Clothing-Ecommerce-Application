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
    path('update_cart/', views.update_cart,name="view_update_cart"),
    path('add/<int:product_id>', views.add_to_cart,name="add_to_cart"),
    path('add-to-wish/<int:product_id>', views.add_to_wish,name="add_to_wish"),
    path('remove/<int:product_id>/', views.remove_from_cart,name="remove_from_cart"),
    path('remove-from-wish/<int:product_id>/',views.remove_from_wish,name="remove_from_wish"),
    path('checkout/', views.checkout,name="checkout"),
    path('create-checkout-sessions/',views.create_checkout_session,name='create_chekout_session'),
    path('checkout_success/',views.checkout_success,name='checkout_success'),
    path('checkout_cancel/',views.checkout_cancel,name='checkout_cancel'),
    path('wishlist/',views.wishlist,name='wishlist')




]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


