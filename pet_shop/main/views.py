from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, AnimalType, Review, Subscription, ContactRequest, ShopContact
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm
from cart.forms import CartAddProductForm


# Create your views here.

def index(request):

    reviews = Review.objects.filter(is_visible=True)

    return render(request, 'index/index.html', {
        'reviews': reviews
    })

def about(request):

    reviews = Review.objects.filter(is_visible=True)

    return render(request, 'about/about.html', {
        'reviews': reviews
    })

def cart(request):
    return render(request, 'cart/cart.html')

def checkout(request):
    return render(request, 'checkout/checkout.html')

def confirmation(request):
    return render(request, 'confirmation/confirmation.html')

def contact(request):
    shop_contact = ShopContact.objects.first()
    return render(request, 'contact/contact.html', {
        'shop_contact': shop_contact
    })

def login_user(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('user_account')
        else:
            messages.error(request, "Invalid email or password.")
    else:
        form = LoginForm()
    return render(request, 'login/login.html', {'form': form})

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('user_account')
    else:
        form = UserRegistrationForm()
    return render(request, 'login/registration.html', {'form': form})

@login_required(login_url='login')
def user_account(request):
    return render(request, 'login/user-account.html')

def logout_user(request):
    auth_logout(request)
    return render(request, 'login/logout.html')

def product_list(request):
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    animal_types = AnimalType.objects.all()

    search_request = request.GET.get('search', '')
    category_id = request.GET.get('category')
    animal_type_id = request.GET.get('animal_type')

    if search_request:
        products = products.filter(name__icontains=search_request)

    if category_id:
        products = products.filter(category_id=category_id)
        selected_category = get_object_or_404(Category, id=category_id)
    else:
        selected_category = None

    if animal_type_id:
        products = products.filter(animal_types__id=animal_type_id)
        selected_animal_type = get_object_or_404(AnimalType, id=animal_type_id)
    else:
        selected_animal_type = None

    paginator = Paginator(products, 9)
    page_number = request.GET.get('page', 1)
    paginated_products = paginator.get_page(page_number)

    reviews = Review.objects.filter(is_visible=True)

    return render(request, 'product_list/product_list.html', {
        'products': paginated_products,
        'search_request': search_request,
        'categories': categories,
        'animal_types': animal_types,
        'selected_category': selected_category,
        'selected_animal_type': selected_animal_type,
        'reviews': reviews
    })

def single_product(request, slug):
    product = get_object_or_404(Product, slug=slug)
    cart_product_form = CartAddProductForm()
    return render(request, 'single-product/single-product.html', {
        'product': product,
        'form': cart_product_form
    })


def load_more_products(request):
    page_number = request.GET.get('page')
    products = Product.objects.filter(available=True)
    paginator = Paginator(products, 9)

    try:
        paginated_products = paginator.get_page(page_number)
    except:
        return JsonResponse({'products': [], 'has_next': False})

    products_data = []
    for product in paginated_products:
        products_data.append({
            'name': product.name,
            'slug': product.slug,
            'price': product.price,
            'discount_price': product.discount_price,
            'is_discounted': product.is_discounted,
            'image_url': product.images.first().image.url if product.images.exists() else '',
        })

    return JsonResponse({'products': products_data, 'has_next': paginated_products.has_next()})

@csrf_exempt
def contact_request(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        if not name or not email or not subject or not message:
            return JsonResponse({"success": False, "message": "All fields are required."}, status=400)
        
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({"success": False, "message": "A mistake? Input the correct email"}, status=400)
        
        ContactRequest.objects.create(name=name, email=email, subject=subject, message=message)
        
        return JsonResponse({"success": True, "message": "Thanks for reaching out! We will get back to you soon."})
    else:
        return JsonResponse({"success": False, "message": "Something went wrong, please try later."}, status=400)


@require_POST
def subscribe(request):
    email = request.POST.get('email', '').strip()

    try:
        validate_email(email)
    except ValidationError:
        return JsonResponse({"success": False, "message": "A mistake? Input the correct email"})

    if Subscription.objects.filter(email=email).exists():
        return JsonResponse({"success": False, "message": "Thank you, you are already subscribed"})
    
    Subscription.objects.create(email=email)
    return JsonResponse({"success": True, "message": "Thank you for your subscription!"})