from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index/index.html')

def about(request):
    return render(request, 'about/about.html')

def cart(request):
    return render(request, 'cart/cart.html')

def checkout(request):
    return render(request, 'checkout/checkout.html')

def confirmation(request):
    return render(request, 'confirmation/confirmation.html')

def contact(request):
    return render(request, 'contact/contact.html')

def login(request):
    return render(request, 'login/login.html')

def product_list(request):
    return render(request, 'product_list/product_list.html')

def single_product(request):
    return render(request, 'single-product/single-product.html')
