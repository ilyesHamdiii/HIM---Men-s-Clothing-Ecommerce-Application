from .models import CartItem

def cart_total(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        cart_count = sum(item.quantity for item in cart_items)
    else:
        total_price = 0
        cart_count = 0
    return {
        'cart_total_price': total_price,
        'cart_total_count': cart_count,
    }
