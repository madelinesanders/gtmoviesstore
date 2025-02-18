from django.shortcuts import render

def cart(request):
    return render(request, 'shopping_cart/cart.html')
