from django.db import models
from store.models import Product
from django.contrib.auth.models import User

# Create your models here.
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)
    size=models.CharField(max_length=50,default="s")
    
    def __str__(self):
        return f"{self.quantity} * {self.product.name}"
class WishItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveBigIntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.quantity} * {self.product.name}"
