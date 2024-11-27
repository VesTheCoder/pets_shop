from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('login/', views.login_user, name='login'),
    path('registration/', views.register_user, name='registration'),
    path('user-account/', views.user_account, name='user_account'),
    path('logout/', views.logout_user, name='logout'),
    path('product_list/', views.product_list, name='product_list'),  
    path('single-product/<slug:slug>/', views.single_product, name='single-product'),
    path('load-more-products/', views.load_more_products, name='load_more_products'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('contact_request/', views.contact_request, name='contact_request'),
]
