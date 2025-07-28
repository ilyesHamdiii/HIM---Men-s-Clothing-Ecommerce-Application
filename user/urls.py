from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings




app_name='user'
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup_view'),
    path('signout/', views.signout_view, name='signout_view'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
