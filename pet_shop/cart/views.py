from decimal import Decimal
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Product
from .cart import Cart
from .forms import CartAddProductForm, CheckoutForm
from .models import Order

# Create your views here.

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data    
        cart.add(product=product, quantity=cd['quantity'], override_quantity=cd['override'])
    return redirect('cart:cart_detail')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

@require_POST
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    is_empty = len(cart) == 0
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'override': True})
    return render(request, 'cart/cart.html', {'cart': cart, 'is_empty': is_empty})


def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = Order(
                user=request.user if request.user.is_authenticated else None,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                company=form.cleaned_data['company'],
                phone=form.cleaned_data['phone'],
                email=form.cleaned_data['email'],
                country=form.cleaned_data['country'],
                address_line_1=form.cleaned_data['address_line_1'],
                address_line_2=form.cleaned_data['address_line_2'],
                city=form.cleaned_data['city'],
                zip_code=form.cleaned_data['zip_code'],
                order_notes=form.cleaned_data['order_notes'],
                items=cart.cart,
                subtotal=cart.get_total_price(),
                shipping_cost=Decimal('0.00'),
                total=cart.get_total_price()
            )
            order.save()
            cart.clear()
            return redirect('cart:confirmation')
    else:
        form = CheckoutForm()
    return render(request, 'cart/checkout.html', {'cart': cart, 'form': form,})

def confirmation(request):
    return render(request, 'cart/confirmation.html')

