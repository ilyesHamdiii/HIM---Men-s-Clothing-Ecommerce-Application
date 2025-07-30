from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name
class Brand(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "brands"
        ordering = ['name']

    def __str__(self):
        return self.name
class Size(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "sizes"
        ordering = ['name']

    def __str__(self):
        return self.name
class Color(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = "colors"
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_products')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, related_name='size_products')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, related_name='color_products')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()
    image_url1 = models.URLField(default="https://www.mrporter.com/variants/images/1647597340628696/in/w1500_q60.jpg")
    image_url2 = models.URLField(default="https://www.mrporter.com/variants/images/1647597340628696/in/w1500_q60.jpg")
    image_url3 = models.URLField(default="https://www.mrporter.com/variants/images/1647597340628696/in/w1500_q60.jpg")

    def __str__(self):
        return self.name

class Customer(models.Model):
    name = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Order(models.Model):
    user = models.CharField(max_length=100)
    items = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100)  

class OrderItem(models.Model):
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
