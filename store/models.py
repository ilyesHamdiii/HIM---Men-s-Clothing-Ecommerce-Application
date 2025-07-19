from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    description=models.TextField()
    image=models.ImageField(upload_to="products/")
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
class Order(models.Model):
    user=models.CharField(max_length=100)
    items=models.CharField(max_length=100)
    date=models.DateField(auto_now_add=True)
    complete=models.BooleanField(default=False)
    transaction_id=models.IntegerField(max_length=100)
class OrderItem(models.Model):
    product=models.CharField(max_length=100)
    quantity=models.IntegerField()


